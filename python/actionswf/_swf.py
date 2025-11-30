
import ctypes


class ButtonData(ctypes.Structure):
	pass
ButtonData._fields_ = [("def_fill", ctypes.c_uint)
				,("def_line_sz", ctypes.c_int)
				,("def_line", ctypes.c_uint)

				,("ov_fill", ctypes.c_uint)
				,("ov_line_sz", ctypes.c_int)
				,("ov_line", ctypes.c_uint)

				,("dn_fill", ctypes.c_uint)
				,("dn_line_sz", ctypes.c_int)
				,("dn_line", ctypes.c_uint)

				,("xcurve", ctypes.c_int)
				,("ycurve", ctypes.c_int)

				,("text", ctypes.c_char_p)
				,("font_id", ctypes.c_int)
				,("font_height", ctypes.c_int)
				,("font_vertical_offset", ctypes.c_int)
				,("font_color", ctypes.c_int)

				,("actions", ctypes.c_char_p)]
ButtonData._pack_ = 4

class EditText(ctypes.Structure):
	pass
EditText._fields_ = [("fontid", ctypes.c_int)
				,("font_height", ctypes.c_int)
				,("fontclassname", ctypes.c_char_p)
				,("rgba", ctypes.c_int)
				,("maxlength", ctypes.c_int)
				,("initialtext", ctypes.c_char_p)
				,("layout_align", ctypes.c_int)
				,("layout_leftmargin", ctypes.c_int)
				,("layout_rightmargin", ctypes.c_int)
				,("layout_indent", ctypes.c_int)
				,("layout_leading", ctypes.c_int)]
EditText._pack_ = 4

def init(lib):
	lib.swf_button.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.POINTER(ButtonData)] #lib.swf_button.restype = c_int #https://docs.python.org/3/library/ctypes.html: By default functions are assumed to return the C int type.
	lib.swf_button_last.argtypes = [ctypes.c_char_p,ctypes.c_char_p] #lib.swf_button_last.restype = c_int

	lib.swf_font.argtypes = [ctypes.c_char_p,ctypes.c_char] #lib.swf_font.restype = c_int
	lib.swf_font_basic.argtypes = [ctypes.c_char_p] #lib.swf_font_basic.restype = c_int

	lib.swf_text.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.c_char_p,ctypes.c_short,ctypes.POINTER(EditText)] #lib.swf_text.restype = c_int

	lib.swf_shape.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.POINTER(ctypes.c_int)] #lib.swf_shape.restype = c_int  # (ctypes.c_int * 2)(*[4, 5])
	lib.swf_shape_basic.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int] #lib.swf_shape_basic.restype = c_int
	lib.swf_shape_bitmap.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.c_int] #lib.swf_shape_bitmap.restype = c_int
	lib.swf_shape_bitmap_clipped.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.c_int] #lib.swf_shape_bitmap_clipped.restype = c_int
	lib.swf_shape_border.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int] #lib.swf_shape_border.restype = c_int

	lib.swf_image.argtypes = [ctypes.c_char_p] #lib.swf_image.restype = c_int
	lib.swf_image_ex.argtypes = [ctypes.c_char_p,ctypes.POINTER(ctypes.c_int)] #lib.swf_image.restype = c_int  # (ctypes.c_int * 2)()
	lib.swf_dbl.argtypes = [ctypes.c_char_p] #lib.swf_dbl.restype = c_int
	lib.swf_dbl_ex.argtypes = [ctypes.c_char_p,ctypes.POINTER(ctypes.c_int)] #lib.swf_dbl_ex.restype = c_int
	lib.swf_dbl_width.argtypes = [ctypes.c_char_p] #lib.swf_dbl_width.restype = c_int
	lib.swf_dbl_height.argtypes = [ctypes.c_char_p] #lib.swf_dbl_height.restype = c_int

	lib.swf_new.argtypes = [ctypes.c_char_p,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_ubyte] #lib.swf_new.restype = None # else c_int is default , is ok, there is still a wrapper to enforce nr of args

	global _lib
	_lib=lib

def button(width,height,buttondata):
	return _lib.swf_button(width,height,buttondata)
def button_last(actions,newtext):
	return _lib.swf_button_last(actions,newtext)

def font(fontname,font_flags):
	return _lib.swf_font(fontname,font_flags)
def font_basic(fontname):
	return _lib.swf_font_basic(fontname)

def text(bound_width,bound_height,variablename,flags,structure):
	return _lib.swf_text(bound_width,bound_height,variablename,flags,structure)

def shape(width,height,args):
	return _lib.swf_shape(width,height,args)
def shape_basic(width,height,fillcolor,linecolor):
	return _lib.swf_shape_basic(width,height,fillcolor,linecolor)
def shape_bitmap(bitmapId,width,height):
	return _lib.swf_shape_bitmap(bitmapId,width,height)
def shape_bitmap_clipped(bitmapId,width,height):
	return _lib.swf_shape_bitmap_clipped(bitmapId,width,height)
def shape_border(width,height,linesize,linecolor):
	return _lib.swf_shape_border(width,height,linesize,linecolor)

def image(imagepath):
	return _lib.swf_image(imagepath)
def image_ex(imagepath,wh):
	return _lib.swf_image_ex(imagepath,wh)
def dbl(imagepath):
	return _lib.swf_dbl(imagepath)
def dbl_ex(imagepath,wh):
	return _lib.swf_dbl_ex(imagepath,wh)
def dbl_width(imagepath):
	return _lib.swf_dbl_width(imagepath)
def dbl_height(imagepath):
	return _lib.swf_dbl_height(imagepath)

def done():
	_lib.swf_done()
def new(path,width,height,backgroundcolor,fps):
	_lib.swf_new(path,width,height,backgroundcolor,fps)
