# -*- coding: UTF-8 -*-

start = int(input(r"请输入本金："))
count = int(input(r"请输入次数数："))

def get_money(start_money, count_num):
    """
    每次都是当前金额除以81，取整数
    """
    pay_mongy = 0
    for num in range(count_num):
        benjing = start_money // 81
        shouyi =  benjing * 0.975
        start_money += shouyi
        pay_mongy += benjing
        print(benjing, shouyi, start_money)
    return start_money, pay_mongy

res_money, pay_mongy = get_money(start_money=start, count_num=count)
print("最后得到的钱：", res_money)
print("投入的钱：", pay_mongy)
