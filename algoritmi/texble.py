import csv
import sys

filename = sys.argv[1]
args = sys.argv[2:]

struct = []
lens = []

with open(filename) as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            line = [r.strip() for r in row if r.strip()]
            struct.append(line)

            lens.append(list([len(r) for r in line]))
    except csv.Error as e:
        sys.exit('Error: file {}, line {}: {}'.format(filename, reader.line_num, e))

longest = max([len(col) for col in lens]) 
for n, col in enumerate(lens):
    for i in range(len(col), longest):
        struct[n].append("")
        lens[n].append(0)

maxlen = []
if "-t" in args:
    struct = list(zip(*struct))
else:
    lens = [l for l in zip(*lens)]

maxlen = [max(*col) for col in lens]
N = max([len(row) for row in struct])

if "-c" in args:
    c = "c"
elif "-r" in args:
    c = "r"
else:
    c = "l"

indent = ""
if not "-f" in args:
    print("\\begin{table}\n\t\\centering\n\t\\begin{tabular}", end="")
    indent = "\t"
else:
    print("\\begin{tabular}", end="")

if "-v" in args:
    print("{ ", c, " | ", (c + " ") * (N - 1), "}", sep="")
else:
    print("{ ", (c + " ") * N, "}", sep="")

for j, row in enumerate(struct):
    print(indent, "\t", sep="", end="")

    if j == 0 and "-s" not in args:
        print("\\toprule\n", indent, "\t", sep="", end="")

    for n in range(N):
        s = "{{:<{}}}".format(maxlen[n])
        
        if n != N - 1:
            e = " & "
        else:
            e = " "

        try:
            print(s.format(row[n]), end=e)
        except IndexError:
            print(s.format(""), end=e)
    
    print("\\\\\n", end="")

    if j == 0 and "-s" not in args and "-v" not in args:
        print(indent, "\t", "\\midrule", sep="")
    elif j == len(struct) - 1 and "-s" not in args:
        print(indent, "\t", "\\bottomrule", sep="")

if not "-f" in args:
    print("\t\\end{tabular}\n\t\\caption{}\n\t\\label{tab:}\n\\end{table}")
else:
    print("\\end{tabular}")
