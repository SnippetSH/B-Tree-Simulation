import ctypes
import os

# DLL 파일 경로 설정
dll_path = os.path.join(os.path.dirname(__file__), 'API', 'Clib', 'Btree.so')

# DLL 로드
lib = ctypes.cdll.LoadLibrary(dll_path)

# 함수 설정
lib.MakeBtree.restype = ctypes.POINTER(ctypes.c_void_p)

lib.Insert.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_int, ctypes.c_char_p]
lib.Insert.restype = None

lib.Search.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_int]
lib.Search.restype = ctypes.c_char_p

lib.Delete.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_int]
lib.Delete.restype = None

lib.DestroyBtree.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
lib.DestroyBtree.restype = None

lib.TraverseBtree.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
lib.TraverseBtree.restype = ctypes.c_char_p

# Btree 생성
tree = lib.MakeBtree()
print(type(tree))

# 값 삽입
lib.Insert(tree, 10, b"100")  # Note the b prefix to convert to byte string
lib.Insert(tree, 20, b"200")  # Note the b prefix to convert to byte string
lib.Insert(tree, 30, b"200")
lib.Insert(tree, 40, b"200")
lib.Insert(tree, 50, b"200")
lib.Insert(tree, 60, b"200")
lib.Insert(tree, 70, b"200")
lib.Insert(tree, 80, b"200")
lib.Insert(tree, 90, b"200")
lib.Insert(tree, 100, b"200")
lib.Insert(tree, 110, b"200")
lib.Insert(tree, 120, b"200")
lib.Insert(tree, 130, b"200")
lib.Insert(tree, 140, b"200")
lib.Insert(tree, 150, b"200")
lib.Insert(tree, 160, b"200")
lib.Insert(tree, 170, b"200")
lib.Insert(tree, 180, b"200")
lib.Insert(tree, 190, b"200")
lib.Insert(tree, 200, b"200")

#lib.Delete(tree, 10)

# 트리 순회 및 출력 가져오기
result = lib.TraverseBtree(tree)
print(result.decode('utf-8'))

# 할당된 메모리 해제
#lib.FreeString(result)

# 트리 파괴
lib.DestroyBtree(tree)
