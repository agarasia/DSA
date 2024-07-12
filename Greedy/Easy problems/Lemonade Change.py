def canPay(bills):
    five, ten = 0, 0

    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:
            if five and ten:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    
    return True
# T(n) = O(n)
# S(n) = O(1)

bills = [5, 5, 5, 10, 20]

print(canPay(bills))