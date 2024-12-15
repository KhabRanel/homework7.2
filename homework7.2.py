def custom_write(file_name, strings):
    f = open(file_name, "a", encoding="utf-8")
    strings_positions = {}
    for i, x in enumerate(strings, 1):
        strings_positions[i, f.tell()] = x
        f.write(x + "\n")
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
