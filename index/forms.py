from django import forms
from captcha.fields import CaptchaField     # 一定要导入这行


class UserForm(forms.Form):
    username = forms.CharField(
        label='用户名',                # 在表单里表现为 label 标签
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'form-control'})   # 添加 css 属性
    )

    captcha = CaptchaField(
        label='验证码',
        required=True,
        error_messages={
            'required': '验证码不能为空'
        }
    )
