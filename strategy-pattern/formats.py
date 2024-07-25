import os
import pypdf

from abc import ABCMeta, abstractmethod

from PIL import Image 
from pytesseract import pytesseract 


class BaseFile(object, metaclass=ABCMeta):
    def __init__(self, path):
        self.path = path

    def size(self):
        # Find file size using os.stat
        return os.stat(self.path).st_size

    def size_in_kb(self):
        size = self.size() / (1024 * 1024)
        # Round to 2 decimal
        return round(size, 2)

    @abstractmethod
    def read_content(self):
        pass


class TextFile(BaseFile):

    FORMAT = "txt"

    def read_content(self):
        with open(self.path, "r") as f:
            return f.read()


class PDFFile(BaseFile):

    FORMAT = "pdf"

    def read_content(self):
        text = ''
        with open(self.path, "rb") as f:
            reader = pypdf.PdfReader(f)
            first_page = reader.pages[0]
            text = first_page.extract_text()
        return text


class DummyPDFFile(BaseFile):

    FORMAT = "dummy-pdf"

    def read_content(self):
        text = ''
        with open(self.path, "rb") as f:
            reader = pypdf.PdfReader(f)
            first_page = reader.pages[0]
            text = first_page.extract_text()
        return text


class JPGFile(BaseFile):

    FORMAT = "jpg"

    def read_content(self):
        path_to_tesseract = "/usr/local/bin/tesseract"

        img = Image.open(self.path)

        pytesseract.tesseract_cmd = path_to_tesseract 

        text = pytesseract.image_to_string(img)
        return text


class PNGFile(BaseFile):

    FORMAT = "png"

    def read_content(self):
        path_to_tesseract = "/usr/local/bin/tesseract"

        img = Image.open(self.path)

        pytesseract.tesseract_cmd = path_to_tesseract 

        text = pytesseract.image_to_string(img)
        return text