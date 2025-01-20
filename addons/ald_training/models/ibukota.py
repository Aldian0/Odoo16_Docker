from odoo import models, fields, api




class AldIbukota(models.Model):
    _name = 'ald.ibukota'
    _description = 'Ald Ibukota'

    name = fields.Char(string='name')
    description = fields.Text('description')
    
