#the solution does'n apply for all the cases but i am trying to find another solution
def minion_game(string):
    # your code goes here
    
    vowel_list = ['A','E','I','O','U']
    string_length = len(string)
    
    kevin_score = 0
    stuart_score = 0
    
    for i in range(string_length):
        
        if s[i] in vowel_list:
            kevin_score += string_length - i
        else:
            stuart_score += string_length - i
     
    if kevin_score > stuart_score:
        print "Kevin ", kevin_score
        
    elif stuart_score > kevin_score:
        print "Stuart", stuart_score
        
    else:
        print "Draw"
   
   
#given
if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
