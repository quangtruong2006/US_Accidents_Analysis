import pandas as pd

def analyze_accidents(df: pd.DataFrame):
    results = {}
    
    # 1. Thống kê theo Thành phố
    accidents_by_city = (
        df.groupby("City")
        .size()
        .sort_values(ascending=False)
    )
    results["accidents_by_city"] = accidents_by_city

    # 2. Thống kê theo Khung giờ
    # Đảm bảo cột Hour là số nguyên
    if "Hour" not in df.columns:
        df["Hour"] = pd.to_datetime(df["Start_Time"]).dt.hour
    
    accidents_by_hour = (
        df.groupby("Hour")
        .size()
        .sort_index()
    )
    results["accidents_by_hour"] = accidents_by_hour

    # 3. Thống kê Mức độ nghiêm trọng
    severity_count = df["Severity"].value_counts().sort_index()
    severity_percentage = round(
        severity_count / severity_count.sum() * 100,
        2
    )
    results["severity_count"] = severity_count
    results["severity_percentage"] = severity_percentage

    return results


def save_report(results, filename="Outputs/bao_cao_thong_ke.txt"):
    try:
        lines = []
        lines.append("=" * 60)
        lines.append(f"{'BÁO CÁO PHÂN TÍCH TAI NẠN GIAO THÔNG (US ACCIDENTS)':^60}")
        lines.append("=" * 60)
        lines.append("")

        # --- 1. Top 5 Thành phố ---
        if "accidents_by_city" in results:
            lines.append("📍 TOP 5 THÀNH PHỐ CÓ SỐ LƯỢNG TAI NẠN CAO NHẤT")
            lines.append("-" * 60)
            top_cities = results["accidents_by_city"].head(5)
            for i, (city, count) in enumerate(top_cities.items(), 1):
                lines.append(f"   {i}. {str(city):<30} : {count:>7,} vụ")
            lines.append("")

        # --- 2. Thống kê theo Mức độ nghiêm trọng ---
        if "severity_percentage" in results:
            lines.append("⚠️ TỶ LỆ MỨC ĐỘ NGHIÊM TRỌNG (SEVERITY)")
            lines.append("-" * 60)
            severity = results["severity_percentage"]
            for level, pct in severity.items():
                bar_length = int(pct // 5)
                bar_chart = "█" * bar_length
                lines.append(f"   - Mức độ {level}: {pct:>6.2f}%  {bar_chart}")
            lines.append("")

        # --- 3. Top 5 Khung giờ nguy hiểm nhất ---
        if "accidents_by_hour" in results:
            lines.append("⏰ TOP 5 KHUNG GIỜ CAO ĐIỂM DỄ XẢY RA TAI NẠN")
            lines.append("-" * 60)
            top_hours = results["accidents_by_hour"].sort_values(ascending=False).head(5)
            for i, (hour, count) in enumerate(top_hours.items(), 1):
                # --- SỬA LỖI TẠI ĐÂY: Ép kiểu int(hour) ---
                h = int(hour) 
                time_str = f"{h:02d}:00 - {h:02d}:59"
                lines.append(f"   {i}. Khung giờ {time_str:<15} : {count:>7,} vụ")
            lines.append("")

        lines.append("=" * 60)
        lines.append(f"{'KẾT THÚC BÁO CÁO':^60}")
        lines.append("=" * 60)

        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
            
        print(f"✅ Đã lưu báo cáo chi tiết (bản đẹp) vào: {filename}")

    except Exception as e:
        print(f"❌ Lỗi khi lưu file báo cáo: {e}")