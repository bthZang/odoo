# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hr_',
    'version': '1.1',
    'category': 'Human Rsc/Hr_',
    'sequence': 95,
    'summary': 'Centralize employee information',
    'depends': [],
    'data': [
        'views/hrr_view.xml',
        '../../addons/hr_recruitment_/views/recruitment_view.xml',
        '../../addons/hr_timekeeping_/views/timekeeping_view.xml',
        '../../addons/hr_staff_/views/staff_view.xml'

            ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
