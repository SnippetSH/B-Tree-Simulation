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
for i in range(1, 101):
    lib.Insert(tree, i, b"11")

#lib.Delete(tree, 10)

# 트리 순회 및 출력 가져오기
result = lib.TraverseBtree(tree)
decoded_result = result.decode('utf-8')
print(decoded_result)
print(type(decoded_result))

# 출력된 결과를 줄 단위로 분리
lines = decoded_result.splitlines()

d = []

for line in lines:
    parts = line.split()
    d.append(int(parts[0]))

n = max(d)

# 결과를 저장할 딕셔너리
result = {i+1: [] for i in range(n)}

# 임시 리스트를 depth별로 동적으로 생성
temp_lists = {i: [] for i in range(2, n+1)}

current_depth = None

for line in lines:
    parts = line.split()
    depth = int(parts[0])
    key = int(parts[2])
    
    if depth == 1:
        # depth 1이 나오면 모든 임시 리스트를 결과에 추가
        for depth_level in range(3, n+1):
            if temp_lists[depth_level]:
                result[depth_level].append(temp_lists[depth_level])
                temp_lists[depth_level] = []
        if temp_lists[2]:
            result[2].append(temp_lists[2])
            temp_lists[2] = []
        result[1].append([key])
    else:
        if current_depth and depth < current_depth:
            for depth_level in range(depth + 1, n + 1):
                if temp_lists[depth_level]:
                    result[depth_level].append(temp_lists[depth_level])
                    temp_lists[depth_level] = []
        temp_lists[depth].append(key)
    
    current_depth = depth

# 마지막 남은 임시 리스트 처리
for depth_level in range(2, n+1):
    if temp_lists[depth_level]:
        result[depth_level].append(temp_lists[depth_level])

# 결과 출력
print(result)


# 할당된 메모리 해제
#lib.FreeString(result)

# 트리 파괴
lib.DestroyBtree(tree)
