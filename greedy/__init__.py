from greedy.change import Change

if __name__ == '__main__':
    while 1:
        menu = input('1. 거스름돈\n')
        if menu == '1':
            Change().count_coin()
        else:
            break
