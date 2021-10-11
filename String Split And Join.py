def split_and_join(line):
    texto=line.split()
    return '-'.join(texto)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)