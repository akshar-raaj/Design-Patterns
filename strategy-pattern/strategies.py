from abc import ABCMeta, abstractmethod


class OCRStrategy(object, metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def perform_ocr(self):
        pass


class TesseractStrategy(OCRStrategy):

    def perform_ocr(self):
        print("Performing OCR using Tesseract")
        pass


class AWSTextractStrategy(OCRStrategy):

    def perform_ocr(self):
        print("Performing OCR using Textract")
        pass


class CloudVisionStrategy(OCRStrategy):

    def perform_ocr(self):
        print("Performing OCR using Cloud Vision")
        pass
