import pandas as pd
import folium
from folium.plugins import HeatMap

def plot_heatmap(csv_path, out_html="heatmap.html", sample_n=200000):
    #Load data
    data = pd.read_csv(csv_path)

    #Kiểm tra cột tọa độ có tồn tại không
    lat_col = "Start_Lat"
    lng_col = "Start_Lng"
    if lat_col not in data.columns or lng_col not in data.columns:
        raise ValueError(f'Thieu cot toa do. Cac cot hien co: {list(data.columns)}')
    
    #Giảm dữ liệu để chạy mượt (do datasheet rất lớn)
    if sample_n is not None and len(data) > sample_n:
        data = data.sample(sample_n, random_state=10)

    #Tính tâm bản đồ (lấy trung bình tọa độ)
    center_lat = data["Start_Lat"].mean()
    center_lng = data["Start_Lng"].mean()

    #Tạo map (center theo trung bình tọa độ)
    m = folium.Map(location=[center_lat, center_lng], zoom_start=4)

    #Vẽ Heatmap
    points = data[["Start_Lat", "Start_Lng"]].values.tolist()
    HeatMap(points, radius=10, blur=12, max_zoom=8).add_to(m)

    #Lưu ra file html
    m.save(out_html)
    return out_html