
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

function debug_end()
	valuex a#1
	return #a
endfunction

function debug_phase_init(ss pointer)
	sv of%%p_offsets
	if of#!=(NULL)
		sv a;setcall a debug_mark_get()
		set a# pointer
		call debug_mark_add()
	endif
endfunction
function debug_phase_parse(ss pointer)
	sv of%%p_offsets
	if of#!=(NULL)
		import "action_code_values_index" action_code_values_index
		sd x;setcall x action_code_values_index()
		set x x#
		sv end;setcall end debug_end()
		set end end#
		sv a;setcall a debug_mark_get()
		setcall a debug_mark_get()
		while a#!=end           # != end? it's not with spaces at end, therefore ";   \nabc" can go wrong
			set a#d^ x   #x is index, 0,1..n
			if a#>=^pointer   # and > ? same like above
				break
			endif
			call debug_mark_add()
			setcall a debug_mark_get()
		endwhile
	endif
endfunction
#function debug_phase_code()
#endfunction

import "mem_free" mem_free

function debug_free()
	sv of%%p_offsets
	if of#!=(NULL)
		call mem_free(of)
	endif
endfunction

function debug_action_parse()
	sv of%%p_offsets
	if of#!=(NULL)
		call debug_mark_start()  #second iteration
	endif
endfunction

import "row_termination" row_termination



importaftercall ebool

import "memalloc" memalloc

function debug_init(sd bool)
	sv of%%p_offsets
	if bool==(TRUE)
		setcall of# memalloc(0)
	endif
endfunction

function debug_action_init(ss ac)
	sv of%%p_offsets
	if of#!=(NULL)
		sd row=1     #at least one row, example: row 1,3 actions
		while ac#!=0
			call row_termination(#ac,#row)
			inc ac
		endwhile
		mult row :
		import "memrealloc" memrealloc
		setcall of# memrealloc(of#,row)
		call debug_mark_start()  #prepare for first iteration

		#store end, more at phase_parse
		add row of#
		sv end;setcall end debug_end()
		set end# row
	endif
endfunction
