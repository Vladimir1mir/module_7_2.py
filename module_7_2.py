from pprint import pprint

def custom_write(file_name, strings):  # название файла для записи/список строк для записи
    strings_positions = {}
    position_number = 1
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        position_byte = file.tell()
        file.write(f'{i}\n')
        strings_positions[(position_number, position_byte)] = i
        position_number += 1
    file.close()
    return strings_positions


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
