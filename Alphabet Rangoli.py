import string
alfabeto=string.ascii_letters
def print_rangoli(size):
        # your code goes here
    filas = []
    for row in range(size):
        to_print = "-".join(alfabeto[row:size])
        filas.append(to_print[::-1] + to_print[1:])
    width = len(filas[0])
    
    for row in range(size-1, 0, -1):
        print(filas[row].center(width, '-'))
        
    for row in range(size):
        print(filas[row].center(width, '-'))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)