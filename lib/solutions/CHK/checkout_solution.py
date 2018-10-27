def module1(val,sku1,price1,sku2,price2,baseprice):
    import math
    retVal=0
    if val < sku2:
       if val < sku1: # if less than 3A
           retVal = (val * baseprice)
       else: #if value grater than 3A
           reminder = val % sku1
           indVal = int(math.floor(val / sku1))
           retVal = ((indVal * price1) + (reminder * baseprice))
    else:
        reminder = val % sku2
        # print("reminder--",reminder)
        if reminder > sku1:
            reminder3 = reminder % sku1
            indVal = int(math.floor(reminder / sku1))
            indVal5 = int(math.floor(val / sku2))
            retVal = (indVal * price1) + (reminder3 * baseprice)+ (indVal5 * price2)
        elif reminder == sku1:
            # print ("else")
            indVal5 = int(math.floor(val / sku2))
            retVal = price1 + (indVal5 * price2)
        elif reminder < sku1:
            indVal5 = int(math.floor(val / sku2))
            retVal = (reminder * baseprice) + (indVal5 * price2)

    return retVal




# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #raise NotImplementedError()
    import math
    from collections import Counter
    # Create list , assuming input string  will be having A,A,B,C,D,E format
    # Removed Split function as input is not comma separated
    # Checking null string
    lis=[]
    lis=skus
    totalVal=0
    idealVal=[]
    idealVal=['A','B','C','D','E','F','G','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    b_val=0
    BtotalVal=0
    FtotalVal=0
    if not lis:
        return 0
    elif len(lis)==0:
        return -1
    else:
        dir_sku=Counter(lis)
        # print (dir_sku)
        #print (dir_sku)
        for item, val in dir_sku.items():
            # For A section
            if item =='A':
                

            elif item =='B':
                 b_val=val
                 if b_val < 2:
                     BtotalVal = (b_val * 30) + totalVal
                 else:
                     reminder = b_val % 2
                     indVal = int(math.floor(b_val / 2))
                     BtotalVal = ((indVal * 45) + (reminder * 30)) + totalVal
            elif item == 'C':
                totalVal = (val * 20)+totalVal
            elif item == 'D':
                totalVal = (val * 15)+totalVal
            elif item =='E':
                BtotalVal=0
                if val < 2:
                    print(1)
                    totalVal = (val * 40) + totalVal
                    # totalVal = (b_val * 30) + totalVal
                    if (b_val < 2 and b_val >0):
                        totalVal = (b_val * 30) + totalVal
                    elif(b_val >0):
                        reminder = b_val % 2
                        indVal = int(math.floor(b_val / 2))
                        totalVal = ((indVal * 45) + (reminder * 30)) + totalVal
                    elif (b_val ==2):
                        totalVal = 45 + totalVal
                elif val==2:
                    print(2)
                    totalVal = (val * 40) + totalVal
                    # print (totalVal)
                    b_new_val = (b_val -1)
                    if (b_new_val < 2 and b_new_val >0):
                        #print (b_new_val)
                        totalVal = (b_new_val * 30) + totalVal
                    elif(b_new_val >2):
                        reminder = b_new_val % 2
                        indVal = int(math.floor(b_new_val / 2))
                        totalVal = ((indVal * 45) + (reminder * 30)) + totalVal
                    elif (b_new_val ==2):
                        totalVal = 45 + totalVal
                elif val > 2:
                    # print(3)
                    totalVal = (val * 40) + totalVal
                    indVal = int(math.floor(val / 2))
                    b_new_val = (b_val - indVal)
                    if (b_new_val < 2 and b_new_val >0):
                        totalVal = (b_new_val * 30) + totalVal
                    elif(b_new_val >2):
                        reminder = b_new_val % 2
                        indVal = int(math.floor(b_new_val / 2))
                        totalVal = ((indVal * 45) + (reminder * 30)) + totalVal
                    elif (b_new_val ==2):
                        totalVal = 45 + totalVal
            elif item == 'F':
                if (val<2 and val>0):
                    print(1)
                    BtotalVal=(10*val)
                elif val==2:
                     FtotalVal=(10*2)
                elif val > 2:
                    # indVal = int(math.floor(val/ 2))
                    FdivVal = (val/2)
                    reminder= val%2
                    # print(FdivVal)
                    # print(reminder)
                    #reminder = int(math.floor(reminder)) + 1
                    if reminder!=0:
                        FtotalVal=((FdivVal+1)*10)
                    else:
                        # print("else")
                        FtotalVal = ((FdivVal+1) * 10)
            elif item not in idealVal:
                return -1

        #totalVal=A_sum+B_sum
        return totalVal+BtotalVal+FtotalVal



# ret = checkout("FFFF")
# print (ret)

# 200+130+50

