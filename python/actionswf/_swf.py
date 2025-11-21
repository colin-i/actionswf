
import ctypes

def init(lib):
	lib.swf_new.argtypes = [ctypes.c_void_p,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_char]
