def tien_tiet_kiem(a, rates, months):
    # Lai suat kỳ hạn moi ky 6 thang:
    rates_6m = rates / 2

    # So chu ky (6 tháng/1 lan)
    cycles = months // 6

    # Tien lai sau moi chu ky 6 thang
    for i in range(1, cycles + 1):
        tien_lai = a * rates_6m
        a += tien_lai
        print(f"Chu kỳ {i:02}: {1 + (i - 1) * 6:02} - {i * 6:02}")
        print(f"Tien lai 6 thang: {tien_lai}")
        print(f"Tien lai + tien goc: {a}")
    # Lai suat khong ky han 6 thang còn lại:
    rem_mons = months % 6
    if rem_mons > 0:
        non_fixed_interest = a * (1.2 / 100) * (rem_mons / 12)
        a += non_fixed_interest
        print(f"Chu kỳ {cycles + 1:02}: {1 + cycles * 6:02} - {t:02}")
        print(f"Lãi suất không kỳ hạn: 0.012 trên năm")
        print(f"Tiền gốc: {a - non_fixed_interest:.2f}")
        print(f"Tiền lãi không kỳ hạn: {non_fixed_interest:.2f}")
        print(f"Tiền gốc + lãi không kỳ hạn: {a:.2f}\n")
    return a
# Dữ liệu đầu vào
y = 30000000
r = 0.072
print(f"Nhập tiền gửi: {y}")
print(f"Nhập lãi suất hàng năm: {r}")
print(f"Lãi suất hàng năm là: {r} %\n")

for t in [18, 20]:
    final_a = tien_tiet_kiem(y, r, t)
    print(f"Số tiền nhận được sau {t} tháng là: {final_a}\n")

