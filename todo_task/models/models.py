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
    group_emails = fields.Char(string="所在组成员", compute="_compute_group_emails", store=True)

    # test = fields.Char("shifou", required=True)

    @api.depends("category_id")
    def _compute_test_field(self):

        for res in self:

            print(res.create_uid.id)
            print("res.create_uid")
            print(type(res.create_uid))
            print(type(res.category_id))
            print(res.category_id)
            if res.category_id.id == 1:
                res.test_field = "为1"
                print("发邮件了")
                # TodoTask.action.sendMail()
            else:
                res.test_field = "为2"
                # TodoTask.action.sendMail()
                print("发邮件了2222")

    @api.depends("group_emails")
    def _compute_group_emails(self):
        """
        此方法通过create_uid查询到所在组，同时将当前组的组员邮箱地址拼接起来，方便前台获取
        :return:
        """
        for res in self:
            ids = res.create_uid.groups_id.users        # 根据当前这条数据的创建人的所在组下的所有组员
            email_str = ""
            for email in ids:
                print(email.email)
                email_str += email.email + ','          # 将查询到的email邮箱拼接成字符串
            res.group_emails = email_str.strip(',')     # 将邮箱字符串最后一个逗号删除，因为多个收件人中间只能由逗号隔开，而且如果最后一个字符是逗号会发送失败

    @api.depends("deadline")
    def _compute_is_expired(self):
        for res in self:
            if res.deadline:
                res.is_expired = res.deadline < fields.Datetime.now()
            else:
                res.is_expired = False

    def action_send_email(self):

        template_id = self.env.ref('todo_task.test_mail_template')
        print(template_id)
        print(template_id.id)
        # 这里报错
        self.message_post_with_template(template_id.id)

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
