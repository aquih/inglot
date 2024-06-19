from odoo import api, fields, models, _


class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    numero_autorizacion = fields.Boolean("Numero de autorización")
