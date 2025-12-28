import pandas as pd
import folium
from folium.plugins import HeatMap
import os

def plot_heatmap(df, out_html="Outputs/heatmap.html", sample_n=200000):
    # Tạo bản sao để không ảnh hưởng dữ liệu gốc bên main
    data = df.copy()

    # Kiểm tra cột tọa độ có tồn tại không
    lat_col = "Start_Lat"
    lng_col = "Start_Lng"
    if lat_col not in data.columns or lng_col not in data.columns:
        print(f"⚠️ Thiếu cột tọa độ. Các cột hiện có: {list(data.columns)}")
        return

    # Xóa các dòng bị thiếu tọa độ (Folium rất kỵ NaN)
    data = data.dropna(subset=[lat_col, lng_col])

    # Giảm dữ liệu để chạy mượt (Map không vẽ nổi triệu điểm đâu)
    if sample_n is not None and len(data) > sample_n:
        data = data.sample(sample_n, random_state=10)
        print(f"ℹ️ Đã lấy mẫu ngẫu nhiên {sample_n} điểm để vẽ bản đồ cho mượt.")

    # Tính tâm bản đồ
    if not data.empty:
        center_lat = data[lat_col].mean()
        center_lng = data[lng_col].mean()
    else:
        center_lat, center_lng = 37.09, -95.71 # Mặc định Mỹ

    # Tạo map
    m = folium.Map(location=[center_lat, center_lng], zoom_start=4)

    # Vẽ Heatmap
    heat_data = data[[lat_col, lng_col]].values.tolist()
    HeatMap(heat_data, radius=10, blur=12, max_zoom=8).add_to(m)

    # Lưu ra file html
    os.makedirs(os.path.dirname(out_html), exist_ok=True)
    m.save(out_html)
    print(f"✅ Đã lưu bản đồ nhiệt vào: {out_html}")
    return out_html