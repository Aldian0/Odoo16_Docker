from odoo import models, fields, api




class AldRw(models.Model):
    _name = 'ald.rw'
    _description = 'Ald Rw'


    name = fields.Char(string='name')
    deskripsi = fields.Text('deskripsi')
    
