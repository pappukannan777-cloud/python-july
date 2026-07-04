
#make a function with name total_cal

# pass biill annd tip percentage as arguments

#find the total amount to be paid

# total = bill_amount*(1 + 0.01*tip_perc)

# total = round(total,2)

#print the amount

#call the function with bill amount and tip percentage as arguments
def total_cal (bill,tip_perc):
    total = bill*(1 + 0.01*tip_perc)
    total = round(total,2)
    print("your total bill is:",total)
    
total_cal (150,20)