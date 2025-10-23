from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def print_custom_report(self):
        return self.env.ref("qweb_test.custom_header_footer_record").report_action(self)