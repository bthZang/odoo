{
    'name': 'Staff Management',
    'version': '1.1',
    'category': 'Human Resource/Staff Management',
    'sequence': 2,
    'summary': 'Centralize employee information',
    'depends': [
        'department_management',
    ],
    'data': [
        'views/staff_view.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}
