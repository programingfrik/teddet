
package libteddet;

import sys.io.File;
import sys.io.FileInput;
import libteddet.TDReader;
import sys.FileSystem;
import haxe.Exception;
import haxe.macro.Format;
import haxe.io.Eof;

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

    public static var basefff:String = "formats_format.csv";

    var frmtf:String;
    var frmtfh:FileInput;
    var name:String;
    var description:String;

    var fileType:FileType;

    var multiTable:Bool;
    var tablesHaveHeaders:Bool;
    var rowDelimiter:String;
    var tableDelimiter:String;
    var quoteChar:String;
    var escapeChar:String;

    var quoting:Quoting;

    var lineTerminator:String;
    var coding:String;

    var tables:List<TDTable>;

    var rules:List<TDValidationRule>;

    public function new(?frmtf:String) {
        this.frmtf = frmtf;
        this.frmtfh = File.read(frmtf);
        var reader = new TDReader(frmtfh);
        try {
            trace(reader.read_row());
        } catch(e:Eof) {
            trace('Error: $e');
        }
        this.frmtfh.close();
    }

    static function loadBaseFormat():TDFormat {
        var tempfrmt = new TDFormat();

        tempfrmt.name = "Minimal formats_format";
        tempfrmt.description =
            "Minimal format for reading formats_format";
        tempfrmt.fileType = FileType.Delimited;
        tempfrmt.multiTable = true;
        tempfrmt.tablesHaveHeaders = true;
        tempfrmt.rowDelimiter = ",";
        tempfrmt.tableDelimiter = "\n\n";
        tempfrmt.quoteChar = "\"";
        tempfrmt.escapeChar = "\\";
        tempfrmt.lineTerminator = "\n\r";

        if (! FileSystem.exists(basefff)) {
            throw new Exception('Error: $basefff doesn\'t exists, '
                                + 'thats a serious thing.');
        }
        var fffh = File.read(basefff);
        var reader = new TDReader(fffh, tempfrmt);

        var frmtData = reader.read_file();

        return null;
    }

    function addtable() {

    }
}