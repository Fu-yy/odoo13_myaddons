from odoo import fields, models


class TodoTask:
    _inherit = 'todo.task'
    is_available = fields.Boolean("是否可用?")
