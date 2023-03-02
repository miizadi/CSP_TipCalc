#This is where the variables are defined, items equals 1 from the start and builds up as the user inputs more number. 
#the total money also starts at 0 and adds up as the user adds prices up. 
items = 1
total_money = 0
prices = []
question = int(input("so what is the price of the item?!!!(type 0 when you want to stop!): "))
total_money = total_money + question
prices.append(question)
#this is where the while loop starts where the user can add as many items and prices as they want.
while question != 0:
  question = int(input("anything else: "))
  total_money = total_money + question
  if question != 0:
    prices.append(question)
    items = items + 1
tax = total_money * 0.10
precentage = int(input("so like what precentage were you trying to tip tonight?!: "))
decimal = precentage / 100
tipamount = total_money * decimal
thetotaltotalmoney = total_money + tipamount + tax
#this is the function/procedure that allows the program to print out the all the prices that the user has inputed.
def reciepe():
  print("receipt")
  for z in range(len(prices)):
    print("$", prices[z])
#this is when the program prints all the products and sums of the math.
  print("subtotal: $", total_money)
  print("The amount of items that you have ordered: ", items)
  print("your tax totals to: $", tax)
  print("The total amount you tipped was: $", tipamount)
  print("The total amount of money you spent was: $", thetotaltotalmoney)
reciepe() 