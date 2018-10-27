def module1(val,sku1,cnt1,sku2,cnt2,baseprice):
    import math
    if val < sku1:
       if val < sku2:
           totalVal = (val * baseprice) + totalVal
        else:
            reminder = val % 3
            indVal = int(math.floor(val / 3))
            totalVal = ((indVal * 130) + (reminder * baseprice)) + totalVal
        else:
            reminder = val % 5
            # print("reminder--",reminder)
            if reminder > 3:
                reminder3 = reminder % 3
                indVal = int(math.floor(reminder / 3))
                indVal5 = int(math.floor(val / 5))
                totalVal = (indVal * 130) + (reminder3 * baseprice) + totalVal + (indVal5 * 200)
            elif reminder == 3:
                # print ("else")
                indVal5 = int(math.floor(val / 5))
                totalVal = 130 + totalVal + (indVal5 * 200)
            elif reminder < 3:
                indVal5 = int(math.floor(val / 5))
                totalVal = (reminder * baseprice) + totalVal + (indVal5 * 200)



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #raise NotImplementedError()

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
                if val<5:
                    if val <3:
                        totalVal=(val*50)+totalVal
                    else:
                        reminder=val%3
                        indVal=int(math.floor(val/3))
                        totalVal=((indVal*130)+(reminder*50))+totalVal
                else:
                    reminder=val%5
                    # print("reminder--",reminder)
                    if reminder>3:
                        reminder3 = reminder % 3
                        indVal  = int(math.floor(reminder / 3))
                        indVal5 = int(math.floor(val / 5))
                        totalVal = (indVal * 130) + (reminder3 * 50) + totalVal+(indVal5*200)
                    elif reminder==3:
                        # print ("else")
                        indVal5 = int(math.floor(val / 5))
                        totalVal = 130 + totalVal + (indVal5 * 200)
                    elif reminder<3:
                        indVal5 = int(math.floor(val / 5))
                        totalVal=(reminder * 50) + totalVal + (indVal5 * 200)

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

