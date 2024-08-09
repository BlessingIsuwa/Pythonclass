ATM_CARD_NAME = "blessing isuwa"
password = 4545
Amount = "N50,000"

x = input("ATM card detail: ")
if x == ATM_CARD_NAME:
    y = int (input("Enter password: "))
    if y == password:
        print("your amount is ", Amount)
    else:
        print("wrong password")
else:
    print("Enter a valid ATM CARD")
    
