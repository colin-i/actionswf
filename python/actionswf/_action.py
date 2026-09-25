
import ctypes

def init(lib):
	lib.action.argtypes = [ ctypes.c_char_p ]
	lib.actionf.argtypes = [ ctypes.c_char_p, ctypes.c_char_p ]
	lib.actionf.restype = ctypes.c_size_t
	lib.actionsf.argtypes = [ ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_size_t), ctypes.c_char_p ]
	lib.actiond.argtypes = [ ctypes.c_char_p ]

	lib.action_sprite.argtypes = [ ctypes.c_int, ctypes.c_char_p ]
	lib.action_init_sprite.argtypes = [ ctypes.c_int, ctypes.c_char_p ]
	lib.actionf_sprite.argtypes = [ ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p ]
	lib.actionf_init_sprite.argtypes = [ ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p ]
	lib.actionsf_sprite.argtypes = [ ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_size_t), ctypes.c_char_p ]
	lib.actionsf_init_sprite.argtypes = [ ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_size_t), ctypes.c_char_p ]

	lib.actions_free.argtypes = [ ctypes.c_char_p ]

	global _lib
	_lib=lib

def action(ac):
	_lib.action(ac.encode('utf-8'))
def actionf(buffer, format, *args): # ... ,b'a',1 or ,*[b'a',1]
	return _lib.actionf(buffer, format.encode('utf-8'), *args) #buffer example: (ctypes.c_char * 10)()
def actionsf(psize, pbuffer, format, *args):
	_lib.actionsf(psize, pbuffer, format.encode('utf-8'), *args)
def actiond(ac):
	_lib.actiond(ac.encode('utf-8'))

def action_sprite(sprite, ac):
	_lib.action_sprite(sprite, ac.encode('utf-8'))
def action_init_sprite(sprite, ac):
	_lib.action_init_sprite(sprite, ac.encode('utf-8'))
def actionf_sprite(sprite, buffer, format, *args):
	_lib.actionf_sprite(sprite, buffer, format.encode('utf-8'), *args)
def actionf_init_sprite(sprite, buffer, format, *args):
	_lib.actionf_init_sprite(sprite, buffer, format.encode('utf-8'), *args)
def actionsf_sprite(sprite, pbuffer, psize, format, *args):
	_lib.actionsf_sprite(sprite, pbuffer, psize, format.encode('utf-8'), *args)
def actionsf_init_sprite(sprite, pbuffer, psize, format, *args):
	_lib.actionsf_init_sprite(sprite, pbuffer, psize, format.encode('utf-8'), *args)

def actions_free(buffer):
	_lib.actions_free(buffer)
