from odoo import http
from odoo.http import request
import odoo.addons.website_sale.controllers.main as main
from odoo.addons.portal.controllers.portal import CustomerPortal


class L10nBrWebsiteSale(main.WebsiteSale):

    def _get_mandatory_billing_fields(self):
        res = super(L10nBrWebsiteSale, self)._get_mandatory_billing_fields()
        return res + ["zip"]

    @http.route()
    def address(self, **kw):
        result = super(L10nBrWebsiteSale, self).address(**kw)
        return result
        