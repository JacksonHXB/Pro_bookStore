#===============================================================================
# 验证
#===============================================================================
from wtforms import Form, StringField,IntegerField
from wtforms.validators import Length,NumberRange, DataRequired


# 验证搜索的查询字段
class SearchForm(Form):
    q = StringField()# DataRequired防止传递为空格
    page = IntegerField()























