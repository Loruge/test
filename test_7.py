winter = ['January', 'February', 'December', '1', '2', '12']
spring = ['March', 'April', 'May', '3', '4', '5']
summer = ['June', 'July', 'August', '6', '7', '8']
fall = ['September', 'October', 'November', '9', '10', '11']

a = input('Enter month\n')


def season_check():
    if a in winter:
        print('This month in Winter')
    elif a in spring:
        print('This month in Spring')
    elif a in summer:
        print('This month in Summer')
    elif a in fall:
        print('This month in Fall')
    else:
        print('Incorrect input')


season_check()
