from unittest.mock import Mock, patch

from formats import PDFDocument
from strategies import TesseractStrategy


def test_pdf_document():
    document = PDFDocument('dummy.pdf')
    with patch('formats.CloudVisionStrategy.perform_ocr') as mock:
        document.perform_ocr()
        mock.assert_called_once()
    # Change the ocr_strategy at runtime
    document.ocr_strategy = TesseractStrategy()
    with patch('formats.TesseractStrategy.perform_ocr') as mock:
        document.perform_ocr()
        mock.assert_called_once()
