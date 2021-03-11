# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Company(models.Model):
    _inherit = 'res.company'
    district_id = fields.Many2one('res.country.district', compute='_compute_address',
                                  inverse='_inverse_district')
    ward_id = fields.Many2one('res.country.ward', compute='_compute_address',
                              inverse='_inverse_ward')
    # country_id = fields.Many2one('res.country', compute='_compute_address',
    #                              inverse='_inverse_country', string="Country", store=True)

    def _get_company_address_field_names(self):
        return ['street', 'street2', 'city', 'zip', 'state_id', 'country_id', 'district_id',
                'ward_id']

    def _inverse_district(self):
        for company in self:
            company.partner_id.district_id = company.district_id

    def _inverse_ward(self):
        for company in self:
            company.partner_id.ward_id = company.ward_id

    @api.onchange('district_id')
    def _onchange_district(self):
        if self.district_id.state_id:
            self.state_id = self.district_id.state_id
