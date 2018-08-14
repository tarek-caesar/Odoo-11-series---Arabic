# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Property(models.Model):
    _name = 'real_estate.property'

    name = fields.Char()

    address = fields.Text()
