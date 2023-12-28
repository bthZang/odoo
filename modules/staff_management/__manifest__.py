{
    'name': 'Staff Management',
    'version': '1.1',
    'category': 'Human Resource/Staff Management',
    'sequence': 2,
    'summary': 'Centralize employee information',
    'depends': [
    ],
    'data': [
        'views/staff_view.xml',
        'views/email.xml',
        'security/ir.model.access.csv',
        'security/category_security.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}
