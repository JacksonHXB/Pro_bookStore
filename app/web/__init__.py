#===============================================================================
# 蓝图初始化
#===============================================================================
from flask import Blueprint, render_template

# 蓝图blueprint:用于解决视图函数与app的绑定问题,用一个蓝图管理多个不同的视图函数
web = Blueprint('web', __name__)
# web = Blueprint('web', __name__, template_folder='templates')# 这里的蓝图也可以注册静态文件static_folder='', static_url_path=''

# 分别导入蓝图管理的所有视图函数文件
from app.web import book
from app.web import auth
from app.web import gift
from app.web import wish
from app.web import main

# 当访问请求返回的状态码是404时，默认返回执行的函数,这里运用了AOP的思想
@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404



















































































































