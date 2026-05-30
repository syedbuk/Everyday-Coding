


glass1 = "milk"
glass2 = "water"
glass1,glass2 = glass2,glass1
print(glass1)
print(glass2)


print("Band Name Generator")
city= input("what is the name of the city you grew up in? ")
pet= input("what is the name of your pet? ")
print("Your band name could be " + city + " " + pet)





print("Welcome to Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
percentage=int(input("How much tip would you like to give? 10, 12, or 15?"))
tip_amount = total_bill * (percentage / 100)
bill_split= int(input("How many people to split the bill? "))
person_pay = (total_bill + tip_amount) / bill_split
print(f"Each person should pay: ${person_pay:.2f}")



