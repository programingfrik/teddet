
package libteddet;

@:keep
class TDDataRow {
    var id:Int;
    var frmtTable:TDTable;
    var cells:List<Dynamic>;
    var rtext:String;

    public function new(id:Int, text:String) {
        this.id = id;
        this.rtext = text;
    }

    public function toString() {
        return 'TDDataRow id=$id rtext=\"$rtext\"';
    }
}
