
import ctypes

def init(lib):
	lib.erbool_get.restype = ctypes.c_char # else c_int is default #lib.erbool_get.argtypes is for at least, not equal or at most
	#erbool_reset

	#freereset

	lib.xlog_pad_get.restype = ctypes.c_ubyte
	lib.xlog_pad_set.argtypes = [ctypes.c_ubyte]

	global _lib
	_lib=lib

def erbool_get():
	return _lib.erbool_get()[0]
def erbool_reset():
	_lib.erbool_reset()

def freereset():
	_lib.freereset()

def xlog_pad_get():
	return _lib.xlog_pad_get()
def xlog_pad_set(new_pad):
	_lib.xlog_pad_set(new_pad)
