{
    'name': 'Secuua theme',
    'description': 'Apply Shopify theme to Odoo',
    'version': '1.0',
    'author': 'Bloopark',
    'category': 'Theme/Creative',
    'data': [
        'views/assets.xml',
        'views/layout.xml',
        'views/snippets.xml',
        'views/theme_common_templates.xml',
    ],
    'images': [
        'static/description/seccua.png',
        'static/description/seccua_screenshot.jpg',
    ],
    'depends': ['website', 'website_theme_install'],
}