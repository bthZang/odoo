# -*- coding: utf-8 -*-
{
    'name': "Customer service",
    'sequence': 2,
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'category': 'Human Resource/Customer service',
    'version': '0.1',
    'depends': ['base', 'staff_management'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/reply_contact.xml',
        'views/customer_view.xml',
        'views/contact_view.xml',
        'views/views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
