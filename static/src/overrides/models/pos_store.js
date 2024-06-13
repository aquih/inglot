/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";


patch(PosStore.prototype, {
    /**
     * @override
     */
    async setup() {
        await super.setup(...arguments);

    },
    getReceiptHeaderData() {
        const json = super.getReceiptHeaderData(...arguments);
        json.diario_factura_nombre = this.config.diario_factura_nombre;
        json.diario_factura_direccion = this.config.diario_factura_direccion;
        return json;
    },

});
