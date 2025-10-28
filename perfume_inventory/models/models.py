# -*- coding: utf-8 -*-
from odoo import fields, models

class PerfumeBrand(models.Model):
    """
    This model represents perfume brands
    e.g Chanel, Xerjoff, Tom Ford
    """
    _name = "perfume.brand"
    _description = 'Perfume Brand'

    name = fields.Char(string = "Perfume Brand")
    country = fields.Char(string = "Country of the Brand")
    description = fields.Text(string = "Overview")
    total_count = fields.Integer(string = "Total Count")
    perfume_ids = fields.One2many(string = "Current Perfume List", comodel_name = "perfume.product", inverse_name = "brand_id")


class PerfumeProduct(models.Model):
    """
    This model represents perfumes
    e.g Bleu de Chanel, More Than Words, Black Orchid
    """
    _name = "perfume.product"
    _description = 'Perfume Product'

    name = fields.Char(string = "Perfume Name")
    brand_id = fields.Many2one(string = "Brand Name", comodel_name = "perfume.brand")
    year = fields.Integer(string = "Launch Year")
    accord_ids = fields.Many2many(string = "Main Accords", comodel_name = "perfume.accords")
    perfumer_ids = fields.Many2many(string = "Perfumer", comodel_name = "perfume.perfumer")
    stock = fields.Integer(string = "Stock size")

class Perfumer(models.Model):
    """
    This model represents perfume creators
    e.g Ernest Beaux, Jacques Polge, Dominique Ropion
    """
    _name="perfume.perfumer"
    _description = 'Perfumer'

    name = fields.Char(string = "Name")
    perfume_ids = fields.Many2many(string = "Fragrances", comodel_name = "perfume.product")

class Accords(models.Model):
    """
    This model represents main accords
    e.g musky, vanilla, sweet
    """
    _name="perfume.accords"
    _description = 'Accords'

    name = fields.Char(string = "Accords")
    perfume_ids = fields.Many2many(string = "Perfumes", comodel_name = "perfume.product")

