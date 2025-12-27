import pandas as pd

def analyze_accidents(df: pd.DataFrame):
    """
    Phân tích dữ liệu tai nạn giao thông:
    - Theo thành phố
    - Theo khung giờ
    - Theo mức độ nghiêm trọng (Severity)
    """

    print("Đang tính toán thống kê...") 
    results = {}

    # ===============================
    # 1. Tổng số tai nạn theo thành phố
    # ===============================
    if "City" in df.columns:
        accidents_by_city = (
            df.groupby("City")
            .size()
            .sort_values(ascending=False)
        )
        results["accidents_by_city"] = accidents_by_city

    # ===============================
    # 2. Phân tích theo khung giờ
    # ===============================
    # Nếu chưa có cột Hour thì tạo
    if "Start_Time" in df.columns:
        if "Hour" not in df.columns:
            df["Hour"] = pd.to_datetime(df["Start_Time"], errors='coerce').dt.hour

        accidents_by_hour = (
            df.groupby("Hour")
            .size()
            .sort_index()
        )
        results["accidents_by_hour"] = accidents_by_hour

    # ===============================
    # 3. Phân tích theo mức độ nghiêm trọng
    # ===============================
    if "Severity" in df.columns:
        severity_count = df["Severity"].value_counts().sort_index()

        severity_percentage = round(
            severity_count / severity_count.sum() * 100,
            2
        )

        results["severity_count"] = severity_count
        results["severity_percentage"] = severity_percentage

    return results

def save_report(stats, file_path="Outputs/bao_cao_thong_ke.txt"):
    """
    Hàm nhận kết quả thống kê (stats) và lưu vào file văn bản.
    """
    try:
        content = []
        content.append("="*40)
        content.append("📊 KẾT QUẢ THỐNG KÊ CHI TIẾT (REPORT)")
        content.append("="*40)

        if "accidents_by_city" in stats:
            content.append("\n📍 Top 5 Thành phố nhiều tai nạn nhất:")
            content.append(str(stats["accidents_by_city"].head(5)))

        if "severity_percentage" in stats:
            content.append("\n⚠️ Tỷ lệ mức độ nghiêm trọng (%):")
            content.append(str(stats["severity_percentage"]))

        if "accidents_by_hour" in stats:
             content.append("\n⏰ Các khung giờ hay xảy ra tai nạn nhất (Top 5):")
             content.append(str(stats["accidents_by_hour"].sort_values(ascending=False).head(5)))
        
        content.append("\n" + "="*40)
        
        # Ghi vào file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))
            
        print(f"✅ Đã lưu báo cáo chi tiết vào: {file_path}")
        
    except Exception as e:
        print(f"❌ Lỗi khi lưu file báo cáo: {e}")