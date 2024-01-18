import datetime


print("欲計算西元年的天干地支，請按Enter輸入西元年：")
year = int(input())
chinese_year = gan_zhi_year(year)
print('西元{}年是{}年'.format(year, chinese_year))

# 輸出結果
print('民國{}年兔年對應的天干地支是： {}'.format(year, gan_zhi_year))

def gan_zhi_year(year):

    # 定義天干和地支的列表
    tian_gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    di_zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

    # 根據天干和地支的循環規律，可以計算出112年屬於的天干和地支
    base_index = (year - 4) % 60
    tian_gan_index = base_index % 10  # 4是甲子年的地支序號，10是天干的數量

    tian_gan_year = tian_gan[tian_gan_index]
    di_zhi_index = base_index % 12  # 12是地支的數量
    di_zhi_year = di_zhi[di_zhi_index]
    # 將天干和地支組合起來，得到干支
    gan_zhi_year = tian_gan_year + di_zhi_year

    return gan_zhi_year
