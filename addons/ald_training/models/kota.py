from odoo import models, fields, api





class ALdkota(models.Model):
    _name = 'ald.kota'
    _description = 'ALdkota'


    name = fields.Char(string='name')
    deskripsi = fields.Text('deskripsi')
    


