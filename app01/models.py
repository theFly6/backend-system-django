from django.db import models


# Create your models here.

class Admin(models.Model):
    """ 管理员 """
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

    def __str__(self):
        return self.username


class Department(models.Model):
    """部门表"""
    title = models.CharField(max_length=32, verbose_name='标题')

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(max_length=16, verbose_name='姓名')
    password = models.CharField(max_length=64, verbose_name='密码')
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='账户余额')
    create_time = models.DateField(verbose_name='入职时间')
    # 1. 级联删除
    depart = models.ForeignKey(to='Department', to_field='id', on_delete=models.CASCADE, verbose_name='部门')
    # 2. 置空
    # depart = models.ForeignKey(to='Department', to_field='id', on_delete=models.SET_NULL, blank=True, null=True)
    gender_choices = (
        (1, '男'),
        (0, '女')
    )
    gender = models.SmallIntegerField(choices=gender_choices, verbose_name='性别')


class PrettyNumber(models.Model):
    """ 靓号表 """
    mobile = models.CharField(verbose_name='手机号', max_length=11)
    price = models.SmallIntegerField(verbose_name='价格', default=0, null=True, blank=True)
    level_choices = (
        (1, '1级'),
        (2, '2级'),
        (3, '3级')
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)
    status_choices = (
        (1, '已占用'),
        (2, '未使用')
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=2)


class Task(models.Model):
    level_choices = (
        (1, '紧急'),
        (2, '重要'),
        (3, '临时')
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)
    title = models.CharField(verbose_name='标题', max_length=32)
    detail = models.TextField(verbose_name='详细信息')
    manager = models.ForeignKey(to=Admin, verbose_name='负责人', on_delete=models.CASCADE)


class Order(models.Model):
    oid = models.CharField(verbose_name='订单号', max_length=64)
    title = models.CharField(verbose_name='名称', max_length=32)
    price = models.IntegerField(verbose_name='价格')
    status_choice = (
        (1, '待支付'),
        (2, '已支付'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choice, default=1)
    admin = models.ForeignKey(verbose_name='管理员', to='Admin', on_delete=models.CASCADE)


class Boss(models.Model):
    name = models.CharField(verbose_name='老板', max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    img = models.CharField(verbose_name='图片', max_length=64)


class City(models.Model):
    name = models.CharField(verbose_name='城市', max_length=32)
    count = models.IntegerField(verbose_name='人口')
    # 本质上也是CharField，自动保存
    img = models.FileField(verbose_name='LOGO', max_length=128, upload_to='city2')

try:
    if not Admin.objects.filter(username='Admin').exists():
        Admin.objects.create(username='Admin',
                             password='c21c2510e4001fdadb85416ecb8c46f4')
except Exception as e:
    print('@@@@@出现此提示无需惊慌')
    print('@@@@@如果你正在执行python manage.py makemigrations,则忽略此信息')
    print('@@@@@如果你正在执行python manage.py migrate, 请你再次执行此命令')
    print('@@@@@执行完上述指令后最终执行python manage.py runserve 8080')
    print('@@@@@即可成功运行项目(账号Admin,密码123)')