# Ancient Greek Lemmatization and Morpho-Syntactic Data

## Referentials

Lemma are from the *Henry George Liddell, Robert Scott, A Greek-English Lexicon*

## Scores

### POS

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9515   | 0.7776    | 0.7375 | 71235   |
| known-tokens     | 0.9555   | 0.7663    | 0.73   | 66241   |
| unknown-tokens   | 0.8989   | 0.5279    | 0.5096 | 4994    |
| ambiguous-tokens | 0.9244   | 0.7384    | 0.7169 | 35332   |

### Lemma

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9592   | 0.7938    | 0.7904 | 71235   |
| known-tokens     | 0.9704   | 0.8963    | 0.8994 | 66241   |
| unknown-tokens   | 0.8106   | 0.6406    | 0.6321 | 4994    |
| ambiguous-tokens | 0.9272   | 0.5782    | 0.6005 | 22879   |

### Lemma without diacritics

|                  | accuracy | precision | recall | support |
|------------------|----------|-----------|--------|---------|
| all              | 0.9613   | 0.8275    | 0.824  | 71235   |
| known-tokens     | 0.9714   | 0.9185    | 0.9199 | 66241   |
| unknown-tokens   | 0.827    | 0.6787    | 0.672  | 4994    |
| ambiguous-tokens | 0.9301   | 0.6609    | 0.6707 | 21002   |
| unknown-targets  | 0.9497   | 0.8259    | 0.8223 | 51804   |


## Script

1. Run `build.py` to get the "simple" training data
	- **Warning:** default output is NFKD
2. Run `build-normalized.py` to get nfd and nfc data

## Sources

- "Gorman Trees", Vanessa Gorman, University of Nebraska-Lincoln, https://github.com/perseids-publications/gorman-trees, https://doi.org/10.5281/zenodo.3596009
- "Daphne Trees", Francesco Mambrini, https://github.com/perseids-publications/daphne-trees
- "Pedalion Trees", Toon Van Hal et al., https://github.com/perseids-publications/cst-trees
- "Perseus Treebank Data", G. Celano et al., https://github.com/PerseusDL/treebank_data
- "Harrington Trees", J. Matthew Harrington, https://github.com/perseids-publications/harrington-trees.git

### Sources to check

Those are sources I do not know the status of (Gold ? Silver ? Bronze ? Wood ?)

- https://github.com/ezhenrik/sematia-tb
- https://github.com/DigitalHill/treebank-data
- https://github.com/danielrruf/AristarchusTreebank-Lit
- https://github.com/Drewlatimer/student-data
- https://github.com/polinayordanova/Treebank-of-Aphtonius-Progymnasmata

## Licence

### Lemmatization data

Licence are the one from the original repositories. Converted data inherits the

### Script

Mozilla Public Licence

## Statistics

- 1,068,131 tokens,
	- including 115,412 punctuation signs
- 56,133 different sentences

91 chars found


| Char | Count |
| ---- | ----- |
|   | 7743 |
| " | 4219 |
| % | 4 |
| ' | 6745 |
| ( | 704 |
| ) | 702 |
| , | 142218 |
| - | 7085 |
| . | 66860 |
| 0 | 1 |
| 1 | 5727 |
| 2 | 3197 |
| 3 | 1616 |
| 4 | 2 |
| : | 7638 |
| ; | 7268 |
| < | 72 |
| > | 74 |
| ? | 137 |
| [ | 577 |
| ] | 571 |
| j | 3 |
| { | 1 |
| ~ | 38 |
| · | 31204 |
| ʽ | 17 |
| ̀ | 230277 |
| ́ | 1123673 |
| ̄ | 25 |
| ̆ | 8 |
| ̈ | 3682 |
| ̓ | 584276 |
| ̔ | 287290 |
| ͂ | 249187 |
| ͅ | 38177 |
| Α | 24953 |
| Β | 1412 |
| Γ | 1957 |
| Δ | 4253 |
| Ε | 7741 |
| Ζ | 2358 |
| Η | 2125 |
| Θ | 2724 |
| Ι | 4642 |
| Κ | 9669 |
| Λ | 5939 |
| Μ | 6123 |
| Ν | 1777 |
| Ξ | 728 |
| Ο | 3754 |
| Π | 9063 |
| Ρ | 2739 |
| Σ | 6155 |
| Τ | 5237 |
| Υ | 586 |
| Φ | 3391 |
| Χ | 903 |
| Ψ | 34 |
| Ω | 346 |
| α | 957329 |
| β | 53775 |
| γ | 152992 |
| δ | 248067 |
| ε | 880724 |
| ζ | 23108 |
| η | 294280 |
| θ | 112297 |
| ι | 845411 |
| κ | 294851 |
| λ | 281371 |
| μ | 315232 |
| ν | 617318 |
| ξ | 30632 |
| ο | 968199 |
| π | 330404 |
| ρ | 379429 |
| ς | 479697 |
| σ | 271423 |
| τ | 541687 |
| υ | 398026 |
| φ | 81370 |
| χ | 95052 |
| ψ | 8992 |
| ω | 340318 |
| ϝ | 13 |
| — | 388 |
| ‘ | 2 |
| ’ | 5404 |
| “ | 4 |
| † | 74 |
| ⏑ | 4 |

