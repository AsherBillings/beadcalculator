import os
import sys
import pdfplumber

def get_beads_from_pdf(pdf_file):
    curBeads = {}
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[1:]: #Skip the first page (Board layout)
            text = page.extract_text()
            if text:
                for line in text.splitlines():
                    if line == "0 - 0": #Line that indicates the end of the bead list
                        return curBeads
                    bead, count = line.strip().split(" ")
                    curBeads[bead] = curBeads.get(bead, 0) + int(count)
    return curBeads

if not sys.argv[1:]:
    print("Please provide pdf file(s) exported from Beadifier as an argument.")
    sys.exit(1)

for x in sys.argv[1:]:
    if not x.endswith(".pdf"):
        print("File is not a pdf file.")
        sys.exit(1)

beads = {}
for pdf_file in sys.argv[1:]:
    pdf_beads = get_beads_from_pdf(pdf_file)
    for bead, count in pdf_beads.items():
        beads[bead] = beads.get(bead, 0) + count

if not os.path.exists("output"):
    os.mkdir("output")
    
with open("output/output_" + sys.argv[1].replace(".pdf", "") + ".csv", 'w') as f:
    for bead, count in beads.items():
        f.write(f"{bead},{count}\n")
