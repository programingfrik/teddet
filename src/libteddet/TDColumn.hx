
package libteddet;

enum ColumnType {
    Text;
    Integer;
    Decimal;
    Date;
    Time;
    DateTime;
}

@:keep
class TDColumn {
    var name:String;
    var type:ColumnType;
    var length:Int;
    var precision:Int;
    var fill:String;
    var alignment:String;
    var description:String;
    var block:Int;
}