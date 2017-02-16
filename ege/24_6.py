x, y = map(int, input().split())
if y >= x+1:
    if y <= 2-2*x*x:
        print('принадлежит')
    else:
        if y >= x*x-5:
            print('принадлежит')
        else:
            print('не принадлежит')

