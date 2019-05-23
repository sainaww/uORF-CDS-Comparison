import plot_bar

def get_list_of_seq(filename):
    with open(filename, 'r') as file:
        list_of_seq = file.readlines()
        list_of_seq = list_of_seq[1::2]
    return list_of_seq


def format_list_of_seq(list_of_seq):
    """

    :param list_of_seq:
    :return: removes \n and converts to uppercase
    """
    for i, seq in enumerate(list_of_seq):
        list_of_seq[i] = seq.strip().upper()
    return list_of_seq


def count_rare_codons(formatted_seq):
    codons_dict = {
    'TTT': 0, 'TTC': 0, 'TTA': 0, 'TTG': 0, 'CTT': 0,
    'CTC': 0, 'CTA': 0, 'CTG': 0, 'ATT': 0, 'ATC': 0,
    'ATA': 0, 'ATG': 0, 'GTT': 0, 'GTC': 0, 'GTA': 0,
    'GTG': 0, 'TAT': 0, 'TAC': 0, 'TAA': 0, 'TAG': 0,
    'CAT': 0, 'CAC': 0, 'CAA': 0, 'CAG': 0, 'AAT': 0,
    'AAC': 0, 'AAA': 0, 'AAG': 0, 'GAT': 0, 'GAC': 0,
    'GAA': 0, 'GAG': 0, 'TCT': 0, 'TCC': 0, 'TCA': 0,
    'TCG': 0, 'CCT': 0, 'CCC': 0, 'CCA': 0, 'CCG': 0,
    'ACT': 0, 'ACC': 0, 'ACA': 0, 'ACG': 0, 'GCT': 0,
    'GCC': 0, 'GCA': 0, 'GCG': 0, 'TGT': 0, 'TGC': 0,
    'TGA': 0, 'TGG': 0, 'CGT': 0, 'CGC': 0, 'CGA': 0,
    'CGG': 0, 'AGT': 0, 'AGC': 0, 'AGA': 0, 'AGG': 0,
    'GGT': 0, 'GGC': 0, 'GGA': 0, 'GGG': 0}
    for seq in formatted_seq:
        if seq[11] == "A":
            spliced_seq = seq[11:-10]
        elif seq [11] == "T":
            spliced_seq = seq[10:-10]
        else:
            formatted_seq.remove(seq)
            #print seq
            continue
        #print spliced_seq[:3]
        i = 0
        while i < len(spliced_seq)-2:
            codon = spliced_seq[i: i+3]
            if not IsN(codon):
                codons_dict[codon] += 1
            i += 3
    return codons_dict, formatted_seq


def count_codons(formatted_seq):
    codons_dict = {
    'TTT': 0, 'TTC': 0, 'TTA': 0, 'TTG': 0, 'CTT': 0,
    'CTC': 0, 'CTA': 0, 'CTG': 0, 'ATT': 0, 'ATC': 0,
    'ATA': 0, 'ATG': 0, 'GTT': 0, 'GTC': 0, 'GTA': 0,
    'GTG': 0, 'TAT': 0, 'TAC': 0, 'TAA': 0, 'TAG': 0,
    'CAT': 0, 'CAC': 0, 'CAA': 0, 'CAG': 0, 'AAT': 0,
    'AAC': 0, 'AAA': 0, 'AAG': 0, 'GAT': 0, 'GAC': 0,
    'GAA': 0, 'GAG': 0, 'TCT': 0, 'TCC': 0, 'TCA': 0,
    'TCG': 0, 'CCT': 0, 'CCC': 0, 'CCA': 0, 'CCG': 0,
    'ACT': 0, 'ACC': 0, 'ACA': 0, 'ACG': 0, 'GCT': 0,
    'GCC': 0, 'GCA': 0, 'GCG': 0, 'TGT': 0, 'TGC': 0,
    'TGA': 0, 'TGG': 0, 'CGT': 0, 'CGC': 0, 'CGA': 0,
    'CGG': 0, 'AGT': 0, 'AGC': 0, 'AGA': 0, 'AGG': 0,
    'GGT': 0, 'GGC': 0, 'GGA': 0, 'GGG': 0}
    for seq in formatted_seq:
        spliced_seq = seq[:-21]
        i = 0
        while i < len(spliced_seq)-2:
            codon = spliced_seq[i: i+3]
            if not IsN(codon):
                codons_dict[codon] += 1
            i += 3
    return codons_dict


def IsN(input_string):
    if 'N' in input_string:
        return True
    return False


list_of_seq = get_list_of_seq('FastaHS.fa')
formatted_list_of_seq = format_list_of_seq(list_of_seq)



rare_codon_dict, modified_list_of_seq = count_rare_codons(formatted_list_of_seq)
arbitrary_codon_dict = count_codons(modified_list_of_seq)
plot_bar.plot_bar_diagram(rare_codon_dict,arbitrary_codon_dict)
