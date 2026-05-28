
package libteddet;

import sys.io.File;
import sys.io.FileInput;

@:keep
class TDFormat {

    public static var frmtbase(get, null):TDFormat;

    public static function get_frmtbase() {
        if (frmtbase == null) {
            frmtbase = loadBaseFormat();
        }
        return frmtbase;
    }

    var frmtf:String;
    var frmtfh:FileInput;
    var name:String;
    var description:String;
    var fileType:String;
    var tableHaveHeaders:Bool;
    var delimiter:String;

    var tables:List<Table>;

    var rules:List<ValidationRule>;

    public function new(?frmtf:String) {
        trace("Creando un formato");
        this.frmtf = frmtf;
        // this.frmtfh = File.read(frmtf);
        //
        // try {
        //     this.frmtfh.readLine();
        // } catch(e:haxe.EOF) {
        //
        // }
    }

    static function loadBaseFormat():TDFormat {
        // "formats_format.csv"
        return null;
    }

    function addtable() {

    }
}