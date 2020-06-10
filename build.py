import glob
import os
import lxml.etree as ET
import string
import logging
# https://github.com/alpheios-project/arethusa-configs/blob/0fb320bcbf1265032af0202ed3592a6ed5ae48e3/configs/arethusa.morph/gr_attributes.json

logging.getLogger(__name__).setLevel(logging.DEBUG)

header = "form\tlemma\tid\t{}\n".format("\t".join([
    "pos",
    "pers",
    "num",
    "tense",
    "mood",
    "voice",
    "gend",
    "case",
    "degree"
]))

AVOID_DUPLICATES = set()
DUPLICATES = 0

GLOBAL_TOKENS = 0 
GLOBAL_PUNC = 0
PUNCTUATION = set(string.punctuation)

def deal_with_xml(xml, basename, projectname):
	with open(f"data/output/{projectname}-{basename}.tsv", "w") as out:
		out.write(header)
		tokens = 0
		punc = 0
		for sentence in xml.xpath("//sentence"):
			tbw_sentence = []
			checked_sentence = []
			temp_tokens = 0
			temp_punc = 0
			for word in sentence.xpath("./word[not(@artificial)]"):
				tbw_sentence.append(
					"\t".join(
						# form="τοίνυν" lemma="τοίνυν" postag="d--------"
						[word.attrib["form"], word.attrib["lemma"], word.attrib.get("id", "?")] + \
						list(word.attrib["postag"])
					)
				)
				if word.attrib["form"] in PUNCTUATION:
					temp_punc += 1
				temp_tokens += 1
				checked_sentence.append(word.attrib["form"])

			checked_sentence = " ".join(checked_sentence)
			# Check duplicates
			if checked_sentence not in AVOID_DUPLICATES:
				out.write("\n".join(tbw_sentence)+"\n")
				out.write("\n") # End of sentence
				tokens += temp_tokens
				punc += temp_punc
				AVOID_DUPLICATES.add(checked_sentence)
			else:
				logging.error(f"Found a duplicate sentence")
		logging.warning(f"{projectname}-{basename}.tsv: {tokens} found, including {punc} punctuation signs, {len(xml.xpath('//sentence'))} sentences")
	return tokens, punc


os.makedirs("data/output", exist_ok=True)

for file in glob.glob("data/source/*/public/xml/**/*.xml", recursive=True):
	with open(file) as f:
		xml = ET.parse(f)
		if xml.getroot().attrib["{http://www.w3.org/XML/1998/namespace}lang"] != "grc":
			logging.debug(f"Ignored {file}") 
			continue
		_, _, projectname, *_, basename = file.split("/")
		tokens, punc = deal_with_xml(xml=xml, basename=basename, projectname=projectname)
		GLOBAL_TOKENS += tokens
		GLOBAL_PUNC += punc

for file in glob.glob("data/source/treebank_data/v2.1/Greek/texts/*.xml", recursive=True):
	with open(file) as f:
		xml = ET.parse(f)
		if xml.getroot().attrib["{http://www.w3.org/XML/1998/namespace}lang"] != "grc":
			logging.debug(f"Ignored {file}") 
			continue
		*_, basename = file.split("/")
		tokens, punc = deal_with_xml(xml=xml, basename=basename, projectname="treebank_data")
		GLOBAL_TOKENS += tokens
		GLOBAL_PUNC += punc

print(f"{GLOBAL_TOKENS} found, including {GLOBAL_PUNC} punctuation signs, {len(AVOID_DUPLICATES)} different sentences")