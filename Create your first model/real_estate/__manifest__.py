# -*- coding: utf-8 -*-
{
    'name': "Real Estate",

    'summary': """
        This module includes property model ,a menu and a view""",

    'description': """
        This module includes : \n
	-Model (property) \n
	-Menu & action for property model \n
	-View for property model \n
    """,

    'author': "Ahmed Tarek",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'CRM',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/menus.xml',
    ],
    
}
