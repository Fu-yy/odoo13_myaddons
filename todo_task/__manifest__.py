# -*- coding: utf-8 -*-
{
    'name': "todo_task",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/todo_security.xml',
        'security/ir.model.access.csv',
        'views/include_testcss.xml',
        'data/message.xml',
        'data/mail_template.xml',
        'views/include_js.xml',
        'views/include_xmind_js.xml',
        'views/views.xml',
        'views/todo_menu.xml',
        # 'views/templates.xml',
        'views/example_webpage.xml',

        # 'static/src/style/test.css',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        'static/src/xml/load_echarts2.xml',
        'static/src/xml/load_xmind.xml',
    ],
    'application': True,

}
