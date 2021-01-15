def prime_number():
   first = int(input("give us the first number: "))
   last = int(input("give us the last number:  "))
   if first == 1 or first == 0:
      print("sorry! 1 or 0 is not a prime number. please don't mind. ")
   number = [2,3,5,7]
   if first < 10 and last > 10:
      for num in number:
         print(num)   
   for i in range(first,last):
      if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0:
         print(i)
#use prime_number() to run the code

width = 68.7
hight = 1.79
bmi = width/hight**2         
#print(bmi)

