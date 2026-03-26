#Ejercicio: 'Write some code using modulo operator and conditional checks in Python to check if 
#the number in the input area is odd or even.
#If it´s odd print out the world "Odd" otherwise print out the word "Even"'

number= int(input("Ingresar número: "))

if number% 2 == 0:
    print("Even")

else : 
    print("Odd")

#Nested con if/else/elif statements :  Create a code that have conditions for entering to a rollercoster. 
# 1- Check height equal/major to 120cm
# 2-Age and pricing: a- <=12 years : $5/ b- 12 to 18 years: $7/ c- >18 years: $12          

costumer_height = int(input("What´s your height?"))
costumer_age = int(input("What´s your age?"))

if costumer_height >= 120:
    if costumer_age <= 12:
        print("Your ticket value is:$5")
    elif costumer_age <= 12:
        print("Your ticket value is:$7")
    else:
        print("Your ticket value is: $12")
else:
    print("Sorry, you dont have the permitted height to riding this rollercoster")

 #Multiple if statement succession: Add to the rollercoster code the conditional for photo

                    

