## Sprint 02 - Dataset Preparation & PDF Extraction

### Implemented
- PDF text extraction using PyMuPDF.
- Multi-page PDF support.
- Whitespace normalization.
- PDF file validation.
- Empty document detection.
- Synthetic resume dataset generation.

### Test Results

| Test Case | Result |
|---|---|
| Resume 01 extraction | PASS |
| Resume 02 extraction | PASS |
| Resume 03 extraction | PASS |
| Skill preservation | PASS |
| Invalid file path | PASS |
| Unsupported file format | PASS |
| Empty PDF | PASS |

### Extraction Results

| Resume | Extracted Characters |
|---|---:|
| Resume 01 | 314 |
| Resume 02 | 314 |
| Resume 03 | 339 |

### Limitations
- Scanned PDFs requiring OCR are not supported.
- Complex PDF layouts have not yet been extensively tested.
- Dataset currently contains synthetic examples.

### Technical Decisions
PyMuPDF was selected for PDF text extraction because
it provides a lightweight Python interface and supports
multi-page PDF processing.

Whitespace normalization was implemented without
aggressively removing punctuation or technical terms,
preserving useful information for downstream NLP.
