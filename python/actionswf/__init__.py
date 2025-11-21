
import ctypes

#try: #in PATH
_lib=ctypes.cdll.LoadLibrary("libactionswf.so")
#except Exception:
#lib=ctypes.cdll.LoadLibrary("actionswf.dll")

from . import _swf
_swf.init(_lib)
new=_lib.swf_new

from . import _tool
_tool.init(_lib)
erbool_get=_lib.erbool_get
