# models/__init__.py
from . import real_estate_property

# models/real_estate_property.py
from odoo import models, fields

class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    address = fields.Char(string='Address')
    price = fields.Float(string='Price')
    bedrooms = fields.Integer(string='Bedrooms')
    bathrooms = fields.Integer(string='Bathrooms')
    square_feet = fields.Integer(string='Square Feet')
