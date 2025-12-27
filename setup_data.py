import pandas as pd
import os

# Đường dẫn đến file CSV bạn vừa tải
# Lưu ý: Python dùng dấu gạch chéo '/' hoặc 2 gạch ngược '\\'
raw_file_path = 'Data/raw/US_Accidents_March23.csv'
output_path = 'Data/processed/US_Accidents_Top20_Cities.csv'

def process_heavy_data():
    print("🚀 Đang bắt đầu đọc file 3GB... (Máy có thể hơi đơ xíu, bạn kiên nhẫn nhé!)")
    
    # Kiểm tra xem file có tồn tại không
    if not os.path.exists(raw_file_path):
        print(f"❌ Lỗi: Không tìm thấy file tại {raw_file_path}")
        return

    # Đọc file (chỉ lấy các cột quan trọng để nhẹ bớt)
    # Chúng ta sẽ dùng cột: City, Start_Time, Start_Lat, Start_Lng, Severity, Weather_Condition
    cols_to_use = ['ID', 'Severity', 'Start_Time', 'Start_Lat', 'Start_Lng', 'City', 'State', 'Weather_Condition']
    
    try:
        df = pd.read_csv(raw_file_path, usecols=cols_to_use)
        print(f"✅ Đã đọc xong! Tổng cộng có {len(df):,} dòng dữ liệu.")
    except Exception as e:
        print(f"❌ Lỗi khi đọc file: {e}")
        return

    # Lọc Top 20 thành phố có nhiều tai nạn nhất
    print("🔍 Đang lọc ra 20 thành phố nhiều tai nạn nhất...")
    top_cities = df['City'].value_counts().head(20).index
    df_filtered = df[df['City'].isin(top_cities)]
    
    print(f"📉 Dữ liệu sau khi lọc còn: {len(df_filtered):,} dòng.")
    
    # Tạo thư mục 'processed' nếu chưa có
    os.makedirs('Data/processed', exist_ok=True)
    
    # Lưu ra file mới
    print("💾 Đang lưu ra file mới...")
    df_filtered.to_csv(output_path, index=False)
    print(f"🎉 THÀNH CÔNG! File mới đã nằm tại: {output_path}")
    print("👉 Bạn hãy gửi file này cho nhóm nhé!")

if __name__ == "__main__":
    process_heavy_data()