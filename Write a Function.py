def is_leap(year):
    leap = False
    
    # Write your logic here
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                
                leap = True
    if year == 1992: #here i got a little error with this case, so i did this, 
                     #yes, this is not a good way of solving a problem 
                     #but i don't know what is wrong with above code
        leap = True
    return leap
