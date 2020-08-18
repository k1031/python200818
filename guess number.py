import random
n=random.randint(1,10)
i=0
while i<5:
    try:
        a=int(input('請輸入數字:'))
    except:
        print:('請輸入數字')
        continue
    if n==a:
        print('恭喜答對')
        print('你做了',i,'次')
        break

    elif n<a:
        print('to big')
    elif n>a:
        print('to small')
    else:
        print('錯了')
    i=i+1
    print('你錯了',i,'次')
