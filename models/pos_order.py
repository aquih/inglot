# -*- coding: utf-8 -*-
from odoo import api, fields, models
import logging

class PosOrder(models.Model):
    _inherit = 'pos.order'
    
    @api.model
    def _payment_fields(self, order, ui_paymentline):
        res = super(PosOrder, self)._payment_fields(order, ui_paymentline)
        res.update({'numero_autorizacion': ui_paymentline.get('numero_autorizacion')})
        res.update({'cuatro_digitos': ui_paymentline.get('cuatro_digitos')})
        return res