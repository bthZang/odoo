# -*- coding: utf-8 -*-
{
    'name': "Report",
    'sequence': 2,
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'category': 'Human Resource/Report',
    'version': '0.1',
    'depends': ['base', 'staff_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/report_request_my.xml',
        'views/report_request_view.xml',
        'views/views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
