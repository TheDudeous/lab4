def filter_lines(filename, predicate):
    """
    Генератор, который построчно читает файл и возвращает
    только строки, удовлетворяющие условию predicate.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if predicate(line):
                yield line


# Использование
if __name__ == '__main__':
    # Создадим тестовый файл
    with open('data.txt', 'w', encoding='utf-8') as f:
        f.write("apple 100\nbanana 50\ncherry 200\ndate 30\nelderberry 150\n")

    # Фильтр: строки, где число больше 80
    for line in filter_lines('data.txt', lambda s: int(s.split()[1]) > 80):
        print(line)