# HJ37 统计每个月兔子的总数
# https://www.nowcoder.com/practice/1221ec77125d4370833fd3ad5ba72395?tpId=37&&tqId=21260&rp=1&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 描述
# 有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，问每个月的兔子总数为多少？
#
# 本题有多组数据。
while True:
    try:
        month = int(input())
        a , b = 1 , 0
        for i in range(month):
            a , b = b , a + b
        print(b)
    except:
        break