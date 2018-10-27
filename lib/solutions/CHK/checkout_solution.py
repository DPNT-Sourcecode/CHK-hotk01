

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #raise NotImplementedError()
    import math
    from collections import Counter
    # Create list , assuming input string  will be having A,A,B,C,D,E format
    lis=[]
    lis=skus.split(",")
    totalVal=0
    if not lis:
        return -1
    else:
        dir_sku=Counter(lis)
        for item, val in dir_sku.items():
            if item =='A':
                if val <3:
                    totalVal=val*50
                else:
                    reminder=val%3
                    indVal=int(math.floor(val/3))
                    totalVal=(indVal*130)+(reminder*50)
            elif item =='B':
                 if val < 2:
                     totalVal = val * 30
                 else:
                     reminder = val % 2
                     indVal = int(math.floor(val / 2))
                     totalVal = (indVal * 45) + (reminder * 30)
            elif item == 'C':
                totalVal = val * 20
            elif item == 'D':
                totalVal = val * 15


        #totalVal=A_sum+B_sum
        return totalVal


sku =('B,B,B,C,D')
ret=checkout(sku)
print(ret)
