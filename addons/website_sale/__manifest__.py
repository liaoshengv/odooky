{
    'name': 'eCommerce',
    'category': 'Website',
    'sequence': 55,
    'summary': 'Sell Your Products Online',
    'website': 'https://www.odoo.com/page/e-commerce',
    'version': '1.0',
    'description': """
Odoo E-Commerce
==================

        """,
    'depends': ['website', 'sale', 'payment', 'website_payment', 'website_portal_sale', 'website_account', 'website_mail', 'website_form', 'rating'],
    'data': [
        'security/ir.model.access.csv',
        'security/website_sale.xml',
        'data/data.xml',
        'data/web_planner_data.xml',
        'views/product_views.xml',
        'views/account_views.xml',
        'views/sale_report_views.xml',
        'views/sale_order_views.xml',
        'views/crm_team_views.xml',
        'views/templates.xml',
        'views/payment_views.xml',
        'views/snippets.xml',
        'views/report_shop_saleorder.xml',
        'views/res_config_view.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
