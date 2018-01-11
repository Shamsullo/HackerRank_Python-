
eglish_input = int(input())
english = set(map(int,input().split())) 

french_input = int(input())
french = set(map(int,input().split()))

print len(english - french)
