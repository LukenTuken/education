import json


def searcher(structure: dict, key: str) -> str:
    """
    Рекурсивная функция поиска ключа и возвращающая значение в составном словаре.
    """
    if key in structure:
        return structure[key]

    for sub_structure in structure.values():
        if isinstance(sub_structure, dict):
            result = searcher(sub_structure, key)
            if result:
                break
    else:
        result = None

    return result


#  Производим чтение данных из файлов.
with open('json_old.json', 'r') as old_file:
    old_file_data = json.load(old_file)

with open('json_new.json', 'r') as new_file:
    new_file_data = json.load(new_file)

result = {}
diff_list = ['services', 'staff', 'datetime']

#  Производим сравнение значений по ключам, отличные значения записываем в результат.
for key in diff_list:
    if searcher(old_file_data, key) != searcher(new_file_data, key):
        result[key] = searcher(new_file_data, key)

#  Выгружаем результат в файл.
with open('result.json', 'w', encoding='utf-8') as result_file:
    json.dump(result, result_file, indent=4, ensure_ascii=False)
