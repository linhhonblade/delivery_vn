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
    'depends': ['stock', 'delivery', 'base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/res_config_settings_views.xml',
        'views/assets.xml',
        'views/res_partner_views.xml',
        'data/res_country_data.xml',
        'data/res.country.state.csv',
        'data/res.country.district.csv',
        'data/res.country.ward.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
}
