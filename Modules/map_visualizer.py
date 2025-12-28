import folium
from folium.plugins import HeatMap
import pandas as pd

def plot_heatmap(df, out_html="heatmap.html"):
    print("Đang dựng bản đồ nhiệt (Heatmap)...")

    # 1. Kiểm tra xem có cột tọa độ hay không
    if 'Start_Lat' not in df.columns or 'Start_Lng' not in df.columns:
        print("Lỗi: Dữ liệu thiếu cột tọa độ (Start_Lat, Start_Lng). Không thể vẽ bản đồ.")
        return

    # 2. Lấy mẫu dữ liệu (Sampling)
    # Lưu ý quan trọng: Folium sẽ bị treo nếu vẽ quá 20.000 điểm.
    # Ta chỉ lấy mẫu khoảng 10.000 điểm để hiển thị đại diện.
    if len(df) > 10000:
        data_sample = df.sample(n=10000, random_state=42)
    else:
        data_sample = df

    # 3. Loại bỏ các dòng bị NaN ở tọa độ để tránh lỗi
    data_sample = data_sample.dropna(subset=['Start_Lat', 'Start_Lng'])

    # 4. Tính tâm bản đồ
    center_lat = data_sample["Start_Lat"].mean()
    center_lng = data_sample["Start_Lng"].mean()

    # 5. Tạo bản đồ nền
    m = folium.Map(location=[center_lat, center_lng], zoom_start=4)

    # 6. Tạo lớp Heatmap và thêm vào bản đồ
    heat_data = data_sample[["Start_Lat", "Start_Lng"]].values.tolist()
    HeatMap(heat_data, radius=10, blur=15).add_to(m)

    # 7. Lưu ra file HTML
    m.save(out_html)
    print(f"Xong! Bản đồ đã được lưu tại file: {out_html}")