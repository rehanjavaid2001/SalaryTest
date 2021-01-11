#Rehan Javaid rj3dxu
import salary

for name in (
        'James E. Ryan',
        'Ryan, James E',
        '181067633',
        'Hao Ran Laurenc Lin',
        '181016364',
        'Thomas Jefferson'
        ):
    job, money, rank = salary.report(name)
    print(name, 'is a', job, 'and makes', money, '(rank', str(rank)+')')