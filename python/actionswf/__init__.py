
from enum import IntEnum
class flag(IntEnum):
	prex=0x8
	x=   0x80
class flags(IntEnum):
	x=flag.prex|flag.x
#class flagss
class FILLSTYLE(IntEnum):
	no=                          -1
	solid=                       0
	repeating_bitmap=            0x40
	clipped_bitmap=              0x41
	nonsmoothed_repeating_bitmap=0x42
	nonsmoothed_clipped_bitmap=  0x43
class State(IntEnum):
	MoveTo=    1
	FillStyle0=1 << 1
	FillStyle1=1 << 2
	LineStyle= 1 << 3
	NewStyles= 1 << 4
class ButtonState(IntEnum):
	Up=     1
	Over=   1 << 1
	Down=   1 << 2
	HitTest=1 << 3

import ctypes

#try: #in PATH
_lib=ctypes.cdll.LoadLibrary("libactionswf.so")
#except Exception:
#lib=ctypes.cdll.LoadLibrary("actionswf.dll")

from . import _swf
_swf.init(_lib)
ButtonData=_swf.ButtonData
EditText=_swf.EditText
button=_swf.button
button_last=_swf.button_last
font=_swf.font
font_basic=_swf.font_basic
text=_swf.text
done=_swf.done
new=_swf.new

from . import _action
_action.init(_lib)
action=_action.action

from . import _tool
_tool.init(_lib)
erbool_get=_tool.erbool_get
