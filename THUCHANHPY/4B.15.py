def check_cccd(cccd):
    return len(cccd) == 12 and cccd.isdigit()

print(check_cccd('079303003953'))