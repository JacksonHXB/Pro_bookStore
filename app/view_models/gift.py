from .book import BookViewModel
# from collections import namedtuple


# 创建一个类并实例化对象
# MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])

# 循环导入的解决方案
# 方案一，在循环导入的双方的代码最后面，才导入两个模型
# 方案二：在使用的时候在代码上一句导入模型



class MyGifts:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list
        
        self.gifts = self.__parse()
        
    def __parse(self):
        temp_gifts = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts
                
    # 获取单个书本的心愿总数
    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        # 使用dict，有利于rest api的序列化
        r = {
            'wishes_count':count,
            'book':BookViewModel(gift.book),
            'id':gift.id
        }
        return r
#         my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
#         return my_gift

# class MyGift:
#     def __init__(self):
#         pass











































