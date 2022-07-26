decp = []
for i in range(1, 5):
    a = input(f"Input the name of description {i} : ")
    decp.append(a)
    i += 1
price = []
for j in range(1, 5):
    b = float(input(f"Input the price of description {j} : "))
    price.append(b)
    j += 1
bank_card_num = int(input("Please enter your bank card number : "))
cash = float(input("what amount of cash would you like to give : "))
print("                  SHOP NAME                    ")
print("       Address: Loan Ipsum,23-10        ")
print("      ************************************   ")
print("                 CASH RECIPT                 ")
print("      ************************************   ")
for i in range(len(decp)):
   for j in range(len(price)):
        if i == j:
            print(f"\t{decp[i]}                             {price[j]}")
print("      ************************************   ")
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



      




