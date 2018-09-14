#===============================================================================
# Flask服务器
#===============================================================================
from app import create_app

__author__ = '黄小兵'

# 初始化app
app = create_app()


if __name__ == '__main__':
    # threaded是开启多线程
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'], threaded=True)


















































