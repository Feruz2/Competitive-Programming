def fizzBuzz(self, n: int) -> List[str]:
    i= 1
    li = []
    while (i<=n):
        if (i%3 == 0) and (i%5 ==0):
            li.append("FizzBuzz")    
        elif(i%3 == 0):
            li.append("Fizz") 
        elif(i%5 == 0):
            li.append("Buzz") 
        else:
            li.append(str(i))
        i += 1
    return li 