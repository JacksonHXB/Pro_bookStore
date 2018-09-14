#===============================================================================
# 验证auth
#===============================================================================
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError, EqualTo

from app.models.user import User

# 注册验证
class RegisterForm(Form):
    nickname = StringField(validators=[DataRequired(), Length(2,10)])
    email = StringField(validators=[DataRequired(), Length(8,64), Email()])
    password = PasswordField(validators=[DataRequired(), Length(6,32)])
    
    # 自定义验证
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first(): # 使用.first()触发查询
            raise ValidationError('电子邮件已被注册！')
    
    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已经存在！')


# 登录验证
class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8,64), Email()])
    password = PasswordField(validators=[DataRequired(), Length(6,32)])



class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8,64), Email()])
    

# 重置密码校验
class ResetPasswordForm(Form):
    password1 = PasswordField(Validators=[
        DataRequired,
        Length(6,32, message='密码长度至少需要6到32个字符之间！'),
        EqualTo('pasword2', message='两次输入的密码不相同！')
    ])
    password2 = PasswordField(validators=[
        DataRequired,
        Length(6,32)
    ])
















































