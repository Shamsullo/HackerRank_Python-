if __name__ == '__main__':
    N = int(raw_input())
    l = []
for i in range(0, N):
    cmd = str(raw_input())
    split_cmd = cmd.split(' ')
    
    if split_cmd[0] == "insert":
        l.insert(int(split_cmd[1]), int(split_cmd[2]))
        
    elif split_cmd[0] == "print":
        print l
        
    elif split_cmd[0] == "remove":
        l.remove(int(split_cmd[1]))
        
    elif split_cmd[0] == "append":
        l.append(int(split_cmd[1]))
        
    elif split_cmd[0] == "sort":
        l.sort()
        
    elif split_cmd[0] == "pop":
        l.pop()
        
    elif split_cmd[0] == "reverse":
        l.reverse()
      
        


