import pandas as pd

def clean_data(df):
    print("\n" + "="*20 + " QUY TRÌNH LÀM SẠCH DỮ LIỆU " + "="*20)

    # 1. Thống kê giá trị thiếu ban đầu
    print("\nThống kê giá trị thiếu ban đầu:")
    print(df.isnull().sum())

    # 2. Danh sách cột ban đầu
    print("\nDanh sách cột ban đầu:")
    print(df.columns.tolist())

    # 3. Kiểu dữ liệu TRƯỚC xử lý
    print("\n[TRƯỚC XỬ LÝ] Kiểu dữ liệu ban đầu:")
    print(df.dtypes)

    # 4. Loại bỏ các cột thừa
    cols_to_drop = ['ID', 'End_Time', 'Airport_Code', 'Number']
    existing_drop_cols = [c for c in cols_to_drop if c in df.columns]
    df = df.drop(columns=existing_drop_cols, errors='ignore')
    print(f"\nĐã xóa các cột thừa: {existing_drop_cols}")

    # 5. Loại bỏ các cột có tỉ lệ missing cao (>40%)
    threshold = len(df) * 0.4
    df = df.dropna(thresh=threshold, axis=1)
    print(f"Đã lọc các cột có tỉ lệ giá trị thiếu cao (ngưỡng {threshold:.0f} dòng).")

    # 6. Loại bỏ các dòng thiếu thông tin quan trọng
    cols_to_check = [c for c in ['Start_Time', 'Severity', 'City'] if c in df.columns]
    df = df.dropna(subset=cols_to_check)
    print(f"Đã loại bỏ các dòng thiếu thông tin tại: {cols_to_check}")

    # 7. Chuẩn hóa Start_Time sang datetime (IN TRƯỚC & SAU)
    if 'Start_Time' in df.columns:
        print("\n[TRƯỚC XỬ LÝ] Kiểu dữ liệu các cột:")
        print(df[['Severity', 'Start_Time', 'Start_Lat', 'City', 'State', 'Weather_Condition']].dtypes)

        df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
        df['Hour'] = df['Start_Time'].dt.hour

        print("\n[SAU XỬ LÝ] Kiểu dữ liệu các cột:")
        print(df[['Severity', 'Start_Time', 'Start_Lat', 'City', 'State', 'Weather_Condition', 'Hour']].dtypes)

    # 8. Điền missing cho Temperature nếu có
    if 'Temperature(F)' in df.columns:
        mean_temp = df['Temperature(F)'].mean()
        df['Temperature(F)'] = df['Temperature(F)'].fillna(mean_temp)

    print(f"\nLÀM SẠCH HOÀN TẤT! Dữ liệu còn lại: {len(df)} dòng.")
    print("="*60 + "\n")

    return df
