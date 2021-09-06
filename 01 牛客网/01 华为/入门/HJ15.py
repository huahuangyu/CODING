# HJ15 求int型正整数在内存中存储时1的个数
# https://www.nowcoder.com/practice/440f16e490a0404786865e99c6ad91c9?tpId=37

n = int(input())
n = bin(n)
print(n.count('1'))
