import os
from Modules.data_loader import load_data

#Định nghĩa đường dẫn đến file dữ liệu đã lọc

data_path = 'Data/processed/US_Accidents_Top20_Cities.csv'

def main():
    print("🚀 CHƯƠNG TRÌNH PHÂN TÍCH TAI NẠN GIAO THÔNG MỸ - NHÓM 2 ")
    print("-" * 50)

    # 2. Gọi hàm đọc dữ liệu từ module data_loader
    df = load_data(data_path)

    if df is not None:
        print(f"\n🎉 Chạy thử thành công! Dữ liệu đã sẵn sàng để phân tích.")
    else:
        print("\n⚠️ Có lỗi xảy ra, vui lòng kiểm tra lại file data.")

if __name__ == "__main__":
    main()