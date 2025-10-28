# -*- coding: utf-8 -*-
{
    'name': "Perfume Inventory",
    'summary': "Practice views (form, search, list)",
    'description': """
Practice views (form, search, list)
    """,
    'author': "ERPGO",
    'website': "https://www.erpgo.az/",
    'category': 'Inventory',
    'version': '18.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_actions_act_window.xml',
        'data/ir_ui_menu.xml',
        'views/perfume_brand.xml',        
    ],
    'application': True,
    'installable': True,
}

