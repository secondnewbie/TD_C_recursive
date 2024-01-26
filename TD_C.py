import pprint

file_data = {
    'project': {
        'name': 'mermaid',
        'datetime': '2024-02-01',
        'shot': {
            'EP0001': {
                'EP0001_0010': {
                    'fps': 24,
                    'frange': [1001, 1100],
                    'author': ['anon', 'aa'],
                    'filepath': {
                        'hipfile': '/home/rapa/down',
                        'nkfile': '/home/rapa/nk',
                    }
                }
            },
            'EP0002': {
                'EP002_0010': {
                    'fps': 24,
                    'frange': [1001, 1050],
                    'author': 'anon',
                }
            },
        }
    }
}


# key_data = {'project': {'shot': {'EP0001': {'EP0001_0010': {'frange': None}}}}}


# class recursive:
def json_get(self):
    pass


def json_insert(data1: dict, data2: dict):
    for k, v in data1.items():
        for i, j in data2.items():
            if isinstance(v, dict):
                if isinstance(j, dict):
                    if k != i:
                        data1[i] = j
                        print(data1)
                        return
                    json_insert(v, j)


def json_delete(data1: dict, data2: dict):
    for k, v in data1.items():
        for i, j in data2.items():
            if i == 'EP0005':
                data1[i] = None
                print(data1)
                return
            if isinstance(v, dict):
                if isinstance(j, dict):
                    json_delete(v, j)


def json_modify(data: dict, key_lst: list, val) -> None:
    """
    :param data: 값을 바꿀 딕셔너리
    :param key_lst: 값을 바꿀 키 경로(리스트)
    :param val: 변경할 밸류 값
    """
    for key in key_lst[:-1]:
        if key in data and isinstance(data[key], dict):  # 바꾸려는 키값이 data에 포함된 동시에 딕셔너리인지 확인
            data = data[key]  # 딕셔너리 탐색을 위해 현재 키 값을 'data'로 업데이트
        else:
            return

    last_key = key_lst[-1]  # 마지막 키 값을 변수로 지정
    if last_key in data:
        data[last_key] = val

    pprint.pprint(file_data)  # 결과 프린트


insert_key_data = {'project': {'shot': {'EP0005': {'EP0005_0050': {'frange': [1001, 1200]}}}}}
key_data = ['project', 'shot', 'EP0001', 'EP0001_0010', 'frange']

# Insert
json_insert(file_data, insert_key_data)
pprint.pprint(file_data)

# Delete
delete_key_data = {'project': {'shot': {'EP0005': None}}}
json_delete(file_data, delete_key_data)
pprint.pprint(file_data)


# Modify
json_modify(file_data, key_data, [4321, 1234])
