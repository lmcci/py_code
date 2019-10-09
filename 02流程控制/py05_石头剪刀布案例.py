#
import random
random_index = random.randint(1, 3)  # 左右都包含
# print(type(random_index))
if random_index == 1:
    computer = '石头'
elif random_index == 2:
    computer = '剪刀'
else:
    computer = '布'

player = input('请输入要出的类型 （石头，剪刀，布）')

print('您出的是 %s' % player)

if player != '石头' and player != '剪刀' and player != '布':
    print('输入不合法')
else:
    if player == computer:
        print('平局')
    elif (player == '石头' and computer == '剪刀'
            or player == '剪刀' and computer == '布'
            or player == '布' and computer == '石头'):
        print('玩家获胜')
    else:
        print('电脑获胜')
