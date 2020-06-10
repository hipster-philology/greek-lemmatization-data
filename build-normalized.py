from greek_normalisation.utils import nfd, nfc
import glob
import os

os.makedirs("data/normalized-nfc", exist_ok=True)
os.makedirs("data/normalized-nfd", exist_ok=True)

for file in glob.glob("data/output/*.tsv"):
	basename = file.split("/")[-1]
	out_nfd = open(f"data/normalized-nfd/{basename}", "w")
	out_nfc = open(f"data/normalized-nfc/{basename}", "w")

	def w(line): 
		out_nfd.write(line)
		out_nfc.write(line)

	with open(file) as f:
		for line_no, line in enumerate(f):
			if line == 0:
				w(line)
			elif not line.strip():  # Sentence boundary
				w(line)
			else:
				out_nfc.write(nfc(line))
				out_nfd.write(nfd(line))