from odoo import models, fields, api




class AldKabupaten(models.Model):
    _name = 'ald.kabupaten'
    _description = 'Ald Kabupaten'

    name = fields.Char(string='name')
    deskripsi = fields.Text('deskripsi')
