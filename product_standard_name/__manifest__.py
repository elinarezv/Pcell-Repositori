# -*- coding: utf-8 -*-
{
    'name': "Product Standard Name",

    'summary': """
        Product""",

    'description': """
        Adds to product field for search standard name
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template_view.xml',
        #'views/templates.xml',
    ],
    'demo': [
    ],
}