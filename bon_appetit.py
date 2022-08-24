def bonAppetit(bill, k, b):
    annaWont = bill[k]
    bill.remove(annaWont)
    sharedCost = sum(x for x in bill)
    annaBill = int(sharedCost / 2)
    annaRest = b - annaBill
    if (annaRest == 0):
        print("Bon Appetit")
    else:
        print(abs(annaRest))

bonAppetit([3, 10, 2, 9], 1, 12)