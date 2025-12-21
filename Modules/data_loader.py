import pandas as pd
import os

def load_data(filepath):
    """
    Hàm này dùng để đọc file CSV đã lọc.
    Trả về: Một bảng dữ liệu (DataFrame)
    """
    print(f"🔄 Đang đọc dữ liệu từ: {filepath}...")
    
    # Kiểm tra xem file có tồn tại không
    if not os.path.exists(filepath):
        print(f"❌ LỖI: Không tìm thấy file tại {filepath}")
        return None
    
    try:
        # Đọc file CSV
        df = pd.read_csv(filepath)
        print(f"✅ Đã đọc xong! Tổng số dòng: {len(df)}")
        print("🔍 5 dòng đầu tiên:")
        print(df.head())
        return df
    except Exception as e:
        print(f"❌ Lỗi khi đọc file: {e}")
        return None