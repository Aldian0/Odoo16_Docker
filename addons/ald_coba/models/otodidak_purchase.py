from odoo import models, fields

class otodidak_purchase(models.Model):
    _name='otodidak.purchase'

    name=fields.Char(string="Name")
    tanggal=fields.Date(date="Tanggal")
    status=fields.Selection([('draft','Draft'),('approve','Approve'),('done','Done')])
    description=fields.Char(string='Deskripsi')
    