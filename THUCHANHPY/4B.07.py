# Chuong trinh tinh tien dien
def tien_dien(kwh):
    if kwh <= 50:
        return kwh * 1678
    elif kwh <= 100:
        return 50 * 1678 + (kwh - 50) * 1734
    elif kwh <= 200:
        return 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
    elif kwh <= 300:
        return 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536
    elif kwh <= 400:
        return 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (kwh - 300) * 2834
    else:
        return 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (kwh - 400) * 2927

def tien_dien_full(kwh):
    total = tien_dien(kwh)
    tax = total * 0.1
    return total + tax
print(tien_dien_full(500))