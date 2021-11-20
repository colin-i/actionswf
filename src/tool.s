Format ElfObj64

import "erbool" erbool
function erbool_get()
    ss p;setcall p erbool()
    return p#
endfunction

function erbool_reset()
    ss p;setcall p erbool()
    set p# 0
endfunction

include "../include/prog.h"

import "swf_mem" swf_mem
function abort()
    #free and set initial null/-1.....
    call swf_mem((mem_exp_free))
endfunction