import os
import ctypes

def init():
    # 현재 운영체제 감지
    current_os = os.name  # 'posix' for Linux/Mac, 'nt' for Windows

    # 파일 경로 설정
    if current_os == 'posix':
        path = os.path.join(os.path.dirname(__file__), 'Clib', 'Btree.so')  # 리눅스 또는 맥용 .so 파일 경로
        lib = ctypes.cdll.LoadLibrary(path)
    elif current_os == 'nt':
        path = os.path.join(os.path.dirname(__file__), 'Clib', 'Btree.dll')  # 윈도우용 .dll 파일 경로
        lib = ctypes.CDLL(path)
    else:
        raise OSError('Unsupported operating system')
    
    return lib

def makeTree(lib):
    lib.MakeBtree.restype = ctypes.POINTER(ctypes.c_void_p)
    return lib.MakeBtree()

def Insert(lib, tree, n, s):
    lib.Insert.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
    lib.Insert.restype = None

    lib.Insert(tree, n, s.encode('utf-8'))

def Delete(lib, tree, n):
    lib.Delete.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_int]
    lib.Delete.restype = None

    lib.Delete(tree, n)

def Search(lib, tree, n):
    lib.Search.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_int]
    lib.Search.restype = ctypes.c_char_p

    result = lib.Search(tree, n)
    return result

def Traverse(lib, tree):
    lib.TraverseBtree.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    lib.TraverseBtree.restype = ctypes.c_char_p

    result = lib.TraverseBtree(tree)
    return result

def Destroy(lib, tree):
    lib.DestroyBtree.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    lib.DestroyBtree.restype = None

    lib.DestroyBtree(tree)