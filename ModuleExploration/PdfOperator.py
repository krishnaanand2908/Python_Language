import PyPDF2
import os
import fontstyle as fnt
print(fnt.apply("Operation Started...", "blue/bold"))
files = os.listdir()
pdfs = []
for file in files:
    if file.endswith(".pdf"):
        pdfs.append(file)
print(fnt.apply("Your folder have these pdf files: ", "cyan/bold"))
for pdf in pdfs:
  print(fnt.apply(f"{pdf}\n", "cyan/bold"))
merger = PyPDF2.PdfMerger()
for pdf in pdfs:
    merger.append(pdf)
merger.write("MergedFile.pdf")
merger.close()
print(fnt.apply("Operation Successfully Completed", "green/bold"))