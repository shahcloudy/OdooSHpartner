# -*- coding: utf-8 -*-
{
    'name': "make_zip_mandatory",

    'summary': """
        This module makes the zip field required at checkout """,

    'description': """
        This module depends on website_sale, it add the zip field at checkout to the
        list of mandatory fields in website_sale
    """,

    'author': "Cloudypedia",
    'website': "http://www.cloudypedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Addon',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}