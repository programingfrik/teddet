
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

    function read_row() {

    }

    function read_table() {

    }

    function read_file() {

    }
}
