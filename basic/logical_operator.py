# 論理演算子 （logical operators）
# and, or, not
a = 1
b = 1
c = 10
d = 100
print(a == b and c > d)
print(a == b or c > d)
print(not a == b)

# challenge1
age = 10  # 年齢
hight = 110  # 身長
# 年齢が10歳以上かつ身長が110cm以上なら乗れるアトラクション
print(age >= 10 and hight >= 110)

# challenge2
master_flg = False
# 修士号保持フラグ
job_experience_years = 4  # 実務経験年数
# 修士号保持もしくは5年以上の実務経験があればvisaの取得が可能
print(master_flg or job_experience_years >= 5)


