import sys
import os
import time

beads = {}

if not sys.argv[1:]:
    print("Please provide csv file(s) as an argument.")
    sys.exit(1)

for x in sys.argv[1:]:
    if not x.endswith(".csv"):
        print("File is not a csv file.")
        sys.exit(1)

for a in sys.argv[1:]:
    with open(a, 'r') as f:
        for x in f:
            bead, count = x.strip().split(",")
            beads[bead] = beads.get(bead, 0) + int(count)

if not os.path.exists("output"):
    os.mkdir("output")

curTime = time.strftime("%Y%m%d-%H%M%S", time.localtime())
with open("output/output_" + curTime + ".csv", 'w') as f:
    for bead, count in beads.items():
        f.write(f"{bead},{count}\n")