# -*- coding: utf-8 -*-
{
    "name": "Perfume Inventory",
    "summary": "Practice views (form, search, list)",
    "description": """
    Practice views (form, search, list)
    This is main description from manifest
    """,
    "author": "ERPGO",
    "website": "https://www.erpgo.az/",
    "category": "Inventory",
    "version": "18.0.0.0.0",  # ODOO_VERSION.MAJOR.MINOR.BUGFIX
    "depends": ["base", "sale"],
    "license": "OPL-1",
    "live_test_url": "https://www.youtube.com",
    "price": 9,
    "support": "yashar.heyderov@outlook.com",
    "data": [
        "security/ir.model.access.csv",
        "data/ir_actions_act_window.xml",
        "data/ir_ui_menu.xml",
        "views/perfume_brand.xml",
        "views/perfume_product.xml",
        "views/perfumer_view.xml",
        "views/updated_sale_order.xml",
    ],
    "demo": [
        "demo/accords_demo.xml",
    ],
    "application": True,
    "installable": True,
}
