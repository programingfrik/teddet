
package libteddet;

@:keep
abstract class TDFileType {
    var format:TDFormat;

    public function new(format:TDFormat) {
        this.format = format;
    }

    abstract public function parse_row():TDDataRow;
}