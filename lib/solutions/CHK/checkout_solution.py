

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #raise NotImplementedError()
    import math
    from collections import Counter
    # Create list , assuming input string  will be having A,A,B,C,D,E format
    # Removed Split function as input is not comma separated
    lis=[]
    lis=skus
    totalVal=0
    idealVal=[]
    idealVal=['A','B','C','D']
    if not lis:
        return -1
    else:
        dir_sku=Counter(lis)
        print (dir_sku)
        for item, val in dir_sku.items():
            if item =='A':
                if val <3:
                    totalVal=(val*50)+totalVal
                else:
                    reminder=val%3
                    indVal=int(math.floor(val/3))
                    totalVal=((indVal*130)+(reminder*50))+totalVal
            elif item =='B':
                 if val < 2:
                     totalVal = (val * 30)+totalVal
                 else:
                     reminder = val % 2
                     indVal = int(math.floor(val / 2))
                     totalVal = ((indVal * 45) + (reminder * 30))+totalVal
            elif item == 'C':
                totalVal = (val * 20)+totalVal
            elif item == 'D':
                totalVal = (val * 15)+totalVal
            elif item not in idealVal:
                return -1

        #totalVal=A_sum+B_sum
        return totalVal


