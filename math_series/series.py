# Chat gpt assisted

def fibonacci(n):  
    """Establishes first 2 numbers in the fibonacci sequence, then for any (n) higher adds the value 1 less of the current postion to 2 less of the current postion"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def lucas(n):
     """The same as fibonacci, beginning numbers are different"""
     if n == 1:
        return 2
     elif n == 2:
        return 1
     else:
        return lucas(n - 1) + lucas(n - 2)
     
# ChatGPT was a huge help on this part
    
def sum_series(n, first=0, second=1):
      if n == 0:
        return first
      elif n == 1:
        return second
      else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)