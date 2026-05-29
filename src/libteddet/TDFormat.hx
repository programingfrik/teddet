
package libteddet;

import sys.io.File;
import sys.io.FileInput;
import libteddet.TDReader;

enum FileType {
    Delimited;
    FixedWidth;
}

enum Quoting {
    ALL;
    MINIMAL;
    NONNUMERIC;
    NONE;
    NOTNULL;
    STRINGS;
}

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

    var fileType:FileType;

    var multiTable:Bool;
    var tablesHaveHeaders:Bool;
    var delimiter:String;
    var quoteChar:String;
    var escapeChar:String;

    var quoting:Quoting;

    var lineTerminator:String;
    var coding:String;

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
        var tempfrmt = new TDFormat();

        tempfrmt.name = "Minimal formats_format";
        tempfrmt.description = "Minimal format for reading formats_format";
        tempfrmt.fileType = FileType.Delimited;
        tempfrmt.multiTable = true;
        tempfrmt.tablesHaveHeaders = true;
        tempfrmt.delimiter = ",";
        tempfrmt.quoteChar = "\"";
        tempfrmt.escapeChar = "\\";
        tempfrmt.lineTerminator = "\n\r";

        var fffh = File.read("formats_format.csv");
        var reader = new TDReader(fffh, tempfrmt);

        return null;
    }

    function addtable() {

    }
}