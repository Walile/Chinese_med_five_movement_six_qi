import datetime

# 定義天干和地支的列表
tian_gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
di_zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
year_112 = datetime.datetime(2023, 1, 1).year

# 兔年屬於地支中的第4個，因此可以對應到di_zhi列表中的第3個元素
di_zhi_index = 3

# 根據天干和地支的循環規律，可以計算出112年屬於的天干和地支
tian_gan_index = (year_112 - 4) % 10  # 4是甲子年的地支序號，10是天干的數量
tian_gan_year = tian_gan[tian_gan_index]
di_zhi_year = di_zhi[di_zhi_index]

# 將天干和地支組合起來，得到112年兔年的干支
gan_zhi_year = tian_gan_year + di_zhi_year

# 輸出結果
print("民國112年兔年對應的天干地支是：" + gan_zhi_year)
