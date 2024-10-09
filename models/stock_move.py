# -*- coding: utf-8 -*-

from odoo import  _, api, Command, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import config, float_compare
import logging

class StockMove(models.Model):
    _inherit = "stock.move"

    costo = fields.Float('Costo', readonly = True)

class StockQuant(models.Model): 
    _inherit = "stock.quant"
    
    @api.constrains("product_id","quantity")
    def revisar_cantidad_negativa(self):
        p = self.env["decimal.precision"].precision_get("Product Unit of Measure")
        for quant in self:
            plantilla = self.env.user.default_pos_id.plantilla_correo_id if self.env.user.default_pos_id else False
            if (plantilla and float_compare(quant.quantity, 0, precision_digits=p) == -1 and quant.location_id.usage == 'internal'):
                valores_correo = {'quant_producto_id': quant.product_id}
                plantilla.with_context(valores_correo).send_mail(self.id, force_send=True)
