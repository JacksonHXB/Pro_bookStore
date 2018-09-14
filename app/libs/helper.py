#===============================================================================
# 工具类
#===============================================================================

# 判断搜索的关键字是否是普通字符串还是ISBN码
def is_isbn_or_key(word):
    # 设置标识符，key表示关键字，isbn表示ISBN码
    isbn_or_key = 'key'
    
    # 判断字符串长度是否是13位，并且都是数字
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
        
    short_word = word.replace('-', '')
    if '-' in word and len(short_word)==10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    
    return isbn_or_key








































