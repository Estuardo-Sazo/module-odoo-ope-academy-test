# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Modulo de practica 
    """,

    'author': "Bitsis Dev",
    'website': "http://www.bitsis.gt",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/ope_academy_view.xml',
        'views/templates.xml',
        'views/res_partner_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
