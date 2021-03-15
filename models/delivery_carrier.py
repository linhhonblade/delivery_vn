# -*- coding: utf-8 -*-

import logging

from odoo import models, fields, api

class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    @api.model
    def available_carriers(self, partner):
        available_carriers = super(DeliveryCarrier, self).available_carriers(partner)
        # if hasattr(self, 'ahamove_get_avail_services'):
        #     filtered = available_carriers.filtered(lambda r: r.delivery_type != 'ahamove')
        #     ahamove_avail_services_list = getattr(self, 'ahamove_get_avail_services')(partner)
        #     avail_ahamove_carriers = self.env['delivery.carrier'].search([('service_type.code',
        #                                                                    'in',
        #                                                                    ahamove_avail_services_list)])
        #     available_carriers = filtered | avail_ahamove_carriers
        return available_carriers

