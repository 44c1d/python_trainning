#for loop and range () function

# #The Gauss chanllenge
total = 0 

for number in range (1, 101):
    total += number
    print(total)

#FizzBuzz Game

for number in range (1,101):
    if number % 3== 0 and number %5 == 0:
        print("FizzBuzz")
    elif number %3 == 0 :
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
