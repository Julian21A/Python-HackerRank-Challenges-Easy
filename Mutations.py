def mutate_string(string, position, character):
    x=string[:position]+character+string[position+1:]
    
    return x

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)