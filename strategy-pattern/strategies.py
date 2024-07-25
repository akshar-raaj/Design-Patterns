import pypdf

from abc import ABCMeta, abstractmethod

from PIL import Image
from pytesseract import pytesseract


class ExtractText(object, metaclass=ABCMeta):

    def __init__(self, path):
        self.path = path

    @abstractmethod
    def read_content(self):
        pass


class ExtractTextSimple(ExtractText):

    def read_content(self):
        with open(self.path, "r") as f:
            return f.read()


class ExtractTextPDF(ExtractText):

    def read_content(self):
        text = ''
        with open(self.path, "rb") as f:
            reader = pypdf.PdfReader(f)
            first_page = reader.pages[0]
            text = first_page.extract_text()
        return text


class ExtractTextImage(ExtractText):

    def read_content(self):
        path_to_tesseract = "/usr/local/bin/tesseract"

        img = Image.open(self.path)

        pytesseract.tesseract_cmd = path_to_tesseract 

        text = pytesseract.image_to_string(img)
        return text
