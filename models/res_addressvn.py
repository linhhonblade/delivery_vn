# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.osv import expression

class CountryState(models.Model):
    _inherit = 'res.country.state'

    district_ids = fields.One2many('res.country.district', 'state_id', string='Districts')

class VnDistrict(models.Model):
    _description = "Vietnam district"
    _name = 'res.country.district'

    state_id = fields.Many2one('res.country.state', string='State', required=True)
    ward_ids = fields.One2many('res.country.ward', 'district_id', string='Wards')
    name = fields.Char(string='District Name', required=True, help='Administrative divisions of a Province. E.g. Quận Hoàng Mai')

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if self.env.context.get('state_id'):
            args = expression.AND([args, [('state_id', '=', self.env.context.get(
                'state_id'))]])
        if operator == 'ilike' and not (name or '').strip():
            domain = []
        else:
            domain = [('name', operator, name)]
        return [
            district_id
            for district_id in self._search(expression.AND([domain, args]), limit=limit,
                                            access_rights_uid=name_get_uid)
        ]

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{}".format(record.name)))
        return result

class VnWard(models.Model):
    _description = "Vietnam ward"
    _name = 'res.country.ward'

    district_id = fields.Many2one('res.country.district', string='Vietnam District', required=True)
    name = fields.Char(string='Ward Name', required=True, help='Administrative divisions of a '
                                                               'District. E.g. Xã Lâm Động')

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if self.env.context.get('district_id'):
            args = expression.AND([args, [('district_id', '=', self.env.context.get(
                'district_id'))]])

        if operator == 'ilike' and not (name or '').strip():
            domain = []
        else:
            domain = [('name', operator, name)]
        return [
            ward
            for ward in self._search(expression.AND([domain, args]),
                                     limit=limit, access_rights_uid=name_get_uid)
        ]

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{}".format(record.name)))
        return result
