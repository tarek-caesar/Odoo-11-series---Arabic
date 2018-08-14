# -*- coding: utf-8 -*-
{
    'name': "Create your first view",

    

    'description': """
        Create your first view and menu for property model
    """,

    'author': "Ahmed Tarek",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'CRM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/menus.xml',
    ],
}
