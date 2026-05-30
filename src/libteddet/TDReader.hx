
package libteddet;

using sys.io.FileInput;

@:keep
class TDReader {

    var file:FileInput;
    var format:TDFormat;

    public function new(file:FileInput, ?format:TDFormat) {
        this.file = file;
        this.format = format;
    }

    public function read_row():TDDataRow {
        
        return null;
    }

    public function read_table():TDDataTable {
        return null;
    }

    public function read_file():TDDataFile {
        return null;
    }
}
