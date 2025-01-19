# -*- coding: utf-8 -*-
# from odoo import http


# class AldTraining(http.Controller):
#     @http.route('/ald_training/ald_training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ald_training/ald_training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ald_training.listing', {
#             'root': '/ald_training/ald_training',
#             'objects': http.request.env['ald_training.ald_training'].search([]),
#         })

#     @http.route('/ald_training/ald_training/objects/<model("ald_training.ald_training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ald_training.object', {
#             'object': obj
#         })
