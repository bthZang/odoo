# -*- coding: utf-8 -*-
{
    'name': "Timekeeping",
    'sequence': 2,
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'category': 'Human Resource/Timekeeping',
    'version': '0.1',
    'depends': ['staff_management', 'department_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
