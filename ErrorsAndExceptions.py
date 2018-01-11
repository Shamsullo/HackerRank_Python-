# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for i in range(t):
    a,b = raw_input().split()
    
    try:
        print(int(a) // int(b))
    except Exception as e:
        print ("Error Code: " + str(e))
