## Overview

This directory has code example for Strategy Pattern.

This pattern is demonstrated using a Document Processing Application.

There can be different document formats, with some being pdf, jpg, png etc. There are different algorithms that can be used to perform OCR operation on these documents. A document format can work with most of the algorithms.

The design goals to be achieved are:
- Extensibility 
- Flexibility

Strategy pattern can aid in such cases to achieve these design goals.

The context classes are defined in `formats.py` and strategies are defined in `strategies.py`.

The UML Class diagram for our example is:

![Strategy Pattern_ Document Processing with OCR strategies](https://github.com/user-attachments/assets/ad2fbfcf-e9aa-4ff0-89b5-61289b2bb0e2)

