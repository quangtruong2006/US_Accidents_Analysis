import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_static_charts(csv_path, out_dir="Outputs", top_n=5):
    # Load data
    df = pd.read_csv(csv_path)

    # Check cột cần thiết
    for c in ["City", "State", "Start_Time"]:
        if c not in df.columns:
            raise ValueError(f"Thiếu cột {c}. Cột hiện có: {list(df.columns)}")

    # Xử lý thời gian + tạo mốc năm
    df["Start_Time"] = pd.to_datetime(df["Start_Time"], errors="coerce")
    df = df.dropna(subset=["Start_Time", "City", "State"])
    df["Year"] = df["Start_Time"].dt.year

    # Tạo cột địa điểm "City, State" và lấy Top N địa điểm
    df["CityState"] = df["City"].astype(str).str.strip() + ", " + df["State"].astype(str).str.strip()
    top_locs = df["CityState"].value_counts().head(top_n).index
    df_top = df[df["CityState"].isin(top_locs)]

    # (1) Bar: chênh lệch tai nạn theo Năm & Địa điểm
    year_loc = df_top.groupby(["Year", "CityState"]).size().reset_index(name="Accidents")
    plt.figure(figsize=(10, 5))
    sns.barplot(data=year_loc, x="Year", y="Accidents", hue="CityState", errorbar=None)
    plt.title(f"Chênh lệch tai nạn theo năm & địa điểm (Top {top_n})")
    plt.tight_layout()
    plt.savefig(f"{out_dir}/bar_year_location.png", dpi=200)
    plt.show()

    # (2) Bar: Top địa điểm nhiều tai nạn nhất
    top_rank = df["CityState"].value_counts().head(10).reset_index()
    top_rank.columns = ["CityState", "Accidents"]
    plt.figure(figsize=(10, 5))
    sns.barplot(data=top_rank, x="Accidents", y="CityState", errorbar=None)
    plt.title("Top 10 địa điểm nhiều tai nạn nhất")
    plt.tight_layout()
    plt.savefig(f"{out_dir}/bar_top10_locations.png", dpi=200)
    plt.show()

    # (3) Pie: tỷ trọng tai nạn theo địa điểm (Top N)
    share = df["CityState"].value_counts().head(top_n)
    plt.figure(figsize=(6, 6))
    plt.pie(share.values, labels=share.index, autopct="%1.1f%%", startangle=90)
    plt.title(f"Tỷ trọng tai nạn theo địa điểm (Top {top_n})")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig(f"{out_dir}/pie_location_share.png", dpi=200)
    plt.show()
