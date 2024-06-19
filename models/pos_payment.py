# -*- coding: utf-8 -*-
from odoo import api, fields, models

class PosPayment(models.Model):
    _inherit = "pos.payment"

    numero_autorizacion = fields.Char('Número de autorización')
    cuatro_digitos = fields.Char('Cuatro digitos')