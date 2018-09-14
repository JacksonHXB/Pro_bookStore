from flask import Flask,make_response

# 也可以通过引入包的方式载入配置文件
# import config

__author__ = '黄小兵'
app = Flask(__name__)


# 载入配置文件，通过该方式载入时，所有的KEY都要大写
app.config.from_object('config')


@app.route('/hello')
def hello():
    # 方式一：return会返回status-code和content-type以及包含中的内容，不指定content-type会设置默认值为text/html
#     return "<html></html>"
    
    # 方式二：通过返回response对象，来输出特定的东西,在headers中加入location就是重定向的基本原理
    headers = {
        'content-type':'text/plain',
        'location':'http://www.baidu.com'
    }
#     response = make_response('<html></html>', 301)
#     response.headers = headers
#     return response

    # 方式三：也可以通过这种方式直接返回
    return '<html></html>', 301, headers
    


# 可以不通过装饰器的方式注册URL
# app.add_url_rule('/hello', view_func=hello)


# IF可以确保在生产环境中不会启动Flask内置的web服务器
if __name__ == '__main__':
    # 启动Flask服务，并开启调试模式,同时可以指定IP地址,四个0表示可以通过外网访问
    # 在生产环境，nginx+uwsgi的方式配置服务器
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])












































