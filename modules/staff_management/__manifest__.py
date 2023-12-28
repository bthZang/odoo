{
    'name': 'Staff Management',
    'version': '1.1',
    'category': 'Human Resource/Staff Management',
    'sequence': 2,
    'summary': 'Centralize employee information',
    'depends': [
        # 'department_management'
    ],
    'data': [
        'views/staff_view.xml',
        'views/email.xml',
        'security/ir.model.access.csv',
        'security/category_security.xml',
        'views/department_view.xml',
        'views/index.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}
