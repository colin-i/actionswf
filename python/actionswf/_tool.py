
import ctypes

def init(lib):
	lib.erbool_get.restype = ctypes.c_char # else c_int is default #lib.erbool_get.argtypes is for at least, not equal or at most
	global _lib
	_lib=lib

def erbool_get(): #this to enforce no arguments
	return _lib.erbool_get()
