from FastQ_converter import convert_to_csv
from io import StringIO

in1 = StringIO(u'@idXXX\nsequenceXXXX\n+\nqualityXXXX\n')
out1 = StringIO(u'"SeqID","sequence","quality"\n"@idXXX","sequenceXXXX","qualityXXXX"\n')

in2 = StringIO(u'X\nY\n+\nZ')
out2 = StringIO(u'"SeqID","sequence","quality"\n')


def test_convert_to_csv():
    result = StringIO()
    convert_to_csv(in1, result)
    assert result.getvalue() == out1.getvalue()


def test_empty_convert_to_csv():
    result = StringIO()
    convert_to_csv(in2, result)
    assert result.getvalue() == out2.getvalue()
