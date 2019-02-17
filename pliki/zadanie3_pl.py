import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input file", action="store")
parser.add_argument("-o", "--output", help="output file", action="store")

args = parser.parse_args()

czyste_em = set()
with open(args.input) as f:
    for line in f:
        line = line.strip().lower()
        if line.count("@") == 1:
            czyste_em.add(line)

with open(args.output, 'w') as f:
    for email in czyste_em:
        f.write(email + "\n")

print(czyste_em)
