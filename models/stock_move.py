# -*- coding: utf-8 -*-

from odoo import  _, api, Command, fields, models

class StockMove(models.Model):
    _inherit = "stock.move"

    costo = fields.Float('Costo', store=True)
    
    @api.onchange('product_id','product_uom_qty')
    def _onchange_inglot_product_id(self):
        costo_linea = 0
        if self.product_id:
            costo_linea = self.product_id.standard_price * self.product_uom_qty
        self.costo = costo_linea
            
