
package libteddet;

using sys.io.FileInput;
using haxe.io.Bytes;
using haxe.io.Encoding;

@:keep
class TDReader {

    var subject:FileInput;
    var format:TDFormat;

    var srchunk:Int = 5; // Size Read Chunk
    var lchunk:Bytes; // Last Chunk
    var strlchunk:String; // Last Chunk but as a String
    var readed:Int = 0; // number of bytes readed in the last chunk

    var upos:Int = 0; // Used Position, up to this position in the chunk the data has been used.
    var tbuff:List<Bytes>; // Temporal Buffer

    var expend:EReg; // Expresión para encontrar el final

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
        expend = new EReg(vef, "g");
    }

    public function read_row():TDDataRow {
        trace("Reading row");
        var textoreg = "";
        var matchend;
        var result:TDDataRow;
        var quant:Int;
        var endFound = false;

        // Is there some read data that wasn't used the last time a
        // row was ask?
        if (upos < readed) {
            // If there is, try to extract the row data from that data
            // try to find the end of the row, wich is marked by a
            // rowDelimiter, a tableDelimiter or the end of the file.

            if (expend.matchSub(strlchunk, upos)) {
                endFound = true;
                matchend = expend.matchedPos();
                quant = (matchend.pos + matchend.len) - upos;
            }
            else {
                quant = readed - upos;
            }

            textoreg = strlchunk.substr(upos, quant);
            upos += quant;
            trace('textoreg = \"$textoreg\"');
        }

        // If we haven´t found the end of the row read a chunk
        // Try to find the end of the row in that chunk

        while ((!subject.eof()) && (!endFound)) {
            upos = 0;
            readed = subject.readBytes(lchunk, 0, srchunk);
            strlchunk = lchunk.getString(0, readed, Encoding.UTF8);
            trace(strlchunk);

            if (expend.matchSub(strlchunk, upos)) {
                endFound = true;
                matchend = expend.matchedPos();
                trace('matchend = \"$matchend\"');
                quant = (matchend.pos + matchend.len) - upos;
                textoreg += strlchunk.substr(upos, quant);
                upos += quant;
            }
            else {
                textoreg += strlchunk;
            }

            trace('textoreg = \"$textoreg\"');
        }

        result = new TDDataRow(0, textoreg);

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
