import tempfile,unittest,json
from pathlib import Path
from main import format_json
class FormatterTests(unittest.TestCase):
    def test_format(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"in.json"; out=Path(d)/"out.json"; src.write_text('{"a":1}')
            self.assertEqual(format_json(src,out),{"a":1}); self.assertIn("\n  ",out.read_text())
    def test_existing_output_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"in.json"; out=Path(d)/"out.json"; src.write_text("{}") ; out.write_text("keep")
            with self.assertRaises(FileExistsError): format_json(src,out)
            self.assertEqual(out.read_text(),"keep")
    def test_same_path_refused(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"x.json"; src.write_text('{"a":1}')
            with self.assertRaises(ValueError): format_json(src,src)
if __name__=="__main__": unittest.main()
