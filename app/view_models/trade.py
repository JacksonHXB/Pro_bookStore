from .book import BookViewModel

class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)
    
    # 处理一组数据
    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]
        
        
    # 处理单个数据
    def __map_to_trade(self, single):
        if single.create_datetime():
            time = single.create_datetime().strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name = single.tb_user.nickname,
            time = time,
            id = single.id
        )


class MyTrades:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.trades = []
        
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list
        
        self.trades = self.__parse()
        
    def __parse(self):
        temp_gifts = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts
                
    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        r = {
            'wishes_count':count,
            'book':BookViewModel(gift.book),
            'id':gift.id
        }
        return r
























































