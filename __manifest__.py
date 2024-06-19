# -*- coding: utf-8 -*-
{
    'name': "Inglot",
    'summary': """ Módulo para Inglot """,

    'description': """
        Funcionalidades extras para Inglot
    """,

    'author': "Aquih",
    'website': "http://www.aquih.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'point_of_sale','l10n_gt_extra','pos_gt'],
    'data': [
        'views/pos_payment_method_view.xml',
        'views/pos_order_view.xml',
    ],    
    'assets': {
        'point_of_sale._assets_pos': [
            'inglot/static/src/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'Other OSI approved licence',
}
