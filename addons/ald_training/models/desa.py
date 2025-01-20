from odoo import models, fields, api




class AldDesa(models.Model):
    _name = 'ald.desa'
    _description = 'Ald Desa'

    name = fields.Char(string='name')
    description = fields.Text('description')
