from email.policy import default
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    policy_number = fields.Char('Nro de Poliza')
    type_partner = fields.Selection([('renewal','Renovacion'), ('new', 'Nuevo')], string='Tipo')
    emission_date = fields.Date(string='Fecha de Emisión')
    due_date = fields.Date(string='Fecha de Vencimiento')
    age = fields.Char('Edad')
    gender = fields.Selection([('male', 'Masculino'), ('female', 'Femenino')],
                              string='Genero')
    rif_ci = fields.Char('RIF/CI')
    security_partner = fields.Many2one('security.partner', string="Aseguradora")

class SecurityPartner(models.Model):
    _name = 'security.partner'
    
    name = fields.Char(string='Aseguradora')