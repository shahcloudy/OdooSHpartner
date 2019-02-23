# -*- coding: utf-8 -*-
from odoo import http

# class /py/myModule(http.Controller):
#     @http.route('//py/my_module//py/my_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//py/my_module//py/my_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/py/my_module.listing', {
#             'root': '//py/my_module//py/my_module',
#             'objects': http.request.env['/py/my_module./py/my_module'].search([]),
#         })

#     @http.route('//py/my_module//py/my_module/objects/<model("/py/my_module./py/my_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/py/my_module.object', {
#             'object': obj
#         })