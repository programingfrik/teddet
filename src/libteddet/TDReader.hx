
package libteddet;

using sys.io.FileInput;
using haxe.io.Bytes;
using haxe.io.Encoding;

@:keep
class TDReader {

    var subject:FileInput;
    var format:TDFormat;

    var srchunk:Int = 1024; // Size Read Chunk
    var lchunk:Bytes; // Last Chunk
    var strlchunk:String; // Last Chunk but as a String
    var readed:Int = 0; // number of bytes readed in the last chunk

    var upos:Int; // Used Position, up to this position in the chunk the data has been used.
    var tbuff:List<Bytes>; // Temporal Buffer

    var expfin:EReg; // Expresión para encontrar el final

    public function new(subject:FileInput, ?format:TDFormat) {
        trace("New TDReader");
        this.subject = subject;
        this.format = (format == null ?
                       TDFormat.getBaseFormat() : format);
        lchunk = Bytes.alloc(srchunk);
        var vef = (this.format.multiTable ?
                   "|" + this.format.tableDelimiter : "");
        vef = "(" + this.format.rowDelimiter + vef + ")";
        trace('vef = \"$vef\"');
        expfin = new EReg(vef, "g");
    }

    public function read_row():TDDataRow {
        trace("Reading row");
        var textoreg = "";
        var matchend;
        var result = new TDDataRow();

        // Is there some read data that wasn't used the last time a
        // row was ask?
        // if (upos < readed) {
            // If there is, try to extract the row data from that data
            // try to find the end of the row, wich is marked by a
            // rowDelimiter, a tableDelimiter or the end of the file.

        //}

        // If we haven´t found the end of the row read a chunk

        // Try to find the end of the row in that chunk
        upos = 0;
        readed = subject.readBytes(lchunk, 0, srchunk);
        strlchunk = lchunk.getString(0, readed, Encoding.UTF8);
        trace(strlchunk);
        if (expfin.match(strlchunk)) {
            matchend = expfin.matchedPos();
            trace('matched = \"$matchend\"');
            textoreg += strlchunk
                .substr(upos, (matchend.pos + matchend.len) - upos);
            trace('textoreg = \"$textoreg\"');
        }


        trace("eof? " + subject.eof());
        // if (! subject.eof()) {
        //     trace("Reading...");
        //     readed = subject.readBytes(lchunk, 0, srchunk);
        //     trace('$readed bytes readed');
        //     trace(lchunk);
        //     npos += readed;
        // }

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
