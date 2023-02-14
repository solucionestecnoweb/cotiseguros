from email.policy import default
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    policy_number = fields.Char('Nro de Poliza')
    type = fields.Many2one('type.partner', string='Tipo')
    emission_date = fields.Char('Fecha de Emisión')
    due_date = fields.Char('Fecha de Vencimiento')
    age = fields.Char('Edad')
    gender = fields.Selection([('male', 'Masculino'), ('female', 'Femenino')],
                              string='Genero')
    modify_individual_label_policyholder = fields.Char('Modificar etiqueta individual por tomador')
    modify_contact_file_beneficiary = fields.Char('Modificar ficha de contactos por beneficiario')
    rif_ci = fields.Char('RIF/CI')
   
class TypePartner(models.Model):
    _name = 'type.partner' 
    
    type = fields.Char('Tipo')
    