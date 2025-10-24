from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    company_name = fields.Char("My Company Name", default="ERPGO az");
    custom_report = fields.Html("Create Custom Report");
    show_preview = fields.Boolean("Show Preview", default=False)

    def print_custom_report(self):
        return self.env.ref("qweb_test.custom_header_footer_record").report_action(self)

    def toggle_preview(self):
        self.show_preview = !(self.show_review);