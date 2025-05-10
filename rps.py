import random as r
while True:
    机器=r.randint(1,3)
    人={'石头':3,'剪刀':2,'布':1}.get(input())
    if 机器==人:
        print('平局')
    elif 机器-人==1 or 机器-人==-2:
        print('输')
    else:
        print('赢')
        break
