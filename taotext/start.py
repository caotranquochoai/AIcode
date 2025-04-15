import google.generativeai as genai
import pandas as pd
import os

# Cấu hình API key (thay YOUR_API_KEY bằng key của bạn)
API_KEY = "Nhập_API_Key"
genai.configure(api_key=API_KEY)

# Hàm tạo cụm từ/câu tiếng Anh ngẫu nhiên
def generate_random_phrase():
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = "Tạo 1 nhiều cụm từ hoặc câu tiếng anh có nghĩa khoảng 100 cụm từ, chỉ trả về cụm từ không trả về bất cứ mô tả nào khác"
    response = model.generate_content(prompt)
    return response.text.strip()

# Hàm lưu vào file TXT
def save_to_txt(phrases, filename="output_phrases.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for phrase in phrases:
            f.write(phrase + "\n")
    print(f"Saved to {filename}")

# Hàm lưu vào file Excel
def save_to_excel(phrases, filename="output_phrases.xlsx"):
    df = pd.DataFrame(phrases, columns=["Phrase"])
    df.to_excel(filename, index=False)
    print(f"Saved to {filename}")

# Main
def main():
    # Số lượng cụm từ muốn tạo
    num_phrases = 1  # Có thể yêu cầu nhiều lần tuy nhiên chỉnh prompt sẽ tiết kiệm lượt gọi API hơn
    phrases = []

    # Tạo các cụm từ
    print("Generating phrases...")
    for _ in range(num_phrases):
        phrase = generate_random_phrase()
        phrases.append(phrase)
        print(f"Generated: {phrase}")

    # Lưu vào file
    output_format = input("Save as (txt/excel): ").lower()
    if output_format == "txt":
        save_to_txt(phrases)
    elif output_format == "excel":
        save_to_excel(phrases)
    else:
        print("Invalid format! Saving as TXT by default.")
        save_to_txt(phrases)

if __name__ == "__main__":
    main()