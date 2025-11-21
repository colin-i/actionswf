
import ctypes

def main():
	#try: #in PATH
	lib=ctypes.cdll.LoadLibrary("libactionswf.so")
	#except Exception:
	#lib=ctypes.cdll.LoadLibrary("actionswf.dll")

#if __name__ == "__main__":
main()
