
package libteddet;

using sys.io.FileInput;

@:keep
class TDReader {

    var file:FileInput;
    var format:String;

    public function new(file:FileInput, ?format:String) {
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
