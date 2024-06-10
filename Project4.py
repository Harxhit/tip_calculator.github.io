print("--------------------Welcome to the tip calculator!!--------------------")

bill = float(input("What was the bill? $"))
tip = int(input("How much tip you would like to give? 0 , 10 , 15 , 25?"))
people = int(input("How many people will spilt the bill?"))
percentage_of_tip = tip / 100
total_tip_amount = percentage_of_tip * bill
total_bill = total_tip_amount + bill 
bill_per_person = total_bill / people
final_amount = round(bill_per_person , 2)
print(f"Each person have to ${final_amount} ")
