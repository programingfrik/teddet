
package libteddet;

import sys.io.File;
import sys.io.FileInput;
import libteddet.TDReader;
import sys.FileSystem;
import haxe.Exception;
import haxe.macro.Format;
import haxe.io.Eof;

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
            frmtbase = loadFormatsFormat();
        }
        return frmtbase;
    }

    public static var basefff:String = "formats_format.csv";

    var frmtf:String;
    var frmtfh:FileInput;
    public var name:String;
    public var description:String;

    public var fileType:TDFileType;

    public var multiTable:Bool;
    public var tablesHaveHeaders:Bool;
    public var fieldDelimiter:String;
    public var rowDelimiter:String;
    public var tableDelimiter:String;
    public var quoteChar:String;
    public var escapeChar:String;

    public var quoting:Quoting;

    public var coding:String;

    public var tables:List<TDTable>;

    public var rules:List<TDValidationRule>;

    public function new(?frmtf:String) {
        trace("New format instance");

        if (frmtf != null) {
            trace('Reading format from $frmtf');
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
    }

    public static function getBaseFormat():TDFormat {
        trace("getBaseFormat");
        var format = new TDFormat();

        format.name = "Base format";
        format.description = "Minimal format with generic default values";
        format.fileType = new TDFTDelimited(format);
        format.multiTable = false;
        format.tablesHaveHeaders = true;
        format.fieldDelimiter = ",";
        format.rowDelimiter = "\r\n";
        format.tableDelimiter = "\n\n";
        format.quoteChar = "\"";
        format.escapeChar = "\\";

        return format;
    }

    public static function loadFormatsFormat():TDFormat {
        trace("loadFormatsFormat");
        var format = getBaseFormat();
        format.name = "Minimal formats_format";
        format.description =
            "Minimal format for reading formats_format";
        format.multiTable = true;

        if (! FileSystem.exists(basefff)) {
            throw new Exception('Error: $basefff doesn\'t exists, '
                                + 'thats a serious thing.');
        }
        var fffh = File.read(basefff);
        var reader = new TDReader(fffh, format);

        // reader

        // var frmtData = reader.read_file();
        return format;
    }

    function addtable() {

    }
}