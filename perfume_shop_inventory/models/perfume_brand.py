# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PerfumeBrand(models.Model):
    _name = 'perfume.brand'
    _description = 'Perfume brand names and related informations'

    name = fields.Char(string='Brand', required=True, )
    country = fields.Char(string='Country', required=True)
    website = fields.Char(string='Website')
    description = fields.Text(string='Description')
