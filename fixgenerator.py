import random

def main():
    list  = ['FUT','OP','CS']
    x = int(raw_input("Enter the number of FIX messages to be generated : "))
    f= open("fix_messages.txt","w+")
    for a in range(x):
        fix = '8=FIX.4.2|35=D|'
        
        product = '55=SYMBOL_' + str(random.randint(1,10)) + '|'
        buyOrSell = '54=' + str(random.randint(1,2)) + '|'
        quantity = '38=' + str(random.randint(1,100)) + '|'
        orderType = '40=' + str(random.randint(1,5)) + '|'
        orderTime = '59=' + str(random.randint(0,6)) + '|'
        securityType = '167=' + random.choice(list) + '|'
        clientId = '1=CLIENT_' + str(random.randint(1,5)) + '|'
        price = '44=' + str(round(random.uniform( 0, 1000 ), 2))
        fix = fix + product + buyOrSell + quantity + orderType + orderTime + securityType + clientId + price + '\n'
        f.write(fix)
    
    f.close()
    print("Fix messages generated")

if __name__ == "__main__":
    main()