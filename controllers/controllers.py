# -*- coding: utf-8 -*-
# from odoo import http


# class OpeAcademy(http.Controller):
#     @http.route('/ope_academy/ope_academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ope_academy/ope_academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ope_academy.listing', {
#             'root': '/ope_academy/ope_academy',
#             'objects': http.request.env['ope_academy.ope_academy'].search([]),
#         })

#     @http.route('/ope_academy/ope_academy/objects/<model("ope_academy.ope_academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ope_academy.object', {
#             'object': obj
#         })
