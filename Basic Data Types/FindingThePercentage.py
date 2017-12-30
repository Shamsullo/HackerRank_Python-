if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    
    for i in range(n):
        s = raw_input().split(" ")
        name = s[0]
        score1 = float(s[1])
        score2 = float(s[2])
        score3 = float(s[3])
        
        av_scores = (score1 + score2 + score3) / 3.0
        student_marks[name] = "%.2f" % av_scores
        
query_name = raw_input()
print (student_marks[query_name])
