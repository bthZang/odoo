# -*- coding: utf-8 -*-
{
    'name': "Work management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Hoang Zangg",
    'category': 'Human Resource/Staff Management',
    'version': '0.1',
    'depends': ['staff_management', 'department_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
    ],
}
