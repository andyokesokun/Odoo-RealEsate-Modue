# __manifest__.py
{
    'name': 'Real Estate Management',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Manage real estate properties',
    'description': """
    A simple module to manage real estate properties.
    """,
    'author': 'Andrew Okesokun',
    'depends': ['base'],
    'data': [
        'views/real_estate_property_views.xml',
    ],
    'installable': True,
    'application': True,
}

