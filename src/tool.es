Format ElfObj64

import "erbool" erbool
functionx erbool_get()
    ss p;setcall p erbool()
    return p#
endfunction

functionx erbool_reset()
    ss p;setcall p erbool()
    set p# 0
endfunction

functionx freereset()
	import "freestart" freestart
	import "freelater" freelater
	call freestart()
	call freelater()
endfunction
