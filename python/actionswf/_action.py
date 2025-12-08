
import ctypes

def init(lib):
	lib.action.argtypes = [ ctypes.c_char_p ]
	lib.actionf.argtypes = [ ctypes.c_char_p, ctypes.c_char_p ]
	lib.actiond.argtypes = [ ctypes.c_char_p ]

	lib.action_sprite.argtypes = [ ctypes.c_int, ctypes.c_char_p ]
	lib.actionf_sprite.argtypes = [ ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p ]
	lib.action_init_sprite.argtypes = [ ctypes.c_int, ctypes.c_char_p ]
	lib.actionf_init_sprite.argtypes = [ ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p ]

	global _lib
	_lib=lib

def action(ac):
	_lib.action(ac.encode('utf-8'))
def actionf(*args, buffer, format): #You must place the variadic ones first in the function definition  #call this like this: (buffer=b, format="...", *["a",1])
	_lib.actionf(buffer, format.encode('utf-8'), *args) #buffer example: (ctypes.c_char * 10)()
def actiond(ac):
	_lib.actiond(ac.encode('utf-8'))

def action_sprite(sprite, ac):
	_lib.action_sprite(sprite, ac.encode('utf-8'))
def actionf_sprite(*args, sprite, buffer, format):
	_lib.actionf_sprite(sprite, buffer, format.encode('utf-8'), *args)
def action_init_sprite(sprite, ac):
	_lib.action_init_sprite(sprite, ac.encode('utf-8'))
def actionf_init_sprite(*args, sprite, buffer, format):
	_lib.actionf_init_sprite(sprite, buffer, format.encode('utf-8'), *args)
