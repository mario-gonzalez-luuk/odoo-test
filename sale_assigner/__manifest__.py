# -*- coding: utf-8 -*-
{
    'name': 'Sales Assigner',
    'version': '0.1',
    'category': 'Sales/Employees',
    'sequence': 15,
    'summary': 'Link module for sale and hr_employee modules',
    'description': "",
    'author': "Luuk",
    'website': 'https://www.goluuk.com/',
    'depends': ['base', 'sale', 'sale_management', 'stock', 'hr', 'sale_stock'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/sale_assigner_views.xml',
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}