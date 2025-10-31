# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import UserError
import time

class PerfumeBrand(models.Model):
    """
    This model represents perfume brands
    e.g Chanel, Xerjoff, Tom Ford
    """
    _name = "perfume.brand"
    _description = 'Perfume Brand'

    name = fields.Char(string = "Perfume Brand")
    logo = fields.Binary()
    logo_name = fields.Char()
    country = fields.Char(string = "Country of the Brand")
    description = fields.Text(string = "Overview")
    total_count = fields.Integer(string = "Total Count of Perfumes", compute = '_count_perfumes')
    perfume_ids = fields.One2many(string = "Current Perfume List", comodel_name = "perfume.product", inverse_name = "brand_id")

    def _count_perfumes(self):
        for record in self:
            record.total_count = len(record.perfume_ids)


class PerfumeProduct(models.Model):
    """
    This model represents perfumes
    e.g Bleu de Chanel, More Than Words, Black Orchid
    """
    _name = "perfume.product"
    _description = 'Perfume Product'

    name = fields.Char(string = "Perfume Name")
    logo = fields.Binary()
    logo_name = fields.Char()
    brand_id = fields.Many2one(string = "Brand Name", comodel_name = "perfume.brand")
    year = fields.Selection(string = "Launch Year", selection="_generate_years")
    gender = fields.Selection(string = "Gender", selection = [('male','Male'), ('female', 'Female'), ('unisex', 'Unisex')])
    accord_ids = fields.Many2many(string = "Main Accords", comodel_name = "perfume.accords")
    perfumer_ids = fields.Many2many(string = "Perfumer", comodel_name = "perfume.perfumer")
    stock = fields.Integer(string = "Stock size")
    currency_id = fields.Many2one(string = "Currency", comodel_name = "res.currency")
    price = fields.Monetary(string = "Price", currency_field = "currency_id")

    def _generate_years(self):
        years_selection = []
        for year in range(fields.Date.today().year, 1499, -1):
            years_selection.append((str(year), str(year)))

        return years_selection

class Perfumer(models.Model):
    """
    This model represents perfume creators
    e.g Ernest Beaux, Jacques Polge, Dominique Ropion
    """
    _name="perfume.perfumer"
    _description = 'Perfumer'

    name = fields.Char(string = "Name")
    avatar = fields.Binary()
    avatar_name = fields.Char()
    perfume_ids = fields.Many2many(string = "Fragrances", comodel_name = "perfume.product")

class Accords(models.Model):
    """
    This model represents main accords
    e.g musky, vanilla, sweet
    """
    _name="perfume.accords"
    _description = 'Accords'

    name = fields.Char(string = "Accord name", required=True)
    color = fields.Char(string = "Accord color", default = "Neutral")
    percentage = fields.Integer(string = "Percentage")
    perfume_ids = fields.Many2many(string = "Perfumes", comodel_name = "perfume.product")
    sale_order_id = fields.Many2one(string = "Sale", comodel_name = "sale.order")

    _sql_constraints = [
        ('unique_accord_name', 'unique(name)', 'Accord already exists!')
    ]

class SaleOrder(models.Model):
    _inherit = "sale.order"

    accord_ids = fields.One2many(string = "Accords", comodel_name = "perfume.accords", inverse_name = "sale_order_id")
    accord_names = fields.Char(string="Accord name", compute="_compute_accord_names")
    accord_colors = fields.Char(string="Accord color", compute="_compute_accord_names")
    accord_percentages = fields.Char(string="Accord percentage", compute="_compute_accord_names")

    @api.depends('accord_ids', 'accord_ids.name', 'accord_ids.color', 'accord_ids.percentage')
    def _compute_accord_names(self):
        for record in self:
            if record.accord_ids:
                record.accord_names = ', '.join(record.accord_ids.mapped('name'))
                record.accord_colors = ', '.join(record.accord_ids.mapped('color'))
                record.accord_percentages = ', '.join(map(lambda perc: str(perc),record.accord_ids.mapped('percentage')))
            else:
                record.accord_names = ''
                record.accord_colors = ''
                record.accord_percentages = ''

    def display_all_accords(self):
        raise UserError("Ishleyirem !!!")

    
