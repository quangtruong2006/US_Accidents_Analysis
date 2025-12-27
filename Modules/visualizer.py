import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# 0) ĐỌC DỮ LIỆU
# =========================
# Đọc file CSV dữ liệu tai nạn (dữ liệu thật)
# 👉 SỬA ĐƯỜNG DẪN CHO ĐÚNG MÁY BẠN
df = pd.read_csv("US_Accidents_Top20_Cities.csv")

# Chuyển Start_Time sang datetime để lấy Năm
df["Start_Time"] = pd.to_datetime(df["Start_Time"], errors="coerce")

# Loại bỏ dòng thiếu thời gian
df = df.dropna(subset=["Start_Time"])

# Tạo cột Năm
df["Year"] = df["Start_Time"].dt.year


# =========================
# BIỂU ĐỒ 1: CỘT NHÓM
# Chênh lệch tai nạn theo NĂM và ĐỊA ĐIỂM
# =========================

# 1) Tạo cột địa điểm dạng "City, State"
#    Mục đích: tránh trùng tên City ở các bang khác nhau
df["CityState"] = (
    df["City"].astype(str).str.strip()
    + ", "
    + df["State"].astype(str).str.strip()
)

# 2) Lấy Top 5 địa điểm có nhiều tai nạn nhất
#    (để biểu đồ gọn, dễ nhìn)
top_locations = df["CityState"].value_counts().head(5).index
df_top = df[df["CityState"].isin(top_locations)]

# 3) Đếm số tai nạn theo từng (Năm, Địa điểm)
#    size() = đếm số dòng (mỗi dòng = 1 vụ tai nạn)
year_location = (
    df_top.groupby(["Year", "CityState"])
          .size()
          .reset_index(name="Accidents")
)

# 4) Vẽ biểu đồ cột nhóm
plt.figure(figsize=(10, 5))
sns.barplot(
    data=year_location,
    x="Year",
    y="Accidents",
    hue="CityState",
    errorbar=None
)
plt.title("Chênh lệch số vụ tai nạn theo năm và địa điểm")
plt.xlabel("Năm")
plt.ylabel("Số vụ tai nạn")
plt.legend(title="Địa điểm")
plt.tight_layout()
plt.show()


# =========================
# BIỂU ĐỒ 2: CỘT
# Top địa điểm có nhiều tai nạn nhất
# =========================

# 1) Đếm số tai nạn theo địa điểm, lấy Top 10
top10 = df["CityState"].value_counts().head(10).reset_index()
top10.columns = ["CityState", "Accidents"]

# 2) Vẽ biểu đồ cột ngang
plt.figure(figsize=(9, 5))
sns.barplot(
    data=top10,
    x="Accidents",
    y="CityState",
    errorbar=None
)
plt.title("Top 10 địa điểm có nhiều tai nạn nhất")
plt.xlabel("Số vụ tai nạn")
plt.ylabel("Địa điểm")
plt.tight_layout()
plt.show()


# =========================
# BIỂU ĐỒ 3: TRÒN
# Tỷ trọng tai nạn theo địa điểm
# =========================

# 1) Lấy Top 5 địa điểm
top5 = df["CityState"].value_counts().head(5)

# 2) Vẽ biểu đồ tròn
plt.figure(figsize=(6, 6))
plt.pie(
    top5.values,
    labels=top5.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Tỷ trọng tai nạn theo địa điểm (Top 5)")
plt.axis("equal")  # giữ hình tròn không méo
plt.tight_layout()
plt.show()
