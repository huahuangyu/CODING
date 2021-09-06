# HJ7 取近似值
# https://www.nowcoder.com/practice/3ab09737afb645cc82c35d56a5ce802a?tpId=37&&tqId=21230&rp=1&ru=/ta/huawei&qru=/ta/huawei/question-ranking
# 描述
# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

n = float(input())
print(int(n + 0.5))