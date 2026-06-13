
package libteddet;

@:keep
class TDFTDelimited extends TDFileType {

    public function new(format:TDFormat) {
        super(format);
    }

    public function parse_row():TDDataRow {

        return null;
    }

}