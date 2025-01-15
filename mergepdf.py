from pypdf import PdfWriter
from pypdf import PdfReader     

merge=PdfWriter()

pdf_file=["test1.pdf","test2.pdf","test3.pdf"]
for pdf in pdf_file:
    merge.append(pdf)

merge.write("merged.pdf")
merge.close()
reader=PdfReader("merged.pdf")
for i, page, in enumerate(reader.pages):
     print(f"Text from page {i + 1}:\n{page.extract_text()}\n")