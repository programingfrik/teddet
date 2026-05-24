
package libteddet;

import sys.io.File;
import sys.io.FileInput;

@:keep
class Format {
    var fmtf:String;
    var fmtfh:FileInput;
    var tipoFichero:String;
    var descripcion:String;

    var tablas:Table;
    var reglas:ValidationRule;

    function new(fmtf:String) {
        trace("Creando un formato");
        // this.fmtf = fmtf;
        // this.fmtfh = File.read(fmtf);
        //
        // try {
        //     this.fmtfh.readLine();
        // } catch(e:haxe.EOF) {
        //
        // }
    }

    function addtable() {

    }
}