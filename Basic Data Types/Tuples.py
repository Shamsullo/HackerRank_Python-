if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
   # from _builtins_ import *
    a = []
    
    for i in range(0, len(integer_list)):
        a.append(int(integer_list[i]))
        
    temp = tuple(a)
    
    print hash(temp)
