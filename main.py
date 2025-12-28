import os
from Modules.data_loader import load_data
from Modules.cleaner import clean_data
from Modules.analysis import analyze_accidents, save_report  # Import thêm save_report
from Modules.visualizer import draw_static_charts
from Modules.map_visualizer import plot_heatmap

def main():
    print("🚀 CHƯƠNG TRÌNH PHÂN TÍCH TAI NẠN GIAO THÔNG MỸ - NHÓM 2")
    print("-" * 60)

    # Tạo thư mục Outputs nếu chưa có
    os.makedirs("Outputs", exist_ok=True)

    # 1. Đọc dữ liệu
    file_path = "Data/processed/US_Accidents_Top20_Cities.csv"
    try:
        df = load_data(file_path)
    except FileNotFoundError:
        print(f"❌ Lỗi: Không tìm thấy file dữ liệu tại {file_path}")
        return

    # 2. Làm sạch dữ liệu
    df_clean = clean_data(df)

    # 3. Phân tích thống kê & LƯU BÁO CÁO (Phần bạn cần)
    print("📊 Đang tiến hành phân tích và lưu báo cáo...")
    stats = analyze_accidents(df_clean)
    
    save_report(stats, "Outputs/bao_cao_thong_ke.txt") 

    # 4. Vẽ biểu đồ tĩnh
    print("🎨 Đang vẽ biểu đồ tĩnh...")
    draw_static_charts(df_clean, "Outputs")

    # 5. Vẽ bản đồ nhiệt
    print("🗺️ Đang vẽ bản đồ nhiệt...")
    plot_heatmap(df_clean, "Outputs/heatmap.html")

    print("-" * 60)
    print("🎉 QUY TRÌNH HOÀN TẤT! Dữ liệu đã sẵn sàng.")
    print("👉 Kiểm tra thư mục 'Outputs/' để xem:")
    print("   1. bao_cao_thong_ke.txt (Số liệu chi tiết)")
    print("   2. Các file ảnh biểu đồ (.png)")
    print("   3. heatmap.html (Bản đồ tương tác)")

if __name__ == "__main__":
    main()