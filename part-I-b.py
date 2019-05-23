def get_list_of_seq(filename):
    with open(filename, 'r') as file:
        list_of_seq = file.readlines()
    return list_of_seq


def format_list(list_of_orfID):
    formatted_list = []
    for orfID in list_of_orfID:
        if orfID[0] == "E":
            spliced_ID = orfID[0:15]
            formatted_list.append(spliced_ID)
    return formatted_list


def get_CDS_seq(my_formatted_list, filename):
    formatted_set = set(my_formatted_list)
    dict_of_ID_and_seq = {}
    should_print_next = False
    previous_ID = None
    with open(filename, 'r') as file:
        for line in file:
            if should_print_next:
                dict_of_ID_and_seq[previous_ID] = line
            if line[1:16] in formatted_set:
                previous_ID = line[1:16]
                should_print_next = True
            else:
                should_print_next = False
    return dict_of_ID_and_seq


def IsN(input_string):
    if 'N' in input_string:
        return True
    return False


def count_codon_usage(dict_of_ID_and_seq):
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
    for seq in dict_of_ID_and_seq.itervalues():
        i = 0
        while i < len(seq)-3:
            codon = seq[i: i+3]
            if not IsN(codon):
                codons_dict[codon] += 1
            i += 3
    return codons_dict


def calculate_codon_percentage(codons_dictionary):
    total = sum(codons_dictionary.itervalues())
    for codon, count in codons_dictionary.iteritems():
        count /= float(total)
        count *= 100
        codons_dictionary[codon] = count
    print codons_dictionary


# list_of_orfID = get_list_of_seq("CDS_orfID_HS.txt")
# formatted_list = format_list(list_of_orfID)
# dict_of_ID_and_seq = get_CDS_seq(formatted_list, "HS_hg38_CDS_ready.fa")
# codons_dict = count_codon_usage(dict_of_ID_and_seq)



# Dictionary of zebrafish for CDS vs uORF
# CDS_dict = {'CTT': 85328, 'ATG': 156105, 'AAG': 193056, 'AAA': 193134, 'ATC': 142380, 'AAC': 146841, 'ATA': 47928, 'AGG': 66657, 'CCT': 107825, 'ACT': 97193, 'AGC': 116022, 'ACA': 115510, 'AGA': 97656, 'CAT': 71899, 'AAT': 106573, 'ATT': 102042, 'CTG': 237464, 'CTA': 42298, 'CTC': 108433, 'CAC': 95954, 'ACG': 43003, 'CAA': 83620, 'AGT': 92091, 'CAG': 215196, 'CCG': 46311, 'CCC': 75584, 'TAT': 75617, 'GGT': 83628, 'TGT': 75182, 'CGA': 42533, 'CCA': 105446, 'TCT': 113579, 'GAT': 162362, 'CGG': 39909, 'TTT': 112374, 'TGC': 68400, 'GGG': 61824, 'TAG': 2229, 'GGA': 135960, 'TAA': 4289, 'GGC': 101111, 'TAC': 99264, 'TTC': 124903, 'TCG': 32657, 'TTA': 43799, 'TTG': 78886, 'TCC': 95257, 'GAA': 166406, 'TCA': 96036, 'GCA': 104866, 'GTA': 41575, 'GCC': 114322, 'GTC': 90453, 'GCG': 46667, 'GTG': 172573, 'GAG': 278771, 'GTT': 87230, 'GCT': 130280, 'ACC': 97689, 'TGA': 6149, 'GAC': 171440, 'CGT': 42501, 'TGG': 70963, 'CGC': 56569}
# calculate_codon_percentage(CDS_dict)
# uorf_dict_DR = rare_codon_dict = {'CTT': 65119, 'ATG': 98253, 'AAG': 61622, 'AAA': 156498, 'ATC': 51692, 'AAC': 66345, 'ATA': 99977, 'AGG': 38288, 'CCT': 38107, 'ACT': 60692, 'AGC': 47121, 'ACA': 89723, 'AGA': 62984, 'CAT': 74272, 'AAT': 112171, 'ATT': 118730, 'CTG': 65616, 'CTA': 42954, 'CTC': 42665, 'CAC': 54893, 'ACG': 20152, 'CAA': 70542, 'AGT': 63398, 'CAG': 62036, 'CCG': 14956, 'CCC': 25530, 'TAT': 106939, 'GGT': 35788, 'TGT': 104361, 'CGA': 17533, 'CCA': 43868, 'TCT': 68650, 'GAT': 52715, 'CGG': 15173, 'TTT': 180725, 'TGC': 56109, 'GGG': 26338, 'TAG': 46294, 'GGA': 38194, 'TAA': 107810, 'GGC': 26713, 'TAC': 46506, 'TTC': 67078, 'TCG': 18406, 'TTA': 110198, 'TTG': 82075, 'TCC': 37363, 'GAA': 64692, 'TCA': 75722, 'GCA': 53285, 'GTA': 48625, 'GCC': 25952, 'GTC': 37609, 'GCG': 19987, 'GTG': 62579, 'GAG': 43014, 'GTT': 75024, 'GCT': 48925, 'ACC': 33238, 'TGA': 80411, 'GAC': 36313, 'CGT': 21243, 'TGG': 47689, 'CGC': 19217}
# calculate_codon_percentage(uorf_dict_DR)

# Dictionary of Humans for CDS vs uORF
# CDS_dict  = {'CTT': 117260, 'ATG': 191931, 'AAG': 282211, 'AAA': 221418, 'ATC': 176943, 'AAC': 166671, 'ATA': 66263, 'AGG': 104783, 'CCT': 158261, 'ACT': 118734, 'AGC': 177504, 'ACA': 134181, 'AGA': 106599, 'CAT': 98008, 'AAT': 151317, 'ATT': 139314, 'CTG': 350045, 'CTA': 62898, 'CTC': 169782, 'CAC': 134663, 'ACG': 53831, 'CAA': 112010, 'AGT': 111033, 'CAG': 306642, 'CCG': 65910, 'CCC': 180200, 'TAT': 105437, 'GGT': 93695, 'TGT': 94858, 'CGA': 54254, 'CCA': 153584, 'TCT': 136597, 'GAT': 195077, 'CGG': 102954, 'TTT': 150452, 'TGC': 111428, 'GGG': 144702, 'TAG': 3975, 'GGA': 146732, 'TAA': 5205, 'GGC': 199928, 'TAC': 129991, 'TTC': 173452, 'TCG': 41042, 'TTA': 68793, 'TTG': 113937, 'TCC': 157280, 'GAA': 266338, 'TCA': 111746, 'GCA': 141563, 'GTA': 62454, 'GCC': 249642, 'GTC': 124514, 'GCG': 69412, 'GTG': 244086, 'GAG': 358238, 'GTT': 96214, 'GCT': 161619, 'ACC': 164476, 'TGA': 9620, 'GAC': 223042, 'CGT': 40065, 'TGG': 108335, 'CGC': 94081}
# calculate_codon_percentage(CDS_dict)
# uorf_dict_HS = {'CTT': 3269565, 'ATG': 4222505, 'AAG': 3167553, 'AAA': 8125649, 'ATC': 2569563, 'AAC': 3296015, 'ATA': 5089295, 'AGG': 1997852, 'CCT': 1958650, 'ACT': 3034374, 'AGC': 2339899, 'ACA': 4531812, 'AGA': 3239999, 'CAT': 3785864, 'AAT': 5741354, 'ATT': 5987579, 'CTG': 3233807, 'CTA': 2197137, 'CTC': 2137284, 'CAC': 2750611, 'ACG': 907937, 'CAA': 3640707, 'AGT': 3155137, 'CAG': 3166516, 'CCG': 695342, 'CCC': 1345330, 'TAT': 5329234, 'GGT': 1817448, 'TGT': 5056685, 'CGA': 787593, 'CCA': 2340206, 'TCT': 3405435, 'GAT': 2604932, 'CGG': 687438, 'TTT': 9024291, 'TGC': 2787974, 'GGG': 1350114, 'TAG': 2255399, 'GGA': 1918349, 'TAA': 5285913, 'GGC': 1355800, 'TAC': 2360901, 'TTC': 3374315, 'TCG': 824923, 'TTA': 5502705, 'TTG': 4045242, 'TCC': 1896067, 'GAA': 3251855, 'TCA': 3835583, 'GCA': 2705105, 'GTA': 2447388, 'GCC': 1349912, 'GTC': 1869497, 'GCG': 861801, 'GTG': 3047560, 'GAG': 2129679, 'GTT': 3629883, 'GCT': 2403400, 'ACC': 1750182, 'TGA': 3829418, 'GAC': 1787003, 'CGT': 933603, 'TGG': 2474073, 'CGC': 846582}
# calculate_codon_percentage(uorf_dict_HS)
