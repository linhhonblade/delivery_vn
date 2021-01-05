# -*- coding: utf-8 -*-
# from odoo import http


# class DeliveryVn(http.Controller):
#     @http.route('/delivery_vn/delivery_vn/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delivery_vn/delivery_vn/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delivery_vn.listing', {
#             'root': '/delivery_vn/delivery_vn',
#             'objects': http.request.env['delivery_vn.delivery_vn'].search([]),
#         })

#     @http.route('/delivery_vn/delivery_vn/objects/<model("delivery_vn.delivery_vn"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delivery_vn.object', {
#             'object': obj
#         })
