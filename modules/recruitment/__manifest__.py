# -*- coding: utf-8 -*-
{
    'name': "Recruitment",
    'sequence': 1,
    'category': 'Human Resource/Recruitment',
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'version': '0.1',
    'depends': ['base', 'staff_management'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/interview_result_wizard.xml',
        'wizards/interview_result_list_wizard.xml',
        'views/applicant_views.xml',
        'views/interview_appointment_views.xml',
        'views/views.xml',
    ],
    'js': ['static/src/js/widgets.js'],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
