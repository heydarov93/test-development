from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    company_name = fields.Char("My Company Name", default="ERPGO az");
    custom_report = fields.Html("Create Custom Report");
    show_preview = fields.Boolean("Show Preview", default=True)
    gender = fields.Selection([('male', 'Kişibala'),('female', 'Xanım')], default="male")
    advanced_gender = fields.Selection("_get_advanced_genders")
    mushteriler = fields.Many2one(comodel_name="mushteriler")
    ref_field_id = fields.Reference([
        ('mushteriler', 'Mushteri'),
        ('quotation_document', 'Quotation Document'),
        ('payment_transaction', 'Payment Transaction'),
    ])
    related_field_id = fields.Integer(string="Customer Age", related="mushteriler.age")

    binary_field = fields.Binary()
    binary_field_name = fields.Char()
    binary_fields = fields.Many2many("ir.attachment", string="Multi Files Upload")

    def print_custom_report(self):
        return self.env.ref("qweb_test.custom_header_footer_record").report_action(self)

    def toggle_preview(self):
        self.show_preview = not self.show_preview;

    def _get_advanced_genders(self):
        return [('a', 'A'),('b', 'B'), ('c', 'C')];


class Mushteriler(models.Model):
    _name = 'mushteriler'
    name = fields.Char()
    age = fields.Integer()
    # sales = fields.One2many(comodel_name="sale.order")
