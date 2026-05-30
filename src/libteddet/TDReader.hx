
package libteddet;

using sys.io.FileInput;

@:keep
class TDReader {

    var subject:FileInput;
    var format:TDFormat;

    public function new(subject:FileInput, ?format:TDFormat) {
        this.subject = subject;
        this.format = format;
    }

    public function read_row():TDDataRow {
        var result = new TDDataRow();
        
        return result;
    }

    public function read_table():TDDataTable {
        return null;
    }

    public function read_file():TDDataFile {
        return null;
    }
}
