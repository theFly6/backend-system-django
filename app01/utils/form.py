from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import ModelForm, CharField, TextInput, PasswordInput, Form

from app01.models import UserInfo, PrettyNumber, Admin, Task
from app01.utils.encrypt import md5


class BootStrap:
    execlude_field = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # print(f'name={name}, field.label={field.label}')
            if name in self.execlude_field:
                continue
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class BootStrapModelForm(BootStrap, ModelForm):
    pass


class BootStrapForm(BootStrap, Form):
    pass


# class BootStrapModelForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for name, field in self.fields.items():
#             # print(f'name={name}, field.label={field.label}')
#             # >>> name=title, field.label=名称
#             field.widget.attrs = {'class': 'form-control', 'placeholder': name}


class UserModelForm(ModelForm):
    name = CharField(min_length=3, label='姓名')

    # create_time = CharField(min_length=3, label='日期',
    #                         widget=TextInput(attrs={"class": 'form-control', 'placeholder': 'create_time'}))

    class Meta:
        model = UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'depart', 'gender']
        widgets = {
            'create_time': TextInput(attrs={"class": 'form-control', 'placeholder': 'create_time'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': name}


class PrettyModel(ModelForm):
    mobile = CharField(label='手机号',
                       validators=[RegexValidator(r'^\d{11}$',
                                                  '1:请填写11位数字'),
                                   RegexValidator(r'^1(31|59|37|52).*',
                                                  '数字必须以131/137/152/159开头'),
                                   RegexValidator(r'^.*0$',
                                                  '数字必须以0结尾')])

    class Meta:
        model = PrettyNumber
        fields = ['mobile', 'price', 'level', 'status']
        # fields = '__all__'
        # exclude = ['level']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': name}

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if len(mobile) != 11:
            raise ValidationError('2:请填写11位数字')
        elif mobile == '13100000000':
            raise ValidationError('保留号码禁止填写')
        elif PrettyNumber.objects.filter(mobile=mobile).exists():
            raise ValidationError('此号码已注册')
        return mobile


class PrettyEditModel(ModelForm):
    status = CharField(disabled=True, label='状态')

    class Meta:
        model = PrettyNumber
        fields = ['mobile', 'price', 'level', 'status']
        # exclude = ['level']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': name}

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        m_id = self.instance.pk
        if len(mobile) != 11:
            raise ValidationError('2:请填写11位数字')
        elif mobile == '13100000000':
            raise ValidationError('保留号码禁止填写')
        elif PrettyNumber.objects.filter(mobile=mobile).exclude(id=m_id).exists():
            raise ValidationError('此号码已注册')
        return mobile


class AdminModelForm(BootStrapModelForm):
    confirm_password = CharField(
        label='确认密码',
        widget=PasswordInput(render_value=True)
    )

    class Meta:
        model = Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'password': PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        confirm = md5(self.cleaned_data.get('confirm_password'))
        pwd = self.cleaned_data.get('password')
        if confirm != pwd:
            raise ValidationError('两次输入值不一致')
        return confirm


class AdminResetModelForm(BootStrapModelForm):
    confirm_password = CharField(
        label='确认密码',
        widget=PasswordInput(render_value=True)
    )

    class Meta:
        model = Admin
        fields = ['password', 'confirm_password']
        widgets = {
            'password': PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        md5_pwd = md5(pwd)
        if Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists():
            raise ValidationError('密码不能与以前的密码相同')
        return md5_pwd

    def clean_confirm_password(self):
        confirm = md5(self.cleaned_data.get('confirm_password'))
        pwd = self.cleaned_data.get('password')
        if confirm != pwd:
            raise ValidationError('两次输入值不一致')
        return confirm


class TaskForm(BootStrapModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'detail': TextInput
        }
