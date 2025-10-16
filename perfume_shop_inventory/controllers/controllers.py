# -*- coding: utf-8 -*-
# from odoo import http


# class TestDevelopment(http.Controller):
#     @http.route('/test_development/test_development', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_development/test_development/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_development.listing', {
#             'root': '/test_development/test_development',
#             'objects': http.request.env['test_development.test_development'].search([]),
#         })

#     @http.route('/test_development/test_development/objects/<model("test_development.test_development"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_development.object', {
#             'object': obj
#         })

