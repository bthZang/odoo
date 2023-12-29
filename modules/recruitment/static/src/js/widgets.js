odoo.define('staff_management.pdf_viewer_widget', function (require) {
    "use strict";

    var core = require('web.core');
    var registry = require('web.field_registry');
    var FieldBinary = require('web.basic_fields').FieldBinary;

    var PdfViewer = FieldBinary.extend({
        init: function () {
            this._super.apply(this, arguments);
            this.fileURL = false;
        },

        start: function () {
            this._super.apply(this, arguments);
            this.fileURL = '/web/content/' + this.recordData.id + '/' + this.name + '?download=true';
            this.$el.html('<iframe style="width:100%;height:100%;" src="' + this.fileURL + '"></iframe>');
        },
    });

    registry.add('pdf_viewer', PdfViewer);

    return PdfViewer;
});
