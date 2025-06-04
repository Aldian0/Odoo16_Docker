# -*- coding: utf-8 -*-
# from odoo import http


# class AldCoba(http.Controller):
#     @http.route('/ald_coba/ald_coba', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ald_coba/ald_coba/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ald_coba.listing', {
#             'root': '/ald_coba/ald_coba',
#             'objects': http.request.env['ald_coba.ald_coba'].search([]),
#         })

#     @http.route('/ald_coba/ald_coba/objects/<model("ald_coba.ald_coba"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ald_coba.object', {
#             'object': obj
#         })
