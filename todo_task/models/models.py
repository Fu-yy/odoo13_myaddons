# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class TodoCategory(models.Model):
    _name = "todo.category"
    _description = "待办事项类别"
    name = fields.Char(string="类别名称", required=True)
    task_ids = fields.One2many(comodel_name="todo.task", inverse_name="category_id", string="待办事项")
    task_count = fields.Integer(string="待办事项个数", compute="_compute_task_count")

    @api.depends("task_ids")
    def _compute_task_count(self):
        for res in self:
            res.task_count = len(res.task_ids)

    def btn_check(self):
        print("点击了")


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = '待办事项详情'
    _inherit = ['mail.thread']

    name = fields.Char(string="事项名称", required=True)
    is_done = fields.Boolean(string="是否完成")
    priority = fields.Selection(string="紧急程度",
                                selection=[("todo", "待办"), ("normal", "普通"), ("urgency", "紧急")],
                                default="todo")
    deadline = fields.Datetime(string="截止时间")
    is_expired = fields.Boolean(string="是否过期", compute="_compute_is_expired")
    category_id = fields.Many2one(string="类别", comodel_name="todo.category")
    test_field = fields.Char(string="测试字段", compute="_compute_test_field", store=True)
    # test = fields.Char("shifou", required=True)

    @api.depends("category_id")
    def _compute_test_field(self):
        for res in self:
            print(type(res.category_id))
            print(res.category_id)
            if(res.category_id == 1):
                res.test_field = "为1"
                print("发邮件了")
                # TodoTask.action.sendMail()
            else:
                res.test_field = "为2"
                # TodoTask.action.sendMail()
                print("发邮件了2222")

    @api.depends("deadline")
    def _compute_is_expired(self):
        for res in self:
            if(res.deadline):
                res.is_expired = res.deadline < fields.Datetime.now()
            else:
                res.is_expired = False

    def action_send_email(self):

        template_id = self.env.ref('todo_task.test_mail_template')
        print(template_id)
        print(template_id.id)
        # 这里报错
        # self.message_post_with_template(template_id.id)




        # self.ensure_one()
        # if not self.head_user.email:
        #     raise UserError('用户%s未设置邮箱，无法发送！' % self.head_user.name)
        # template_id = self.env.ref('todo_task.send_msg_template', raise_if_not_found=False)
        # if template_id:
        #     # 调用了/addons/mail/models/mail_template.py的send_mail()，参数1(res_id)是呈现模板的记录的id,force_send:是否立即发送(否则使用邮件队列)
        #     template_id.sudo().with_context(lang=self.env.context.get('lang')).send_mail(self.id, force_send=True)


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
