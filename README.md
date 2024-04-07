# 后台管理系统（基于Django实现）



# 1. 项目说明

​	本应用是基于Django实现的后台管理系统，UI组件使用BootStrap，通过Mysql数据库进行数据存储，图表有用到echarts和hcharts。



# 2. 使用说明

- 首先安装所需依赖库：django，PIL等库。
- 然后再修改setting中的mysql数据库配置连接到一个新的用于存放账号信息的一个数据库上。

- 最后按照正常的Django项目启动流程即可正常运行：
  - `python manage.py makemigrations`
  - `python manage.py migrate`
  - `python manage.py migrate`（第二次执行效果为向绑定的数据库插入管理员账号：用户名Admin、密码123）
  - `python manage.py runserver 8080`



# 3. 效果展示

**登陆界面**

![](./md_pic/登陆界面.png)

**部门管理**

![](./md_pic/部门管理.png)



**新增用户**

![](./md_pic/新增用户.png)



**用户管理界面**

![](./md_pic/用户管理界面.png)



**管理员界面**

![](./md_pic/管理员页面.png)

**任务管理**

![](./md_pic/任务管理.png)



**订单管理**

![](./md_pic/订单管理.png)



**任务管理**

![](./md_pic/echarts数据图表.png)



**头像信息上传**

![](./md_pic/头像信息上传.png)

