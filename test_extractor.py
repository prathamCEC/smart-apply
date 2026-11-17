
from pathlib import Path
import fitz

from src.pdf_extractor import extract_resume_text

DATA_DIR = Path("sample_data")

# Test 1: Extract all three resumes
for index in range(1, 4):
    pdf_path = DATA_DIR / f"resume_0{index}.pdf"

    text = extract_resume_text(pdf_path)

    assert len(text) > 0

    print(f"Resume {index}: Extraction successful")
    print("Characters:", len(text))

# Test 2: Verify important skills survive extraction
resume_01 = extract_resume_text(
    DATA_DIR / "resume_01.pdf"
)

expected_skills = [
    "Python",
    "Java",
    "SQL",
    "Flask",
    "Django"
]

for skill in expected_skills:
    assert skill.lower() in resume_01.lower()

print("\nSkill preservation test: PASSED")

# Test 3: Invalid file path
try:
    extract_resume_text("sample_data/missing.pdf")
    assert False, "Expected FileNotFoundError"

except FileNotFoundError:
    print("Invalid path test: PASSED")

# Test 4: Unsupported file format
try:
    extract_resume_text("sample_data/resume_01.txt")
    assert False, "Expected ValueError"

except ValueError:
    print("Unsupported format test: PASSED")

# Test 5: Empty PDF
empty_pdf = DATA_DIR / "empty_test.pdf"

doc = fitz.open()
doc.new_page()
doc.save(empty_pdf)
doc.close()

try:
    extract_resume_text(empty_pdf)
    assert False, "Expected ValueError"

except ValueError:
    print("Empty PDF test: PASSED")

finally:
    empty_pdf.unlink(missing_ok=True)

print("\nAll extraction tests completed!")
