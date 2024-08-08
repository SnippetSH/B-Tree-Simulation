def makeResult(r):
    decoded_result = r.decode('utf-8')
    # print(decoded_result)
    # print(type(decoded_result))

    # 출력된 결과를 줄 단위로 분리
    lines = decoded_result.splitlines()

    d = []

    for line in lines:
        parts = line.split()
        d.append(int(parts[0]))

    n = max(d)


    if(n >= 2):
        # 결과를 저장할 딕셔너리
        result = {(i+1): [] for i in range(n)}

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
                        result[(depth_level)].append(temp_lists[depth_level])
                        temp_lists[depth_level] = []
                if temp_lists[2]:
                    result[2].append(temp_lists[2])
                    temp_lists[2] = []
                result[1].append([key])
            else:
                if current_depth and depth < current_depth:
                    for depth_level in range(depth + 1, n + 1):
                        if temp_lists[depth_level]:
                            result[(depth_level)].append(temp_lists[depth_level])
                            temp_lists[depth_level] = []
                temp_lists[depth].append(key)
            
            current_depth = depth

        # 마지막 남은 임시 리스트 처리
        for depth_level in range(2, n+1):
            if temp_lists[depth_level]:
                result[(depth_level)].append(temp_lists[depth_level])
        
        result['max'] = n
        result = {'max': result.pop('max'), **result}
    else:
        arr = [[]]
        for line in lines:
            parts = line.split()
            key = int(parts[2])
            arr[0].append(key)
        
        result = {
            'max': 1,
            1: arr
        }
        
    return result