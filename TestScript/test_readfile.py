import json
import sys, os, time
dir = os.path.dirname(__file__)
sys.path.insert(0, dir + '/../')

from Library.FileHelper import FileHelp


class TestFile:

    def test_readExcel(self):
        inst = FileHelp()
        filename = os.path.join(dir, '../Data/Excel/demoexcel.xlsx')
        data = inst.reader_excel(filename, "member")
        for item in data:
            print(item)

    def test_readjson(self):
        read = FileHelp()
        filename = open(os.path.join(dir, '../Data/Files/Employee.js'))
        data = json.load(filename)
        print(data["Contact"])
