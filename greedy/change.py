class Change:
    def count_coin(self):
        product_price = int(input('상품 가격 : '))
        money = int(input('낸 돈 : '))
        change = money - product_price
        count_coin = 0
        for coin in [500, 100, 50, 10]:
            count_coin += change // coin
            change %= coin
        print(f'거슬러줘야 할 동전의 최소 개수 : {count_coin}')

        '''
        count_500 = change // 500
        count_100 = change % 500 // 100
        count_50 = change % 500 % 100 // 50
        count_10 = change % 500 % 100 % 50 // 10
        count_coin = count_500 + count_100 + count_50 + count_10
        '''