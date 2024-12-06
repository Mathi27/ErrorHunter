def sum_of_digits(num):
    total = 0
    while num > 0:
 
        total += num % 10  
        num //= 10         
    return total

if __name__ == "__main__":
    num = int(input("Enter the Number: "))
    if num < 0:  
        num = -num
    result = sum_of_digits(num)
    print(f"Sum of digits: {result}")

 
        total += num % 10
         num = num//10  
 
 
        num = num // 10  
 
        num //= 10  
  
    return total

if __name__ == "__main__":
    num = int(input("Enter the Number : "))
     print(sum_of_digits(num))
 
    res=sum_of_digits(num)
    print(res)
 
    
 
  