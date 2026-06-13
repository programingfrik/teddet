
package libteddet;

@:keep
class TDFTFixedWidth extends TDFileType {

    public function new(format:TDFormat) {
        super(format);
    }

    public function parse_row():TDDataRow {

        return null;
    }

}