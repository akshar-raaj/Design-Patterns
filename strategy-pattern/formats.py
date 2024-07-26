import os

from abc import ABCMeta, abstractmethod
from strategies import TesseractStrategy, CloudVisionStrategy, AWSTextractStrategy


class BaseDocument(object, metaclass=ABCMeta):
    def __init__(self, path, ocr_strategy=None):
        self.path = path
        self.ocr_strategy = ocr_strategy or TesseractStrategy()

    def size(self):
        # Find file size using os.stat
        return os.stat(self.path).st_size

    def size_in_kb(self):
        size = self.size() / (1024 * 1024)
        # Round to 2 decimal
        return round(size, 2)

    @abstractmethod
    def num_pages(self):
        pass

    def perform_ocr(self):
        # Perform OCR using the set strategy.
        self.ocr_strategy.perform_ocr()


class PDFDocument(BaseDocument):

    FORMAT = "pdf"

    def __init__(self, path, ocr_strategy=None):
        ocr_strategy = ocr_strategy or CloudVisionStrategy()
        super().__init__(path, ocr_strategy)

    def num_pages(self):
        # Find number of pages in the PDF using some PDF library like pypdf
        pass


class JPGDocument(BaseDocument):

    FORMAT = "jpg"

    def __init__(self, path, ocr_strategy=None):
        ocr_strategy = ocr_strategy or CloudVisionStrategy()
        super().__init__(path, ocr_strategy)

    def num_pages(self):
        # JPG images have 1 page
        return 1


class PNGDocument(BaseDocument):

    FORMAT = "png"

    def __init__(self, path, ocr_strategy=None):
        ocr_strategy = ocr_strategy or AWSTextractStrategy()
        super().__init__(path, ocr_strategy)

    def num_pages(self):
        # PNG images have 1 page
        return 1
