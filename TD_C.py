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

def json_insert(data1:dict, data2:dict):
    for k, v in data1.items():
        for i, j in data2.items():
            if isinstance(v, dict):
                if isinstance(j, dict):
                    if k != i:
                        data1[i] = j
                        # print(data1)
                        return
                    json_insert(v, j)

def json_delete(data1:dict, data2:dict):
    for k, v in data1.items():
        for i, j in data2.items():
            if i == 'EP0005':
                data1[i] = None
                print(data1)
                return
            if isinstance(v, dict):
                if isinstance(j, dict):
                    json_delete(v, j)


def json_modify(self):
    pass

insert_key_data = {'project': {'shot': {'EP0005': {'EP0005_0050': {'frange': [1001, 1200]}}}}}
json_insert(file_data, insert_key_data)
print(file_data)

json_modify(file_data, ['project', 'shot', 'EP0001', 'EP0001_0010', 'frange'], [1001, 1100])
json_modify(file_data, key_data, [1001, 1100])

delete_key_data = {'project': {'shot': {'EP0005': None}}}
json_delete(file_data, delete_key_data)
print(file_data)
