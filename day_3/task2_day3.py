#Multiple if statement succession: Add to the rollercoster code the conditional for photo
costumer_height = int(input("What´s your height?"))
costumer_age = int(input("What´s your age?"))

if costumer_height >= 120:
    if costumer_age <= 12:
        bill= 5
        print("Child 120ticket value is:$5")
    elif costumer_age <= 18:
        bill= 7
        print("Teenage ticket value is :$7")
    else:
        bill= 12
        print("Adult ticket value is: $12")
    photo = input("Do you want to have a photo take? Type Y for yes and N for no.")
    if photo == "Y":
        bill += 3
    
    print(f"Your ticket value is : ${bill}")    
else:
    print("Sorry, you dont have the permitted height for riding this rollercoster")