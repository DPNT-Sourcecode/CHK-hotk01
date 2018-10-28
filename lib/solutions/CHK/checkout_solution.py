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

def moodule2(val,baseCnt,basePrice,origVal,origBasePrice,OrigOfferPrice,OrigOfferCnt): #2f 1 b
    import math
    retVal=0
    retVal1 = 0
    #BtotalVal = 0
    if val < baseCnt:
        print(189)
        retVal = (val * basePrice)
        # totalVal = (b_val * 30) + totalVal
        if (origVal < OrigOfferCnt and origVal > 0):
            retVal1 = (origVal * origBasePrice)
        elif (origVal > 0):
            reminder = origVal % OrigOfferCnt
            indVal = int(math.floor(origVal / OrigOfferCnt))
            retVal1 = ((indVal * OrigOfferPrice) + (reminder * origBasePrice))
        elif (origVal == OrigOfferCnt):
            retVal1 = OrigOfferPrice
    elif val == baseCnt:
        print(2)
        retVal = (val * basePrice)
        # print (totalVal)
        b_new_val = (origVal - 1)
        if (b_new_val < OrigOfferCnt and b_new_val > 0):
            # print (b_new_val)
            retVal1 = (b_new_val * origBasePrice)
        elif (b_new_val > OrigOfferCnt):
            reminder = b_new_val % OrigOfferCnt
            indVal = int(math.floor(b_new_val / OrigOfferCnt))
            retVal1 = ((indVal * OrigOfferPrice) + (reminder * origBasePrice))
        elif (b_new_val == OrigOfferCnt):
            retVal1 = OrigOfferPrice
    elif val > baseCnt:
        # print(3)
        retVal = (val * basePrice)
        indVal = int(math.floor(val / baseCnt))
        b_new_val = (origVal - indVal)
        print ("OrigOfferCnt",OrigOfferCnt)
        if (b_new_val < OrigOfferCnt and b_new_val > 0):
            retVal1 = (b_new_val * origBasePrice)
        elif (b_new_val > OrigOfferCnt):
            reminder = b_new_val % OrigOfferCnt
            indVal = int(math.floor(b_new_val / OrigOfferCnt))
            retVal1= ((indVal * OrigOfferPrice) + (reminder * origBasePrice))
        elif (b_new_val == OrigOfferCnt):
            retVal1 = origBasePrice
    return retVal,retVal1

def module3(qty,price):
    return qty*price

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
    AtotalVal=0
    BtotalVal=0
    FtotalVal=0
    HtotalVal = 0
    VtotalVal = 0
    EtotalVal =0
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
                AtotalVal=module1(val,3,130,5,200,50)
                # print (AtotalVal)
            elif item =='H':
                HtotalVal = module1(val, 5, 45, 10, 80, 10)
            elif item == 'V':
                VtotalVal = module1(val, 2, 90, 3, 130, 50) #2V for 90, 3V for 130
            elif item =='B':
                 b_val=val
                 if b_val < 2:
                     BtotalVal = (b_val * 30) + totalVal
                 else:
                     reminder = b_val % 2
                     indVal = int(math.floor(b_val / 2))
                     BtotalVal = ((indVal * 45) + (reminder * 30)) + totalVal
            elif item =='E':
                BtotalVal=0
                EtotalVal ,BtotalVal=moodule2(val,2,40,b_val,30,45,1)

            elif item == 'F':
                if (val<2 and val>0):

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
            elif item  in ("W","T","G","C"):
                resttotalVal=module3(val,20)
                totalVal=totalVal+resttotalVal
            elif item in ("X", "L"):
                resttotalVal = module3(val, 90)
                totalVal = totalVal + resttotalVal
            elif item in ("Y"):
                resttotalVal = module3(val, 10)
                totalVal = totalVal + resttotalVal
            elif item in ("Z",):
                resttotalVal = module3(val, 50)
                totalVal = totalVal + resttotalVal
            elif item in ("S",):
                resttotalVal = module3(val, 30)
                totalVal = totalVal + resttotalVal
            elif item in ("M",):
                resttotalVal = module3(val, 15)
                totalVal = totalVal + resttotalVal
            elif item in ("I",):
                resttotalVal = module3(val, 35)
                totalVal = totalVal + resttotalVal
            elif item in ("J",):
                resttotalVal = module3(val, 60)
                totalVal = totalVal + resttotalVal
            elif item not in idealVal:
                return -1

            #totalVal=A_sum+B_sum
        return totalVal+BtotalVal+EtotalVal+FtotalVal+AtotalVal+VtotalVal+HtotalVal



ret = checkout("EBBBEEE")
print (ret)

# 200+130+50

