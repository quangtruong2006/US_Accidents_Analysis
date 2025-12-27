import os
import pandas as pd
from Modules.data_loader import load_data
from Modules.cleaner import clean_data
from Modules.analysis import analyze_accidents
from Modules.visualizer import plot_charts
from Modules.map_visualizer import plot_heatmap 

data_path = 'Data/processed/US_Accidents_Top20_Cities.csv'

def main():
    print("🚀 CHƯƠNG TRÌNH PHÂN TÍCH TAI NẠN GIAO THÔNG MỸ - NHÓM 2")
    print("-" * 50)
    df = load_data(data_path)
    if df is not None:
        print(f"✅ Đã đọc xong! Tổng số dòng: {len(df)}")
        df_clean = clean_data(df)
        stats = analyze_accidents(df_clean)
        plot_charts(stats)
        plot_heatmap(df_clean)
        print("-" * 50)
        print(f"🎉 Quy trình chạy thử hoàn tất! Dữ liệu đã sẵn sàng.")
    else:
        print("\n⚠️ Có lỗi xảy ra, vui lòng kiểm tra lại file data.")

if __name__ == "__main__":
    main()