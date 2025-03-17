item1 = 100
item2 = 150
item3 = 130
budget = 300
cogs = (item1+item2+item3)
difference = (cogs-budget)
print ("total cost", cogs, " pound ")
print ("difference between cost& budget",difference , "pound ")
if cogs > budget:  
    print("Cost exceeds the budget")
elif cogs < budget:  
    print("Cost is within the budget")
else: 
    print("Cost matches the budget exactly")
