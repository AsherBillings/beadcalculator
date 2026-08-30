import sys

beads = {}

if not sys.argv[1:]:
    print("Please provide csv file(s) as an argument.")
    sys.exit(1)

for a in sys.argv[1:]:
    with open(a, 'r') as f:
        for x in f:
            bead, count = x.strip().split(",")
            beads[bead] = beads.get(bead, 0) + int(count)

for bead, count in beads.items():
    print(f"{bead}: {count}")