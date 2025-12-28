import pandas as pd

def analyze_accidents(df: pd.DataFrame):
    results = {}
    accidents_by_city = (
        df.groupby("City")
          .size()
          .sort_values(ascending=False)
    )
    results["accidents_by_city"] = accidents_by_city

    if "Hour" not in df.columns:
        df["Hour"] = pd.to_datetime(df["Start_Time"]).dt.hour
    accidents_by_hour = (
        df.groupby("Hour")
          .size()
          .sort_index()
    )
    results["accidents_by_hour"] = accidents_by_hour

    severity_count = df["Severity"].value_counts().sort_index()
    severity_percentage = round(
        severity_count / severity_count.sum() * 100,
        2
    )
    results["severity_count"] = severity_count
    results["severity_percentage"] = severity_percentage

    return results


def save_report(results, filename="report.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== BÁO CÁO PHÂN TÍCH TAI NẠN ===\n\n")
        f.write("1. Tai nạn theo thành phố:\n")
        f.write(results["accidents_by_city"].to_string())
        f.write("\n\n")
        f.write("2. Tai nạn theo khung giờ:\n")
        f.write(results["accidents_by_hour"].to_string())
        f.write("\n\n")
        f.write("3. Mức độ nghiêm trọng:\n")
        f.write(results["severity_count"].to_string())
        f.write("\n\n")
        f.write("Tỷ lệ phần trăm theo mức độ:\n")
        f.write(results["severity_percentage"].to_string())
        f.write("\n")
