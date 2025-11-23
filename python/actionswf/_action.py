
import ctypes

def init(lib):
	lib.action.argtypes = [ ctypes.c_char_p ]
	global _lib
	_lib=lib

def action(ac):
	_lib.action(ac)
