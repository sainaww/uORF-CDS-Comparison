def get_codons_from_file(my_excel_file):
    new_list = []
    with open(my_excel_file) as infile:
        lines = infile.readlines()
        for line in lines:
            stripped_line = line.strip().split()
            new_list.append(stripped_line[0])
        for line in lines:
            stripped_line = line.strip().split()
            new_list.append(stripped_line[5])
        for line in lines:
            stripped_line = line.strip().split()
            new_list.append(stripped_line[10])
        for line in lines:
            stripped_line = line.strip().split()
            new_list.append(stripped_line[15])
    return new_list


def write_freq_to_file(codons_list, my_dict, outfile):
    with open(outfile, 'w') as out_file:
        for codon in codons_list:
            codon_with_thiamine = codon.replace("U", "T")
            out_file.write("%s\n" % my_dict[codon_with_thiamine])


HS_CDS_dict = {'CTT': 117260, 'ATG': 191931, 'AAG': 282211, 'AAA': 221418, 'ATC': 176943, 'AAC': 166671, 'ATA': 66263, 'AGG': 104783, 'CCT': 158261, 'ACT': 118734, 'AGC': 177504, 'ACA': 134181, 'AGA': 106599, 'CAT': 98008, 'AAT': 151317, 'ATT': 139314, 'CTG': 350045, 'CTA': 62898, 'CTC': 169782, 'CAC': 134663, 'ACG': 53831, 'CAA': 112010, 'AGT': 111033, 'CAG': 306642, 'CCG': 65910, 'CCC': 180200, 'TAT': 105437, 'GGT': 93695, 'TGT': 94858, 'CGA': 54254, 'CCA': 153584, 'TCT': 136597, 'GAT': 195077, 'CGG': 102954, 'TTT': 150452, 'TGC': 111428, 'GGG': 144702, 'TAG': 3975, 'GGA': 146732, 'TAA': 5205, 'GGC': 199928, 'TAC': 129991, 'TTC': 173452, 'TCG': 41042, 'TTA': 68793, 'TTG': 113937, 'TCC': 157280, 'GAA': 266338, 'TCA': 111746, 'GCA': 141563, 'GTA': 62454, 'GCC': 249642, 'GTC': 124514, 'GCG': 69412, 'GTG': 244086, 'GAG': 358238, 'GTT': 96214, 'GCT': 161619, 'ACC': 164476, 'TGA': 9620, 'GAC': 223042, 'CGT': 40065, 'TGG': 108335, 'CGC': 94081}
codons_list = get_codons_from_file("Codon_Usage.tsv")
write_freq_to_file(codons_list, HS_CDS_dict, 'HS_CDS_codon_usage.tsv')
