from odoo import models, fields, api






class AldProvnsi(models.Model):
    _name = 'ald.provinsi'
    _description = 'Ald Provnsi'

    name = fields.Char(string='name')
    deskripsi = fields.Text('deskripsi')
   

