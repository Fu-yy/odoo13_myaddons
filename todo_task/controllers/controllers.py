# -*- coding: utf-8 -*-
from myaddons.todo_task.utils.ComplexEncoder import ComplexEncoder
from odoo import http
import json
import psycopg2


class TodoTask(http.Controller):
    @http.route('/todo_task/todo_task/', auth='public')
    def index(self, **kw):

        return "Hello, world"

    @http.route('/example', type='http', auth='public', website=True)
    def render_example_page(self):
        Todo = http.request.env['todo.task']
        todos = Todo.search([])
        print(todos[0].name)
        return http.request.render('todo_task.example_page', {'todos': todos})
        # return json.dumps(todos)

    @http.route('/test', type='http', auth='public')
    def test_search(self, **kwargs):
        """
        参数传递：
            可以在路径中添加参数http://localhost:8069/test?aa=1&bb=2
            此时 所有参数保存在kwargs中，保存格式{'aa': '1', 'bb': '2'}，通过kwargs.get可以获取值

        请求参数：
            type    请求的类型，可以是http或json。
            auth='public'   不登陆也可以可以访问此路径，其他参数为 user none
            auth='public'   不登陆也可以可以访问此路径，其他参数为 user none
                user - 必须是已通过登录认证的用户，才能访问该请求。如果未经过登录直接访问，则会拦截并跳转回odoo登录页面。

                public - 使用公用的认证，可以不经过登录验证直接访问。

                none - 相应的方法总是可用，一般用于框架和认证模块，对应请求没有办法访问数据库或指向数据库的设置。
        函数作用:
            当请求路径时，会返回数据库中的数据
        各个参数：
            conn：
                数据库连接参数
            tables：
                查询结果
        :return:
            json.dumps(tables, cls=ComplexEncoder, ensure_ascii=False)
                cls=ComplexEncoder 对象转换为json时无法转换datetime字段，重写构造json类，遇到日期特殊处理，其余的用内置的就行。
                ensure_ascii=False json转换中文默认会使用ascii码，此处禁用了ascii

        ex:
            return  local_redirect_with_hash('http://www.bing.com')--重定向到bing
        """
        print(kwargs)
        print(kwargs.get('aa'))
        print(kwargs.get('bb'))
        conn = psycopg2.connect(database="admin", user="postgres", password="4117", host="127.0.0.1", port="5432")

        # 查找名叫 test4 的数据库  postgres  是数据库的超级用户名称
        vals = conn.cursor()
        vals.execute("SELECT * FROM todo_task")  # 执行sql语句查询数据
        tables = vals.fetchall()  # 返回查询结果
        print(tables)
        conn.close()
        return json.dumps(tables, cls=ComplexEncoder, ensure_ascii=False)   # cls=ComplexEncoder 对象转换为json时无法转换datatime字段，所以此时

    @http.route('/todo_task/todo_task/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('todo_task.listing', {
            'root': '/todo_task/todo_task',
            'objects': http.request.env['todo.task'].search([]),
        })

    # @http.route('/todo_task/todo_task/objects/<model("todo_task.todo_task"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('todo_task.object', {
    #         'object': obj
    #     })
