import os
from strategies import ExtractTextSimple, ExtractTextPDF, ExtractTextImage


class BaseFile(object):
    def __init__(self, path, extractor):
        self.path = path
        self.extractor = extractor

    def size(self):
        # Find file size using os.stat
        return os.stat(self.path).st_size

    def size_in_kb(self):
        size = self.size() / (1024 * 1024)
        # Round to 2 decimal
        return round(size, 2)

    def read_content(self):
        return self.extractor.read_content()


class TextFile(BaseFile):

    def __init__(self, path):
        super().__init__(path, ExtractTextSimple(path))

    FORMAT = "txt"


class PDFFile(BaseFile):

    def __init__(self, path):
        super().__init__(path, ExtractTextPDF(path))

    FORMAT = "pdf"


class DummyPDFFile(BaseFile):

    def __init__(self, path):
        super().__init__(path, ExtractTextPDF(path))

    FORMAT = "dummy-pdf"


class JPGFile(BaseFile):

    def __init__(self, path):
        super().__init__(path, ExtractTextImage(path))

    FORMAT = "jpg"


class PNGFile(BaseFile):

    def __init__(self, path):
        super().__init__(path, ExtractTextImage(path))

    FORMAT = "png"
