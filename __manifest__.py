# -*- coding: utf-8 -*-
{
    'name': "Purchase Request",

    'summary': """
        Provide functionality for requesting purchase orders
        and approving them before purchase orders are created.""",

    'description': "",

    'author': "YDS",
    'website': "www.yds-int.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Purchase',
    'version': '15.0.0.0',
    "license": "AGPL-3",
    'sequence': -10,
    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'product','contacts','purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_request.xml',
        'views/request_order.xml',
    ],
    'application': False,
    'installable': True,
    'autoinstall': False,
}
