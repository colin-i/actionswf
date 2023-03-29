
format elfobj64

include "../include/prog.h"

function debug_mark()
	valuex row#1
	return #row
endfunction
function debug_mark_start()
	sv a;setcall a debug_mark()
	set a# 0
endfunction
function debug_mark_add()
	sv a;setcall a debug_mark()
	add a# :
endfunction
function debug_mark_get()
	value offsets=NULL
	const p_offsets^offsets

	sv a;setcall a debug_mark()
	sv b;set b a#
	add b offsets
	return b
endfunction

function debug_target()
	valuex a#1
	return #a
endfunction

function debug_end()
	valuex a#1
	return #a
endfunction
function debug_actions()
	datax a#1  #65535
	return #a
endfunction

import "mem_free" mem_free
import "f_close" f_close

function debug_free()
	sv of%p_offsets
	if of#!=(NULL)
		call mem_free(of)
		value file=NULL
		const p_debug_file^file
		call f_close(#file)
	endif
endfunction

function debug_phase_init(ss pointer)
	sv of%p_offsets
	if of#!=(NULL)
		sv a;setcall a debug_mark_get()
		set a# pointer
		call debug_mark_add()
	endif
endfunction
function debug_phase_parse(ss pointer)
	sv of%p_offsets
	if of#!=(NULL)
		sv a
		sv start;setcall start debug_mark_get()
		sv target;setcall target debug_target()
		if target#==(NULL)
		#need to know empty rows
			set a start
			while pointer>a#
				incst a
			endwhile
			set target# a
		else
			set a target#
		endelse
		#if pointer>=^a#  # and > ? it's not with spaces at end, therefore ";   \nabc" can go wrong
		if pointer<^a#
			ret
		endif
		import "action_code_get" action_code_get   #the pointer is not reallocated, can use offset but will be slower
		sd x;setcall x action_code_get()
		while start#<^pointer   #or a
			set start# x
			call debug_mark_add()
			setcall start debug_mark_get()
		endwhile
		set start# x      ##also,set for this row, can be the only set
		call debug_mark_add()
		set target# (NULL)
	endif
endfunction
function debug_phase_code_add()
	sv of%p_offsets
	if of#!=(NULL)
		sd acts;setcall acts debug_actions()
		inc acts#
	endif
endfunction

function debug_action_phase()
	sv of%p_offsets
	if of#!=(NULL)
		call debug_mark_start()  #second and third iteration
	endif
endfunction

import "row_termination" row_termination

importx "strlen" strlen
importx "sprintf" sprintf



importaftercall ebool

import "memalloc" memalloc
import "f_open_mem" f_open_mem

function debug_init(sd bool,sd path)
	sv of%p_offsets
	if bool==(TRUE)
		setcall of# memalloc(0)

		sd a;setcall a strlen(path)
		add a 5
		sd b;setcall b memalloc(a)
		call sprintf(b,"%s.log",path)
		sv file%p_debug_file
		setcall file# f_open_mem(b,"wb")
	endif
endfunction

import "f_printf2" f_printf2

function debug_action_init(ss ac)
	sv of%p_offsets
	if of#!=(NULL)
		sd start;set start ac

		sd row=1     #at least one row, example: row 1,3 actions
		while ac#!=0
			call row_termination(#ac,#row)
			inc ac
		endwhile

		#out rows\nac\n
		sv file%p_debug_file
		char f={Percent,l,u,LineFeed,Percent,s,LineFeed,Nullchar}
		call f_printf2(file#,#f,row,start)

		mult row :
		import "memrealloc" memrealloc
		setcall of# memrealloc(of#,row)

		call debug_mark_start()  #prepare for first iteration

		#set target to 0, for recognizing blank rows at second iteration
		sv target;setcall target debug_target()
		set target# (NULL)

		add row of#
		sv end;setcall end debug_end()   #at third iteration
		set end# row
		#
		sd acts;setcall acts debug_actions()
		set acts# 0
	endif
endfunction

function debug_phase_code(sd codepointer)
	sv of%p_offsets
	if of#!=(NULL)
		sv a;setcall a debug_mark_get()
		if codepointer==a#   #can also be smaller
			sv b;set b a
			sv end;setcall end debug_end()
			while codepointer==b#
				call debug_mark_add()
				setcall b debug_mark_get()
				if b==end#
					break
				endif
			endwhile
			sub b a
			div b :

			#out rows,actions\n
			sd acts;setcall acts debug_actions()
			sv file%p_debug_file
			char f={Percent,l,u,Comma,Percent,u,LineFeed,Nullchar}   #must escape \n or something
			call f_printf2(file#,#f,b,acts#)
			set acts# 0
		endif
	endif
endfunction