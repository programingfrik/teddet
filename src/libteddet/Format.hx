
package libteddet;

import sys.io.File;
import sys.io.FileInput;

@:keep
class Format {

    public static var frmtbase(get, null):Format;

    public static function get_frmtbase() {
        if (frmtbase == null) {
            frmtbase = new Format();
        }
        return frmtbase;
    }

    var frmtf:String;
    var frmtfh:FileInput;
    var name:String;
    var description:String;
    var fileType:String;
    var tableHaveHeaders:Bool;

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

    function addtable() {

    }
}