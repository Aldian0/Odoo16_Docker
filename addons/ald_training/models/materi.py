from odoo import models, fields, api








class AldMateri(models.Model):
    _name = 'ald.materi'
    _description = 'Ald Materi'

    name = fields.Char(string='name')
    deskripsi = fields.Text('deskripsi')
