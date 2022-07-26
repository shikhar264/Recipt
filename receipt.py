decp=[]
price = []
for i in range(1, 5):
    item_name = input(f"Input the name of item {i} : ")
    decp.append(item_name)
    item_price = int(input(f"Input the price of item {i}: "))
    price.append(item_price)
    
bank_card_num = int(input("Please enter your bank card number : "))
cash = float(input("what amount of cash would you like to give : "))
print("                  SHOP NAME                    ")
print("       Address: Loan Ipsum,23-10        ")
print("      ************************************   ")
print("                 CASH RECIPT                 ")
print("      ************************************   ")
for i in range(0, 4):
    print(decp[i], end='\r')
    print(f"\t\t\t\t{price[i]}")
for i in range(len(price) - 1): 
    price[i+1] += price[i]
print(f"     TOTAL                                 {price[i+1]}")
change = cash - price[i+1]
if change < 0:
    change = abs(change)
    change = round(change, 2)
print(f"     Cash                                    {cash}       ")
print(f"     Change                                {change}   ")
print("      ************************************   ")
print(f"     Bank card                            {bank_card_num}     ")
print("     Approval Code                       #123455       ")
print("      ************************************   ")
print("                  THANK YOU                   ")
print("              ||||| |||| ||||||| | | |||||                    ")



      




