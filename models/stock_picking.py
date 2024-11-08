# -*- coding: utf-8 -*-

from odoo import  _, api, Command, fields, models
import logging

class StockPicking(models.Model):
    _inherit = "stock.picking"

    costo_total = fields.Float('Costo total', readonly = True)
    
    def button_validate(self):
        res = super(StockPicking, self).button_validate()
        for albaran in self:
            costo = 0
            if albaran.move_ids_without_package:
                costo_linea = 0
                for linea in albaran.move_ids_without_package:
                    costo_linea = linea.product_id.standard_price * linea.quantity
                    costo += costo_linea
                    linea.costo = costo_linea
                albaran.costo_total = costo
        return res
                
    def _enviar_correo_cantidad_negativa(self):
        productos_negativos = []
        ubicacion_id = self.picking_type_id.default_location_src_id.id
        for linea in self.move_ids_without_package:
            existencia = linea.product_id.with_context({'location' : ubicacion_id}).qty_available
            if (existencia - linea.quantity) < 0:
                productos_negativos.append(linea.product_id.name)

        if len(productos_negativos) > 0:
            productos = ','.join(productos_negativos)
            plantilla = self.env.ref('inglot.mail_template_inglot_producto_negativo')
            valores_correo = {'quant_productos': productos}
            plantilla.with_context(valores_correo).send_mail(self.id, force_send=True)