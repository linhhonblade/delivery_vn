# -*- coding: utf-8 -*-
{
    'name': "delivery_vn",

    'summary': """
        Vietnam Delivery Methods""",

    'description': """
        A base set-up for Vietname delivery methods
    """,

    'author': "mailovemisa",
    'website': "https://github.com/linhhonblade",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Operations/Inventory/Delivery',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'delivery'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_config_settings_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
}
