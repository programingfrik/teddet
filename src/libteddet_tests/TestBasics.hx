
import utest.Runner;
import utest.ui.Report;
import utest.Assert;
import sys.io.File;

class TestBasics extends utest.Test {

    function test_BasicRead() {
        // "test_data/20260404_0831_donaciones.PCC"
        // Format fmtpagoc = Format("test_data/pagos_ciguacorp.csv");
        // FileInput pago = File.read("test_data/20260404_0831_donaciones.PCC");
        // Reader rdpago = Reader(pago, fmtpagoc);
        // reg = rdpago.read_row();
        // Assert.equals(reg["cuenta"], 1234123412341234);
        Assert.isTrue(true);
    }

    function test_BasicWrite() {
        Assert.equals(5, 5);
    }

    public static function main() {
        var runner = new Runner();
        runner.addCase(new TestBasics());
        Report.create(runner);
        runner.run();
    }
}
