# -*- coding: utf-8 -*-

from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_delivery_ahamove = fields.Boolean(string='Integrate Odoo with Ahamove Shipping')
    module_delivery_ghn = fields.Boolean(string='Integrate Odoo with GHN Shipping')
    module_delivery_vtp = fields.Boolean(string='Integrate Odoo with Viettel Post')
