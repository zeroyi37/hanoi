def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n-1, x, z, y)#将X塔上1~n-1个圆盘移到Y塔上，以Z塔为辅助塔
        print(x, '-->', z)#将第n个圆盘移到Z塔上
        hanoi(n-1, y, x, z)#把Y塔上编号1~n-1的圆盘移到Z上，以X为辅助塔

n = int(input('请输入汉诺塔层数：'))
hanoi(n, 'X', 'Y', 'Z')
