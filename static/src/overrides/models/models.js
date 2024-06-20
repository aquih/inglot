/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { Order, Orderline } from "@point_of_sale/app/store/models";
import { Payment } from "@point_of_sale/app/store/models";
import { omit } from "@web/core/utils/objects";
import {
    formatFloat,
    roundDecimals as round_di,
    roundPrecision as round_pr,
    floatIsZero,
} from "@web/core/utils/numbers";

patch(Orderline.prototype, {
    setup() {
        super.setup(...arguments);

    },
    getDisplayData() {
        const data = super.getDisplayData(...arguments);
        var descuento = 0;
        data.productDefaultCode = this.product.default_code
        if (data.discount > 0){
            var precio_total = (parseFloat(data.unitPrice) / (1-(data.discount/100))) * parseFloat(data.qty)
            descuento = precio_total - parseFloat(data.price)
        }
        data.descuento = round_pr(Math.max(0, descuento), this.pos.currency.rounding);
        return data
    }
    
});


patch(Order.prototype, {
    setup(_defaultObj, options) {
        super.setup(...arguments);

    },
    obtener_total_articulos(lineas){
        var total_articulos = 0;
        lineas.forEach(function (linea) {
            total_articulos += parseFloat(linea.qty);
        });
        return total_articulos
    },
    obtener_subtotal(lineas){
        var subtotal = 0;
        lineas.forEach(function (linea) {
            var precio_unitario_sin_descuento = parseFloat(linea.unitPrice);
            if (linea.discount > 0){
                precio_unitario_sin_descuento = parseFloat(linea.unitPrice) / ( 1 - (linea.discount/100)   );
            }
            var precio_total = precio_unitario_sin_descuento * parseFloat(linea.qty)
            subtotal += precio_total
        });
        return round_pr(Math.max(0, subtotal), this.pos.currency.rounding);
    },
    export_for_printing() {
        return {
            ...super.export_for_printing(...arguments),
            cantidad_articulos: this.obtener_total_articulos(this.orderlines.map((l) => omit(l.getDisplayData(), "internalNote"))),
            subtotal: this.obtener_subtotal(this.orderlines.map((l) => omit(l.getDisplayData(), "internalNote"))),
            descuento: this.obtener_subtotal(this.orderlines.map((l) => omit(l.getDisplayData(), "internalNote"))) - this.get_total_with_tax(),
        };
    }
});

patch(Payment.prototype, {
    setup(obj, options) {
        super.setup(...arguments);
        this.numero_autorizacion = '';
        this.cuatro_digitos = '';
    },

    export_as_JSON(){
        const json = super.export_as_JSON(...arguments);
        json.numero_autorizacion = this.numero_autorizacion;
        json.cuatro_digitos = this.cuatro_digitos;
        return json;
    },

    export_for_printing(){
        const json = super.export_for_printing(...arguments);
        json.numero_autorizacion = this.numero_autorizacion;
        json.cuatro_digitos = this.cuatro_digitos;
        return json;
    },

});