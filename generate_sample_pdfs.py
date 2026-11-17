
import fitz
from pathlib import Path

DATA_DIR = Path("sample_data")

for index in range(1, 4):
    txt_path = DATA_DIR / f"resume_0{index}.txt"
    pdf_path = DATA_DIR / f"resume_0{index}.pdf"

    resume_text = txt_path.read_text(encoding="utf-8")

    document = fitz.open()
    page = document.new_page()

    page.insert_textbox(
        fitz.Rect(50, 50, 545, 790),
        resume_text,
        fontsize=11,
        fontname="helv",
        lineheight=1.5
    )

    document.save(pdf_path)
    document.close()

    print(f"Generated: {pdf_path}")

print("\nAll sample PDFs generated successfully!")
