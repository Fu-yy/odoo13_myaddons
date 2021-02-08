# -*- coding: utf-8 -*-
# from odoo import http


# class DishesManagement(http.Controller):
#     @http.route('/dishes_management/dishes_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dishes_management/dishes_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dishes_management.listing', {
#             'root': '/dishes_management/dishes_management',
#             'objects': http.request.env['dishes_management.dishes_management'].search([]),
#         })

#     @http.route('/dishes_management/dishes_management/objects/<model("dishes_management.dishes_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dishes_management.object', {
#             'object': obj
#         })
