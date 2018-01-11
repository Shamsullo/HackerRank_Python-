def average(array):
    # your code goes here
  
    array = set(array)
    result = sum(array) / len(array)
    
    return result

    
    #given
    if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
    
    
