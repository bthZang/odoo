# -*- coding: utf-8 -*-
{
    'name': "Login",
    'sequence': 3,
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Human Resource/Login',
    'version': '0.1',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'qweb': [
        'views/views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
