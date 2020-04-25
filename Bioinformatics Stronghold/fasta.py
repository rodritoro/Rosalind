class Fasta:

    def __init__(self, fasta_string):
        self.fasta_string = fasta_string
        self.fasta_dict = {}
        self.parse_fasta(self.fasta_string)


    def parse_fasta(self, fasta_string):
        lines = [split.strip() for split in fasta_string.split('\n') if len(split.strip()) > 0]

        current_header = ''
        for i, line in enumerate(lines):
            if line.startswith('>'):
                current_header = line
                self.fasta_dict[current_header] = ''
            else:
                self.fasta_dict[current_header] += line


    def __repr__(self):
        repr_string = ''
        for key in self.fasta_dict:
            value = self.fasta_dict[key]
            repr_string += f'{key}\n{value}\n'
        return repr_string


if __name__ == '__main__':

    test_fasta_string = """
    >Rosalind_24
    TCAATGCATGCGGGTCTATATGCAT
    TCAATGCATGCGGGTCTATATGCAT
    >Rosalind_25
    TCAATGCATGCGGGTCTATATGCAT
    TCAATGCATGCGGGTCTATATGCAT
    """

    my_fasta = Fasta(test_fasta_string)
    print(my_fasta)