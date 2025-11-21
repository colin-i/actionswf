
import ctypes

def init(lib):
	lib.swf_new.argtypes = [ctypes.c_void_p,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_char]
	#lib.swf_new.restype = None # else c_int is default , is ok, there is still a wrapper to enforce nr of args
	global _lib
	_lib=lib

def new(path,width,height,backgroundcolor,fps):
	_lib.swf_new(path,width,height,backgroundcolor,fps)
