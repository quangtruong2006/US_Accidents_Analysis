def clean_data(df):
    print("Đang làm sạch dữ liệu...")
    
    # 1. Chuyển đổi kiểu dữ liệu thời gian
    df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
    df['End_Time'] = pd.to_datetime(df['End_Time'], errors='coerce')
    
    # 2. Loại bỏ các dòng bị thiếu thông tin cốt lõi
    df.dropna(subset=['Start_Time', 'City'], inplace=True)
    
    # 3. Xử lý giá trị thiếu cho nhiệt độ (điền bằng trung bình)
    if 'Temperature(F)' in df.columns:
        mean_temp = df['Temperature(F)'].mean()
        df['Temperature(F)'] = df['Temperature(F)'].fillna(mean_temp)
    
    # 4. Trích xuất thêm cột giờ để phân tích (tùy chọn)
    df['Hour'] = df['Start_Time'].dt.hour
    
    print("Làm sạch hoàn tất!")
    return df

# --- SAU ĐÓ GỌI HÀM ĐỂ THỰC THI ---
# Giả sử df_raw là biến chứa dữ liệu bạn vừa load thành công ở ảnh image_5862bb.png
df = clean_data(df) 

# Kiểm tra lại kết quả
print(df.info())
df.head()
