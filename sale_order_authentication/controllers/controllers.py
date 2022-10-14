# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderAuthentication(http.Controller):
#     @http.route('/sale_order_authentication/sale_order_authentication', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_authentication/sale_order_authentication/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_authentication.listing', {
#             'root': '/sale_order_authentication/sale_order_authentication',
#             'objects': http.request.env['sale_order_authentication.sale_order_authentication'].search([]),
#         })

#     @http.route('/sale_order_authentication/sale_order_authentication/objects/<model("sale_order_authentication.sale_order_authentication"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_authentication.object', {
#             'object': obj
#         })
