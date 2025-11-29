
import ctypes

def init(lib):
	lib.action.argtypes = [ ctypes.c_char_p ]
	lib.actionf.argtypes = [ ctypes.c_char_p, ctypes.c_char_p ]
	global _lib
	_lib=lib

def action(ac):
	_lib.action(ac)
def actionf(*args, buffer, format): #You must place the variadic ones first in the function definition
	_lib.action(buffer, format, *args) #call this like this: (buffer=b, format="...", *["a",1])
