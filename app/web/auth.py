from flask import render_template, request, redirect, url_for,flash

from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.models.base import db
from app.models.user import User
from flask_login import login_user,logout_user
from . import web

# 用户注册
#------------------------------------------------------------------------------ 
@web.route('/register',methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            # 将属性遍历赋值
            user.set_attr(form.data)
            # 将数据存入到数据库中
            db.session.add(user)
        # 注册成功，就跳转
        return redirect(url_for('web.login'))
    return render_template('auth/register.html',form=form)


# 登录
#------------------------------------------------------------------------------ 
@web.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST'and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            # 在cookie中保存我们的登录信息,remember设置为cookie时长，默认是一年
            login_user(user, remember=True)
            nextPage = request.args.get('next')  # login_manager跳转的页面地址
            print("nextPage",nextPage)
            if not nextPage or not nextPage.startswith('/'):  # 判断是否是以/开头的，这样可以防止重定向攻击
                nextPage = url_for('web.index')
            return redirect(nextPage)
        else:
            flash('帐号不存在，或密码不正确！')
    return render_template('auth/login.html',form=form)


# 用户注销
#------------------------------------------------------------------------------ 
@web.rout('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))


# 处理忘记密码的提交信息
#------------------------------------------------------------------------------ 
@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account_email = form.email.data
#             try:
                # first_or_404如果没有查询到结果，会抛出异常
            user = User.query.filter_by(email=account_email).first_or_404()
#             except Exception as e:
#                 # 抛出自定义的404页面
#                 return render_template('404.thml')
            from app.libs.email import send_mail
            send_mail(form.email.data, '重置你的密码！', 'email/reset_password.html', user=user, token=user.generate_token())
            flash('一封邮件已发送到邮箱，'+account_email+'，请及时查收！')
    return render_template('auth/forget_password_request.html', form=form)


# 用户接收到邮件之后，点击处理的函数
#------------------------------------------------------------------------------ 
@web.route('/reset/password/<token>', methods=['GET','POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        result = User.reset_password(token, form.password1.data)
        if result:
            flash('你的密码已经更新，请使用新密码登录！')
            return redirect(url_for('web.login'))
        else:
            flash('密码重置失败！')
    return render_template('auth/forget_password.html', form=form)




























































