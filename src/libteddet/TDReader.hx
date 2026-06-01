
package libteddet;

using sys.io.FileInput;
using haxe.io.Bytes;

@:keep
class TDReader {

    var subject:FileInput;
    var format:TDFormat;
    var srchunk:Int = 1024; // Size Read Chunk
    var lchunk:Bytes; // Last Chunk
    var npos:Int = 0; // Next Position
    var tbuff:List<Bytes>; // Temporal Buffer

    public function new(subject:FileInput, ?format:TDFormat) {
        this.subject = subject;
        this.format = format;
        lchunk = Bytes.alloc(srchunk);
    }

    public function read_row():TDDataRow {
        var result = new TDDataRow();
        var readed:Int = 0;
        trace("Reading row");

        trace(subject.eof());
        if (! subject.eof()) {
            trace("Reading...");
            readed = subject.readBytes(lchunk, npos, srchunk);
            trace('$readed bytes readed');
            trace(lchunk);
            npos += readed;
        }
        
        return result;
    }

    public function read_table():TDDataTable {
        while (! subject.eof()) {
            read_row();
        }
        return null;
    }

    public function read_file():TDDataFile {
        var dataf = new TDDataFile();
        while (!  subject.eof()) {
            read_table();
        }
        return dataf;
    }
}
