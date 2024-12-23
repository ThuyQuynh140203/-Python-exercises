def calculate_bmi(weight, height):
    height_m = height / 100
    # tinh bmi
    bmi = weight / height_m ** 2
    return round(bmi, 2)
def evaluate_bmi(bmi, gender, age):
    if(bmi < 18.5):
        return "Thieu can"
    if(18.5 <= bmi <= 24.9):
        return "Binh thuong"
    elif(24.9 <= bmi <= 29.9):
        return "Thua can"
    else:
        return "Beo phi"

def suggest_bmi_action(bmi, gender, age):
    # Gợi ý cải thiện chỉ số BMI dựa trên đánh giá
    evaluation = evaluate_bmi(bmi, gender, age)
    if evaluation == "Thiếu cân":
        return "Bạn nên tăng cường chế độ ăn giàu dinh dưỡng và duy trì tập luyện."
    elif evaluation == "Bình thường":
        return "Bạn có chỉ số BMI bình thường, hãy duy trì chế độ ăn uống và tập luyện hiện tại."
    elif evaluation == "Thừa cân":
        return "Bạn nên điều chỉnh chế độ ăn và tăng cường hoạt động thể chất."
    else:
        return "Bạn cần cân nhắc chế độ giảm cân và tập luyện thường xuyên."

# Nhập dữ liệu từ người dùng
weight = float(input("Nhập cân nặng của bạn (kg): "))
height = float(input("Nhập chiều cao của bạn (cm): "))
gender = input("Nhập giới tính của bạn (nam/nữ): ").lower()
age = int(input("Nhập tuổi của bạn: "))

# Tính và đánh giá chỉ số BMI
bmi = calculate_bmi(weight, height)
evaluation = evaluate_bmi(bmi, gender, age)
suggestion = suggest_bmi_action(bmi, gender, age)

# Xuất kết quả
print(f"Chỉ số BMI của bạn là: {bmi}")
print(f"Đánh giá: {evaluation}")
print(f"Gợi ý: {suggestion}")