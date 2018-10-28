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
        b_new_val = (origVal - 1)
        retVal1 = module5(OrigOfferCnt, origVal, OrigOfferPrice, origBasePrice)
    elif val == baseCnt:
        print(2)
        retVal = (val * basePrice)
        print ("retVal",retVal)
        b_new_val = (origVal - 1)
        if b_new_val>0:
            retVal1=module5(OrigOfferCnt, b_new_val, OrigOfferPrice, origBasePrice)
        # print ("b_new_val",b_new_val)
        # print ("retVal1",retVal1)
        # print ("OrigOfferPrice",OrigOfferPrice)
        # print ("OrigOfferCnt", OrigOfferCnt)

    elif val > baseCnt:
        print(3)
        retVal = (val * basePrice)
        indVal = int(math.floor(val / baseCnt))
        print ("origVal",origVal)
        print ("origVal", indVal)
        b_new_val = (origVal - indVal)
        retVal1 = module5(OrigOfferCnt, b_new_val, OrigOfferPrice, origBasePrice)

    return retVal,retVal1

def module3(qty,price):
    return qty*price


def module4(qty,val,price):
    import math
    retVal=0
    if (val < qty and val > 0):
        retVal = (price * val)
    elif val == qty:
        retVal = (price * qty)
    elif val > qty:
        # indVal = int(math.floor(val/ 2))
        reminder = val % (qty+1)
        print("reminder",reminder)
        if reminder!=0:
            priceToPaid=(((qty+1)*reminder)-(qty*reminder))
            retVal=(priceToPaid*price)+(qty*price)
        else:
            reminder = val /(qty + 1)
            retVal = (reminder*qty * price)
    return retVal

def module5(qty,val,price,basePrice):
    import math
    retVal=0
    if val < qty:
        retVal = (val * basePrice)
    else:
        reminder = val % qty
        indVal = int(math.floor(val / qty))
        retVal = ((indVal * price) + (reminder * basePrice))
    return  retVal

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
    UtotalVal = 0
    KtotalVal = 0
    PtotalVal = 0
    q_val = 0
    QtotalVal = 0
    RtotalVal=0
    MtotalVal=0
    NtotalVal=0
    StotalVal = 0
    TtotalVal = 0
    XtotalVal = 0
    YtotalVal = 0
    ZtotalVal = 0
    m_val=0
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
                 BtotalVal=module5(2,b_val,45,30)
            elif item =='E':
                BtotalVal=0
                EtotalVal ,BtotalVal=moodule2(val,2,40,b_val,30,45,2)
                print("EtotalVal",EtotalVal)
                print("BtotalVal", BtotalVal)
            elif item == "F":
                FtotalVal=module4(2,val,10)
            elif item =='K':
                 KtotalVal=module5(2,val,150,80)
            elif item =='P':
                 PtotalVal=module5(5,val,200,50)
            elif item == 'Q':
                q_val=val
                QtotalVal = module5(3, q_val, 80, 30)
            elif item =='R':
                QtotalVal=0
                RtotalVal ,QtotalVal=moodule2(val,3,50,q_val,30,80,3)
            elif item == "U":
                UtotalVal=module4(3,val,40)
            elif item  in ("W","G","C"):
                resttotalVal=module3(val,20)
                totalVal=totalVal+resttotalVal
            elif item in ("L"):
                resttotalVal = module3(val, 90)
                totalVal = totalVal + resttotalVal
            elif item in ("O"):
                resttotalVal = module3(val, 10)
                totalVal = totalVal + resttotalVal
            elif item in ("S","T","X","Y","Z"):
                # resttotalVal = module3(val, 30)
                if item=='S':
                    StotalVal = module5(3, val, 45, 20)
                elif item == 'T':
                    TtotalVal = module5(3, val, 45, 20)
                elif item == 'X':
                    XtotalVal = module5(3, val, 45, 17)
                elif item == 'Y':
                    YtotalVal = module5(3, val, 45, 20)
                elif item == 'Z':
                    ZtotalVal = module5(3, val, 45, 21)
                # totalVal = totalVal + resttotalVal
                # if item in ("Z",):
                # resttotalVal = module3(val, 50)
                # totalVal = totalVal + resttotalVal
            elif item in ("D"):
                resttotalVal = module3(val, 15)
                totalVal = totalVal + resttotalVal
            elif item in ("I",):
                resttotalVal = module3(val, 35)
                totalVal = totalVal + resttotalVal
            elif item in ("J",):
                resttotalVal = module3(val, 60)
                totalVal = totalVal + resttotalVal
            elif item in ("M"):
                m_val = val
                MtotalVal = module3(m_val,15)
            elif item in ("N"):
                MtotalVal=0
                NtotalVal = module3(val, 40)
                print ("NtotalVal",NtotalVal)
                if val>=3:
                    print("if")
                    qtyReduce=m_val-(val/3)
                    if qtyReduce>0:
                        MtotalVal=module3(qtyReduce,15)
                else:
                    MtotalVal =module3(m_val,15)
                # print("MtotalVal",MtotalVal)
                # print("NtotalVal", NtotalVal)
            elif item not in idealVal:
                return -1

            #totalVal=A_sum+B_sum
        return totalVal+BtotalVal+EtotalVal+FtotalVal+AtotalVal+VtotalVal+HtotalVal+UtotalVal+KtotalVal+PtotalVal+QtotalVal+RtotalVal+MtotalVal+NtotalVal+StotalVal+TtotalVal+XtotalVal+YtotalVal+ZtotalVal



ret = checkout("XXXYYYY")
print (ret)

# 200+130+50

# 150+60=210

