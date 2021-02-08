# -*- coding: utf-8 -*-

from odoo import models, fields, api

class dishes_management(models.Model):
    _name = 'dishes_management.dishes_management'
    _description = 'dishes_management.dishes_management'

    dish_name = fields.Char()
    dish_description = fields.Char()
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


