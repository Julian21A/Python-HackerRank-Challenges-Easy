x=int(input())
for i in range(x):
    a,b = map(str,input().split())
    try: 
        int(b)
        try:
            int(a)
            try:
                print(int(a)//int(b))
            except ZeroDivisionError:
                print('Error Code: integer division or modulo by zero')
        except ValueError:
            print(f"Error Code: invalid literal for int() with base 10: '{a}'")
    except ValueError:
        print(f"Error Code: invalid literal for int() with base 10: '{b}'")
    