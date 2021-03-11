# -*- coding: utf-8 -*-

from odoo import models, fields, api

ADDRESS_FIELDS = ('street', 'street2', 'zip', 'city', 'state_id', 'country_id', 'district_id',
                  'ward_id')

class Partner(models.Model):
    _inherit = 'res.partner'

    district_id = fields.Many2one('res.country.district', string='District', ondelete='restrict',
                                  domain="[('state_id', '=?', state_id)]")
    ward_id = fields.Many2one('res.country.ward', string='Ward', ondelete='restrict',
                              domain="[('district_id', '=?', district_id)]")

    @api.model
    def _address_fields(self):
        return list(ADDRESS_FIELDS)

    def _display_address(self, without_company=False):
        """
                The purpose of this function is to build and return an address formatted accordingly to the
                standards of the country where it belongs.
                :returns: the address formatted in a display that fit its country habits (or the default ones
                    if not country is specified)
                :rtype: string
                """
        address_format = self._get_address_format()
        args = {
            'state_code': self.state_id.code or '',
            'state_name': self.state_id.name or '',
            'country_code': self.country_id.code or '',
            'country_name': self._get_country_name(),
            'company_name': self.commercial_company_name or '',
            'district_name': self.district_id.name or '',
            'ward_name': self.ward_id.name or '',

        }
        for field in self._formatting_address_fields():
            args[field] = getattr(self, field) or ''
        if without_company:
            args['company_name'] = ''
        elif self.commercial_company_name:
            address_format = '%(company_name)s\n' + address_format
        return address_format % args

    def _display_address_depends(self):
        return self._formatting_address_fields() + [
            'country_id.address_format', 'country_id.code', 'country_id.name',
            'company_name', 'state_id.code', 'state_id.name', 'district_id.name', 'ward_id.name',
        ]
