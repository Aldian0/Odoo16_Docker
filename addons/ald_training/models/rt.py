from odoo import models, fields, api




class AldRt(models.Model):
    _name = 'ald.rt'
    _description = 'Ald Rt'

    name = fields.Char(string='name')
    deskrispi = fields.Text('deskrispi')
    
