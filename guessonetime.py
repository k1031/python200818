import random
n=random.randint(1,10)
while True:
    try:
        a=int(input('請輸入數字:'))
    except:
        print:('請輸入數字')
        continue
    if n==a:
        print('恭喜答對')
    else:
        print('錯了')



