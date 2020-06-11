import glob
from collections import Counter
import unicodedata

chars = Counter()

for file in glob.glob("data/output/*.tsv"):
	with open(file) as f:
		for line_no, line in enumerate(f):
			if line_no == 0:
				continue
			elif not line.strip():
				continue

			token, form, *_ = line.split("\t")
			chars.update(Counter(token+form))

print(f"{len(chars)} chars found")

for char in sorted(list(chars.keys())):
	print(f"{char}\t{chars[char]}")