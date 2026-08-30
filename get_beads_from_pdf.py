import sys
import pdfplumber

def get_beads_from_pdf(pdf_file):
    curBeads = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[1:]: #Skip the first page (Board layout)
            text = page.extract_text()
            if text:
                for line in text.splitlines():
                    if line == "0 - 0": #Line that indicates the end of the bead list
                        return curBeads
                    curBeads.append(line)
    return curBeads

if not sys.argv[1]:
    print("Please provide pdf file(s) exported from Beadifier as an argument.")
    sys.exit(1)

if not sys.argv[1].endswith(".pdf"):
    print("File is not a pdf file.")
    sys.exit(1)

beads = []
beads.extend(get_beads_from_pdf(sys.argv[1]))

with open("output_" + sys.argv[1].replace(".pdf", "") + ".csv", 'w') as f:
    for bead in beads:
        f.write(f"{bead.replace(" ", ",")}\n")
