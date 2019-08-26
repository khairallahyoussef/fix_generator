def main():
    clientsOccurenceDic = {}
    productsOccurenceDic = {}
    orderTypesOccurenceDic = {}
    quantityPerProductDic = {}
    marginPerClientDic = {}
    securityTypeOccurenceDic = {}
    transactionVolumes = 0
    with open('fix_messages.txt') as fp:
        for line in fp:
            array = line.strip('\n').split('|')
            client = array[8][2:]
            product = array[2][3:]
            orderType = array[5][3:]
            quantity = int(array[4][3:])
            securityType = array[7][4:]
            price = float(array[9][3:])
            transactionVolumes = transactionVolumes + price
            transationType = int(array[3][3:])
            
            if client not in clientsOccurenceDic.keys() :
                clientsOccurenceDic[client] = 1
            else :
                clientsOccurenceDic[client] = clientsOccurenceDic[client] + 1
            
            if product not in productsOccurenceDic.keys() :
                productsOccurenceDic[product] = 1
            else :
                productsOccurenceDic[product] = productsOccurenceDic[product] + 1  
            
            if orderType not in orderTypesOccurenceDic.keys() :
                orderTypesOccurenceDic[orderType] = 1
            else :
                orderTypesOccurenceDic[orderType] = orderTypesOccurenceDic[orderType] + 1
                
            if securityType not in securityTypeOccurenceDic.keys() :
                securityTypeOccurenceDic[securityType] = 1
            else :
                securityTypeOccurenceDic[securityType] = securityTypeOccurenceDic[securityType] + 1   
                
            if product not in quantityPerProductDic.keys() :
                quantityPerProductDic[product] = quantity
            else :
                quantityPerProductDic[product] = quantityPerProductDic[product] + quantity        
            
            if client not in marginPerClientDic.keys() :
                if transationType == 1 :
                    marginPerClientDic[client] = -price
                elif transationType == 2 :
                    marginPerClientDic[client] = price
            else :
                if transationType == 1 :
                    marginPerClientDic[client] = marginPerClientDic[client] - price
                elif transationType == 2 :
                    marginPerClientDic[client] = marginPerClientDic[client] + price
                
    
    print("Messages amount per Client : ")
    for i in clientsOccurenceDic:
        print i, clientsOccurenceDic[i]
    
    print("\n")          
    print("List of traded products")
    for i in productsOccurenceDic:
        print i
    
    print("\n")
    mostTradedProducts = list()
    itemMaxValue = max(productsOccurenceDic.items(), key=lambda x: x[1])
    for key, value in productsOccurenceDic.items():
        if value == itemMaxValue[1]:
            mostTradedProducts.append(key)
    print("List of most traded product(s) : ")
    for i in mostTradedProducts :
        print i
    
    print("\n")
    print("Most popular order type product : " + max(orderTypesOccurenceDic.iterkeys(), key=lambda k: orderTypesOccurenceDic[k]))
    
    print("\n")
    print("Average ordered quantity per product : ")
    for i in productsOccurenceDic:
        print i, quantityPerProductDic[i] / productsOccurenceDic[i]
    
    
    print("\n")
    print("Security types occurence : ")
    for i in securityTypeOccurenceDic:
        print i, securityTypeOccurenceDic[i]
    
    print("\n")
    print("Margin per Client : ")
    for i in marginPerClientDic:
        print i, marginPerClientDic[i]
        
    print("\n")
    print("Transactions volume : " + str(transactionVolumes))    
    

if __name__ == "__main__":
    main()    