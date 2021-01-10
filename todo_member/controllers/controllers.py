# -*- coding: utf-8 -*-
# from odoo import http


# class TodoMember(http.Controller):
#     @http.route('/todo_member/todo_member/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_member/todo_member/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_member.listing', {
#             'root': '/todo_member/todo_member',
#             'objects': http.request.env['todo_member.todo_member'].search([]),
#         })

#     @http.route('/todo_member/todo_member/objects/<model("todo_member.todo_member"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_member.object', {
#             'object': obj
#         })
