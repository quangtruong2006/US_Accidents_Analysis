import pandas as pd

def clean_data(df):
    print("Đang làm sạch dữ liệu...")
    
    # 1. Chuyển đổi Start_Time (Cột này bắt buộc phải có để phân tích)
    if 'Start_Time' in df.columns:
        df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
        # Tạo cột Hour luôn để dùng cho phân tích sau này
        df['Hour'] = df['Start_Time'].dt.hour
    else:
        print("❌ Lỗi nghiêm trọng: Không tìm thấy cột 'Start_Time'")
        return df

    # 2. Chuyển đổi End_Time (Kiểm tra nếu có thì mới làm)
    if 'End_Time' in df.columns:
        df['End_Time'] = pd.to_datetime(df['End_Time'], errors='coerce')
    else:
        print("⚠️ Cảnh báo: Không có cột 'End_Time', bỏ qua bước này.")
    
    # 3. Loại bỏ các dòng bị thiếu thông tin cốt lõi (Start_Time, City)
    # Chỉ lọc trên các cột thực sự tồn tại
    cols_to_check = [c for c in ['Start_Time', 'City'] if c in df.columns]
    df.dropna(subset=cols_to_check, inplace=True)
    
    # 4. Xử lý giá trị thiếu cho nhiệt độ (nếu có)
    if 'Temperature(F)' in df.columns:
        mean_temp = df['Temperature(F)'].mean()
        df['Temperature(F)'] = df['Temperature(F)'].fillna(mean_temp)
    
    print(f"Làm sạch hoàn tất! Dữ liệu còn lại: {len(df)} dòng.")
    return df