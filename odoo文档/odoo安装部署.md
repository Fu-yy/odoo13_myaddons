# odoo安装部署

## 环境安装步骤(windows)

> 前提：本机已经安装好python3.7，pycharm2019，node12.18.2，vc++4.0

### 1.安装PostgreSQL 及pgAdmin4并新建数据库

#### 安装数据库及可视化连接工具

> git地址 https://gitee.com/Fu-yy/typora-cloud-notes.git  在根目录下/安装包/odoo相关

#### 安装后需要新建一个用户，并赋予用户相关权限

```bash
# cmd进入postgresql的bin目录
D:\PostgreSQL\9.3\bin>createuser.exe -U postgres -P baixyu
为新角色输入的口令:
再输入一遍:
口令:
#该例子创建了一个baixyu的角色，注意这里面不是用户，而是角色，U选项指出了你想要建立的新用户的编号。必须是PostgreSQL的用户才能建立用户，通常情况下就是postgres用户。-P选项通知createuser提示输入新用户的密码。
-------------------------------------------------

#为新建的角色赋予创建数据库的权限
#使用可视化工具或者postgresql自带的psql都可
```

> 默认用户（postgres）无法被外部链接

#### 创建数据库

```shell
#新建数据库
D:\PostgreSQL\9.3\bin>createdb.exe -U baixyu test
口令:

D:\PostgreSQL\9.3\bin>psql -U baixyu -d test
用户 baixyu 的口令：
psql (9.3.5)
输入 "help" 来获取帮助信息.
```



### 2.获取odoo源码(本次使用odoo13.0)

```bash
git clone https://gitee.com/mirrors/odoo.git odoo13 -b 13.0 --depth 1
```

#### 配置PyCharm环境

- 配置pycharm相关参数

  ![image-20201030085057603](images/ODOO安装部署/image-20201030085057603.png)
  ![image-20201030085119741](images/ODOO安装部署/image-20201030085119741.png)

  

  

- Parameters中添加参数:--config=***\odoo.conf
    ![image-20201030085145065](images/ODOO安装部署/image-20201030085145065.png)

	> 注意：需要在odoo13文件夹中新建一个odoo.conf配置文件

- odoo.conf配置文件

  ```properties
  [options]
  db_host=localhost	#postgresql数据库地址
  db_port=5432		#postgresql端口号
  db_user=testuser	#新建的用户名
  db_password=4117	#密码
  dbfilter = odoo		#具体不清楚什么含义
  addons_path=./addons	#addons路径
  ```

- 根据python版本调整requirements.txt中的参数，将不符合自己环境版本的字段删掉（本机是3.7，需要将lxml==3.7.1的一条删掉）

![image-20201030090028334](images/ODOO安装部署/image-20201030090028334.png)

- 打开Terminal 输入命令安装插件

  ```bash
  pip install -r requirements.txt
  ```

- 运行后输入 http://127.0.0.1:8069/

  > 在表单中输入邮箱和密码（就是以后登陆的账户及密码），在数据库选择处输入一个postgresql中没有的库，odoo会自动初始化一个库

## 开发

### 安装自定义模块

```bash
#odoo-bin ---- odod的启动脚本(相对于根目录)
#scaffold  ---- 脚手架  指的是 会把新建的模块 其他的文件一并创建，如controllers、demo、data、views、models、__manifest__.py等
#todo ---- 新模块的名字（官方建议小写）
#myaddons ---- 指定新模块的存放位置，建议自定义一个新的文件夹存放新创建的模块(相对于根目录)
python odoo-bin scaffold todo myaddons	
```

### 模块下各层结构

![image-20201105095133620](images/ODOO安装部署/image-20201105095133620.png)

> demo和security文件分别用于演示数据和安全控制文件的存放，views下是xml文件，用来控制视图

#### manyfest.py

```python
 {
     'name': 'To-Do Application',     #名称 必填
     'description': 'Manage your personal To-Do     tasks.',     #描述信息
     'author': 'Daniel Reis',     	#作者
     'depends': ['base'],     		#依赖
     'application': True, 			#是否为应用
     'data':[]
 }
    
    
#其他参数

#summary--显示为模块的副标题

#version--默认为 1.0。 它应该遵循版本语义规则（详见http://semver.org/）

#license--许可证标识符，默认为LGPL-3

#website--网站是一个用于查找有关模块的更多信息的URL。 这可以帮助人们找到更多的文档或问题跟踪，以提出 Bug 和建议。


#category--模块的功能类别，默认为Uncategorized。 现有类别的列表可以在【应用程序】下拉列表中的安全组表单（设置|用户|组）中找到其它可用的描述符：
#    installable 默认为 True，但可以设置为 False 以禁用模块
#    auto_install 如果设置为True，此模块将被自动安装，前提是其所有依赖项都已安装。 它用于必装模块


#data--关联的路径 包括权限路径、views下的文件路径
    # data实例
    # 添加模块后需要在manyfest中添加data

    'data': [
            'security/ir.model.access.csv',	
            'views/views.xml',
            'views/templates.xml',
        ],
    # 使用scaffold脚手架安装的模块在默认情况下'security/ir.model.access.csv'是被注释掉的，需要手动打开，此行决定安装应用后在侧边菜单是否展示此应用
```

![image-20201105095320898](images/ODOO安装部署/image-20201105095320898.png)

![image-20201105095337600](images/ODOO安装部署/image-20201105095337600.png)

![image-20201105095351451](images/ODOO安装部署/image-20201105095351451.png)



**为应用添加图标**

![image-20201105095541618](images/ODOO安装部署/image-20201105095541618.png)





#### modul层

```python
  # -*- coding: utf-8 -*- 
  from odoo import models, fields 
  class TodoTask(models.Model): 
   _name = 'todo.task' 
   _description = 'To-do Task'
   name = fields.Char('Description', required=True) 
   is_done = fields.Boolean('Done?') 
   active = fields.Boolean('Active?', default=True) 


-------------------------------------------------------------
#第一行 # -*- coding: utf-8 -*- 是一个特殊的标记告诉Python解释器，这个文件有UTF-8，以便它可以期望和处理非ASCII字符。我们不会使用任何非 ANSI 字符，但无论如何这是一个很好的做法。

#第二行是Python代码import语句，从Odoo核心导入模型和字段对象。

#第三行声明了我们的新模型。它是从models.Model派生的类。

#第四行设置_name属性，定义将在整个Odoo中引用此模型的标识符。注意，实际的Python类名，在这个例子中，TodoTask对其他Odoo模块是无意义的。 _name值将用作标识符。

#请注意，此行和以下行是缩进的。如果你不熟悉Python，你必须知道这是很重要的：缩进定义一个嵌套的代码块，所以这四行应该是同样缩进。

#然后我们有_description模型属性。它不是强制性的，但它为模型记录提供了一个用户友好的名称，可用于用户友好的消息。

#最后三行定义模型的字段。值得注意的是name和active是特殊的字段名。默认情况下，当从其他模型引用它时，Odoo将使用name字段作为记录的标题。active字段用于停用记录，默认情况下，仅显示活动记录。我们将使用它来清除已完成的任务，而不会从数据库中删除它们。
```

> 实例:分组对应多个事项

```python
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TodoCategory(models.Model):
    _name = "todo.category"
    _description = "待办事项类别"
    name = fields.Char(string="类别名称", required=True)


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = '待办事项详情'

    name = fields.Char(string="事项名称", required=True)
    is_done = fields.Boolean(string="是否完成")
    priority = fields.Selection(string="紧急程度",
                                selection=[("todo", "待办"), ("normal", "普通"), ("urgency", "紧急")],
                                default="todo")
    deadline = fields.Datetime(string="截止时间")
    is_expired = fields.Boolean(string="是否过期", compute="_compute_is_expired")
    category_id = fields.Many2one(string="类别", comodel_name="todo.category")
    # test = fields.Char("shifou", required=True)

    @api.depends("deadline")
    def _compute_is_expired(self):
        for res in self:
            if(res.deadline):
                res.is_expired = res.deadline < fields.Datetime.now()
            else:
                res.is_expired = False

```



> 根据条件的不同显示不同的下拉列表

- 在后端控制的写法

![image-20201105092926110](images/ODOO安装部署/image-20201105092926110.png)

![image-20201105092937449](images/ODOO安装部署/image-20201105092937449.png)

![image-20201105091914139](images/ODOO安装部署/image-20201105091914139.png)

![image-20201105091954714](images/ODOO安装部署/image-20201105091954714.png)

- 在前端控制的写法

![image-20201105092426469](images/ODOO安装部署/image-20201105092426469.png)



#### security层

> 此文件夹中```ir.model.access.csv```文件决定了模块是否对某些用户展示，可以达到权限控制的目的

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_todo_task,todo.task,model_todo_task,base.group_user,1,1,1,1


//参数说明
ir.model.access.csv
id:权限id，默认规则是access_模块名_类名，还没发现有什么用
name:权限名，默认规则是模块名.类名，还没发现有什么用
model_id:id:这个是固定写法，规则是model_模块名_类名，其它地方引用权限会用这个id
group_id:id:组id,这里的base.group_user是系统内置组，即员工.员工组，创建帐户时，默认属于这个组。所以给这个组赋权限，相当于给新帐户的默认权限。
perm_read,perm_write,perm_create,perm_unlink:对应读、写、增加、删除权限，1是有权限，0是无权限，具体根据需要来设置权限
```

![image-20201105101400147](images/ODOO安装部署/image-20201105101400147.png)

#### views层

##### templates.xml

##### views.xml

> 可以在此文件中定义字段的显示方式等

```xml
<odoo>
    <data>

	<!--todo.category list 展示列表 -->
        <record model="ir.ui.view" id="todo_category_list">
            <field name="name">Todo Category List</field>
            <field name="model">todo.category</field>
            <field name="arch" type="xml">
                <tree string="Todo Category">
                    <field name="name"/>
                </tree>
            </field>
        </record>
        <!--todo.category form  也就是详情  -->
        <record model="ir.ui.view" id="todo_category_form">
            <field name="name">Todo Category Form</field>
            <field name="model">todo.category</field>
            <field name="arch" type="xml">
                <form>
                    <sheet>
                        <group>
                            <group>
                                <field name="name"/>
                            </group>
                            <group>

                            </group>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>

<!--todo.task model的 list列表 -->
        <record model="ir.ui.view" id="todo_task_list">
            <field name="name">Todo Task List</field>
            <field name="model">todo.task</field>
            <field name="arch" type="xml">
                <tree>
                    <field name="name"/>
                    <field name="is_done"/>
                    <field name="priority"/>
                    <field name="deadline"/>
                    <field name="is_expired"/>
                    <field name="category_id"/>
                </tree>
            </field>
        </record>

<!--todo.task model的 form详情 -->
        <record model="ir.ui.view" id="todo_task_form">
            <field name="name">Todo Task Form</field>
            <field name="model">todo.task</field>
            <field name="arch" type="xml">
                <form>
                    <sheet>
                        <group>
                            <group>
                                <field name="name"/>
                                <field name="is_done"/>
                            </group>
                            <group>
                                <field name="priority"/>
                                <field name="deadline"/>
                                <field name="is_expired"/>
                                <field name="category_id"/>
                            </group>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>


        <!-- actions opening views on models -->
 <!-- todo.task model的 菜单跳转路径 -->
        <record model="ir.actions.act_window" id="act_todo_task_win">
            <field name="name">Todo task window</field>
            <field name="res_model">todo.task</field>
            <field name="view_mode">tree,form</field>
        </record>
 <!-- todo.category model的 菜单跳转路径 -->
         <record model="ir.actions.act_window" id="act_todo_category_win">
             
            <field name="name">Todo task window</field>
             <!-- model的id  唯一  与models中models.py文件对应 -->
            <field name="res_model">todo.category</field>
            <field name="view_mode">tree,form</field>
        </record>


        <!-- Top menu item -->

        <menuitem name="Todo" id="menu_root"/>

		<!-- 一级菜单   name:显示的文字 -->
        <menuitem name="Todo Manager" id="menu_todo_manager" parent="menu_root"/>

        <!-- actions -->
        <!-- 二级菜单   name:显示的文字  parent：一级菜单id  sequence：排列的优先级 数越大 越靠前  action:跳转的路径对应id-->
        <menuitem name="待办事项列表" id="menu_todo_task_list" parent="menu_todo_manager" sequence="1"
                  action="act_todo_task_win"/>
        <menuitem name="组列表" id="menu_todo_category_list" parent="menu_todo_manager" sequence="3"
                  action="act_todo_category_win"/>
    </data>
</odoo>
```











# odoo模块、模型、应用



>模块(module)：是一个odoo应用，包含模型(models)、控制器(controllers)、视图(views)、权限(ir.rule，ir.group, ir.model.access）、初始化数据(data)、报表(report)、向导(wizard)、静态文件(static)等。
>模型(model)：是模块(module）的一部分，是odoo的ORM的描述对象，它的工作是帮我们将内存中的对象反映为数据库中的关系数据。
>复杂的模块可以被定义为应用





# odoo模块间数据传递（目前是同一个应用下的模块）

> 方式：通过数据库 一对多、多对多、多对一

```python
# 模块A
class TodoCategory(models.Model):
    _name = "todo.category"
    _description = "待办事项类别"
    name = fields.Char(string="类别名称", required=True)
    task_ids = fields.One2many(comodel_name="todo.task", inverse_name="category_id", string="待办事项")
```



```python
# 模块B
class TodoTask(models.Model):
    _name = 'todo.task'
    _description = '待办事项详情'

    name = fields.Char(string="事项名称", required=True)
  
    test_field = fields.Char(string="测试字段", compute="_compute_test_field", store=True)
    # test = fields.Char("shifou", required=True)

    @api.depends("category_id")
    def _compute_test_field(self):
        for res in self:
            if(res.category_id == 1):
                res.test_field = "为1"
            else:
                res.test_field = "为2"
```



> A模块的```task_ids```字段和B模块```category_id```字段呈1：n对应模式
>
> 传递数据思路：
>
> ​	A模块更改数据后，B模块通过关联字段访问A模块数据，并跟据数据做出计算得到结果写到自己的数据库中达到持久化
>
> ​		```store=True字段要设置，否则无法写入数据库```









# odoo社区安装版

## pycharm配置

![image-20201031082321417](images/ODOO安装部署/image-20201031082321417.png)

```bash
#Parameters
--config=E:\Code\PyCharm_Code\OSCGODOO13\OSCGODOO13\bin\odoo.conf

#Environment variables
PYTHONUNBUFFERED=1;path=E:\Code\PyCharm_Code\OSCGODOO13\OSCGODOO13\runtime\bin;E:\Code\PyCharm_Code\OSCGODOO13\OSCGODOO13\runtime\python;E:\Code\PyCharm_Code\OSCGODOO13\OSCGODOO13\runtime\pgsql\bin;E:\Code\PyCharm_Code\OSCGODOO13\OSCGODOO13\runtime\win32\nodejs;E:\Code\PyCharm_Code\OSCGODOO13\OSCGODOO13\runtime\win32\wkhtmltopdf;

#workdirectory（不要带source）
E:\Code\PyCharm_Code\OSCGODOO13\OSCGODOO13
```



![image-20201031082402142](images/ODOO安装部署/image-20201031082402142.png)







## odoo规范

![image-20201031110217291](images/ODOO安装部署/image-20201031110217291.png)







## odoo权限

```bash
#这是两个model的权限，不加权限无法操作model 在security中修改
acc_todo_task,todo.task,model_todo_task,base.group_user,1,1,1,1
acc_todo_category,todo.category,model_todo_category,base.group_user,1,1,1,1

```

## odoo菜单排序

![image-20201103192717585](images/ODOO安装部署/image-20201103192717585.png)

```sequence="权重值"``` ---值越大排的位置越靠前