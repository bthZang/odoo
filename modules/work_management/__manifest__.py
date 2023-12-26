{
    'name': 'Work assignment',
    'version': '1.1',
    'category': 'Human Resource/Work assignment',
    'sequence': 2,
    'summary': 'Manage work assignment for employee',
    'depends': [
        'department_management',
        'staff_management',
    ],
    'data': [
        'views/self_work_view.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
