import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plot_charts(df, out_dir="Outputs"):
    print("Đang vẽ biểu đồ thống kê...")

    # 1. Tạo thư mục Outputs nếu chưa có
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # 2. Xử lý dữ liệu phụ trợ (Tạo cột CityState để nhóm)
    # Chúng ta cần đảm bảo cột Year và CityState tồn tại để vẽ
    if 'Start_Time' in df.columns:
        df['Year'] = pd.to_datetime(df['Start_Time'], errors='coerce').dt.year
    
    if 'City' in df.columns and 'State' in df.columns:
        df["CityState"] = df["City"].astype(str).str.strip() + ", " + df["State"].astype(str).str.strip()
    else:
        print("Thiếu cột City hoặc State, bỏ qua bước vẽ biểu đồ địa lý.")
        return

    # 3. Vẽ biểu đồ 1: Top 10 địa điểm nhiều tai nạn nhất
    try:
        top_rank = df["CityState"].value_counts().head(10).reset_index()
        top_rank.columns = ["CityState", "Accidents"]
        
        plt.figure(figsize=(12, 6))
        sns.barplot(data=top_rank, x="Accidents", y="CityState", palette="viridis")
        plt.title("Top 10 địa điểm xảy ra tai nạn nhiều nhất")
        plt.xlabel("Số vụ tai nạn")
        plt.ylabel("Địa điểm")
        plt.tight_layout()
        plt.savefig(f"{out_dir}/bar_top10_locations.png", dpi=150)
        plt.close() # Đóng để giải phóng RAM
        print(f"- Đã lưu: {out_dir}/bar_top10_locations.png")
    except Exception as e:
        print(f"Lỗi khi vẽ biểu đồ Top 10: {e}")

    # 4. Vẽ biểu đồ 2: Tỷ trọng (Pie Chart)
    try:
        share = df["CityState"].value_counts().head(5) # Top 5
        plt.figure(figsize=(8, 8))
        plt.pie(share.values, labels=share.index, autopct="%1.1f%%", startangle=90)
        plt.title("Tỷ trọng tai nạn (Top 5 địa điểm)")
        plt.savefig(f"{out_dir}/pie_location_share.png", dpi=150)
        plt.close()
        print(f"- Đã lưu: {out_dir}/pie_location_share.png")
    except Exception as e:
        print(f"Lỗi khi vẽ biểu đồ tròn: {e}")

    print("Vẽ biểu đồ hoàn tất!")