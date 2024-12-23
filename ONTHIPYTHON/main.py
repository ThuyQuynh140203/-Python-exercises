def taxi_bill(km):
    if km <= 0.3:
        return km * 20000
    elif km <= 3:
        return  0.3 * 20000 + (km - 0.3) * 18600
    elif km <= 11:
        return 0.3 * 20000 + 2.7 * 18600 + (km - 3) * 14200
    elif km <= 20:
        return 0.3 * 20000 + 2.7 * 18600 + 8 * 14200 + (km - 11) * 13000
    elif km <= 30:
        return 0.3 * 20000 + 2.7 * 18600 + 8 * 14200 + 9 * 13000 + (km - 20) * 12000
    else:
        return 0.3 * 20000 + 2.7 * 18600 + 8 * 14200 + 9 * 13000 + 10 * 12000 + (km - 30) * 11000

def taxi_bill_full(km):
    taxi_total = taxi_bill(km)
    if km > 120:
        taxi_total *= 0.9
    taxi_total *= 1.05
    return taxi_total

print(taxi_bill_full(20))