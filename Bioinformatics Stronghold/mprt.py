"""
Problem
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into

http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following

http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""

import argparse
import time
import json
import urllib.request as url
import re

sample_dataset = """A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args


class Protein:

    def __init__(self, id):
        self.id = id
        self.fasta = self.fetch_protein_fasta(self.id)
        self.header, self.sequence = self.parse_fasta(self.fasta)
        self.n_glycosylation = self.check_for_n_glycosylation(self.sequence)


    def fetch_protein_fasta(self, id):
        uniprot_id = id
        fasta_address = f'https://www.uniprot.org/uniprot/{uniprot_id}.fasta'
        fasta = url.urlopen(fasta_address).read().decode('UTF-8')
        return fasta

    def parse_fasta(self, fasta):
        split_fasta = fasta.split('\n')
        header = split_fasta[0]
        sequence = ''.join(split_fasta[1:])
        return header, sequence

    def check_for_n_glycosylation(self, sequence):
        m = re.finditer(r'N[^P][ST][^P]', sequence)
        positions = []
        if m:
            for match in m:
                positions.append(str(match.start() + 1))
        return positions


if __name__ == '__main__':
    START = time.time()
    args = get_args()

    if args.input_file:
        with open(args.input_file) as f:
            protein_ids = f.read().split('\n')
    else:
        protein_ids = sample_dataset.split('\n')

    final_protein_ids = [prot_id for prot_id in protein_ids if len(prot_id) > 0]

    for protein_id in final_protein_ids:
        protein = Protein(protein_id)
        if len(protein.n_glycosylation) > 0:
            print(protein.id)
            print(' '.join(protein.n_glycosylation))


    print('\nFinished in {} seconds\n'.format(time.time() - START))
