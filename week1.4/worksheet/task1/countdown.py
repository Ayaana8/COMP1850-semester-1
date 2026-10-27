
def countdown(number): 
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 

    if number ==0:
        print(0)
    else:
        print(number) 
        countdown(number-1) 

