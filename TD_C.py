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
                'EP0002_0010': {
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
def json_get(file_data: dict, getv: str):
    box = []
    for k, y in file_data.items():
        if k == getv:
            box.append(y)
        elif isinstance(y, dict):
            result = json_get(y,getv)

            box.extend(result)

    return box

def json_insert(data1: dict, data2: dict):
    """
    :param data1: 원본 데이터
    :param data2: 입력할 값의 경로
    """
    for k, v in data1.items():
        for i, j in data2.items():
            if isinstance(v, dict):
                if isinstance(j, dict):
                    if k != i:
                        data1[i] = j
                        return
                    json_insert(v, j)


def json_delete(data1: dict, data2: dict):
    """
    :param data1: 원본 데이터
    :param data2: 삭제할 값의 경로
    """
    for k, v in data1.items():
        for i, j in data2.items():
            if not isinstance(j, dict):
                data1[i] = None
                return
            if isinstance(v, dict):
                if isinstance(j, dict):
                    json_delete(v, j)


def json_modify(data: dict, key_lst: list, val) -> None:
    """
    :param data: 원본 데이터 (json)
    :param key_lst: 바꿀 값의 경로
    :param val: 바꿀 밸류 값
    """
    for key in key_lst:
        last_key = key_lst[-1]
        if last_key in data:
            data[last_key] = val
            return
        if key in data and isinstance(data[key], dict):
            json_modify(data[key], key_lst[1:], val)


# Get
result = json_get(file_data, 'frange')
print(result)

# Insert
insert_key_data = {'project': {'shot': {'EP0005': {'EP0005_0050': {'frange': [1001, 1200]}}}}}
json_insert(file_data, insert_key_data)

print("-"*110, "\n")
print("Insert Result", "\n")
pprint.pprint(file_data)


# Delete
delete_key_data = {'project': {'shot': {'EP0005': None}}}
json_delete(file_data, delete_key_data)

print("-"*110, "\n")
print("Delete Result", "\n")
pprint.pprint(file_data)


# Modify
key_data = ['project', 'shot', 'EP0001', 'EP0001_0010', 'frange']
json_modify(file_data, key_data, [4321, 1234])

print("-"*110, "\n")
print("Modify Result", "\n")
pprint.pprint(file_data)
