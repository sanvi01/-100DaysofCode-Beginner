print("welcome to tip calculator!")
bill = float(input("what is the total bill?"))
tip = int(input("how much percent of tip you wanna give?10, 12 or 15?"))
people = int(input("how many people are splitting the bill?"))
total_tip = tip/100 * bill
total_bill = bill + total_tip
#amnt = round(total_bill/people, 2)
amnt = "{:.2f}".format(total_bill/people)
print(f"amount payable by per person is {amnt}")
