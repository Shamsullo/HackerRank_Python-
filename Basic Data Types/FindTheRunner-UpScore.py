if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    arr.sort()
    
    max = arr[len(arr) - 1]
    max2 = arr[0]
    
    for i in arr:
        if i < max:
            max2 = i
        
    print max2
