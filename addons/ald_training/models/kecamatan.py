from odoo import models, fields, api




class AldKecamatan(models.Model):
    _name = 'ald.kecamatan'
    _description = 'Ald Kecamatan'

    name = fields.Char(string='name')
    deskripsi = fields.Text('deskripsi')
    
