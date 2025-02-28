# Age group categorization
# classify a person's age group: Child (<13) , Teenager(13-19),Adult(20-59), Senior(60+)

age = int(input("Enter Your Age : \n"))

if age < 13:
    print("You are a Child")
elif age < 20:
    print("You are a Teenager")

elif age < 60:
    print("You are an Adult Person")
else:
    print("You are a senior person")


# price based on age if age < 19 price $ 8 for adult price $12 , and if day is wednesday then $2 discount

age = 23
day = "tuesday"

price = 12 if age >= 19 else 8

if day == "wednesday":
     price -= 2
print("Ticket price for you is $",price)


# weather activity suggestion 
# problem => Suggest an activity based on the weather (e.g Sunny- Go for walk , Rainy - read a book , snowy- build a snowman)

def weatherSuggetion(weather ):
     if weather == "sunny":
          print("Go for walk")
     elif weather == "rainy":
          print("Read a Book")
     else:
        print("Build a Snowman")   
          
  
weatherSuggetion("sunny")
weatherSuggetion("rainy")
weatherSuggetion("snowy")