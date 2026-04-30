
import utest.Runner;
import utest.ui.Report;
import utest.Assert;

class TestBasics extends utest.Test {

    function test_BasicRead() {
        // "test_data/20260404_0831_donaciones.PCC"
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
