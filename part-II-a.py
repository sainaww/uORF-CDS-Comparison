import numpy as np
import collections
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_bed")
    parser.add_argument("input_wig")
    parser.add_argument("output_bed")
    parser.add_argument("output_mean_conservation")
    args = parser.parse_args()
    return args


def remove_non_chromosomes(filename, output_file):
    with open(filename, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for line in infile:
                if line[0].lower() == 'c':
                    outfile.writelines([line])


def build_dictionary(bed_file):
    """
    builds dictionaryof dictionaries, with keys being chr 1-25, and values start position : stop position
    :param bed_file:
    :return:
    """
    my_dict = collections.defaultdict(dict)
    with open(bed_file, 'r') as infile:
        for line in infile:
            split_line = line.strip().split()
            my_dict[split_line[0]][int(split_line[1])] = int(split_line[2])
    return dict(my_dict)


def convert_wig_scores_to_list(wig_file, my_dict):
    rolling_count = collections.defaultdict(dict)
    final_results = collections.defaultdict(dict)

    with open(wig_file, 'r') as infile:
        chromosome_number = ""
        start_position = 0
        score = None
        for line in infile:
            split_line = line.strip().split(" ")
            if split_line[0] == "fixedStep":
                chromosome_number = split_line[1][6:]
                start_position = int(split_line[2][6:])-1
                score = None
            else:
                score = float(line)

            if chromosome_number in my_dict and start_position in my_dict[chromosome_number]:
                rolling_count[(chromosome_number, start_position)]["value"] = []
                rolling_count[(chromosome_number, start_position)]["stop"] = int(my_dict[chromosome_number][start_position])

            update_rolling_count(rolling_count, score, start_position, final_results)
            start_position +=1
    return final_results
                

def update_rolling_count(rolling_count, score, start_position, final_results):
    keys = list(rolling_count.keys())
    for chr_no_and_start in keys:
        if start_position <= rolling_count[chr_no_and_start]["stop"]:
            rolling_count[chr_no_and_start]["value"].append(score)
        else:
            final_results[chr_no_and_start] = rolling_count[chr_no_and_start]
            del final_results[chr_no_and_start]["stop"]
            final_results[chr_no_and_start]["average"] = compute_average(final_results[chr_no_and_start]["value"])
            del rolling_count[chr_no_and_start]


def compute_average(list_of_scores):
    new_list = filter(None, list_of_scores)
    if len(new_list) != 0:
        return float(sum(new_list)) / float(len(new_list))


def write_to_bed_file(bed_file, final_results, bed_output, step_4_file):
    with open(bed_file, 'r') as infile:
        with open(bed_output, 'w') as outfile:
            with open(step_4_file,'w') as mean_conservation:
                for line in infile:
                    split_line = line.strip().split()
                    try:
                        average = final_results[(split_line[0], int(split_line[1]))]["average"]
                    except KeyError:
                        average = None
                    try:
                        value = final_results[(split_line[0], int(split_line[1]))]["value"]
                    except KeyError:
                        value = []
                    output_line = line + str(average) + str(value)
                    outfile.write(output_line)
                    outfile.write("\n")
                    conservation_line = split_line[3] + "\t" + str(average)
                    mean_conservation.write(conservation_line)
                    mean_conservation.write("\n")

def main():

    # remove_non_chromosomes("uORF_HS.txt.bed", "uORF_HS.bed")
    args = parse_arguments()
    my_dict = build_dictionary(args.input_bed)
    final_results = convert_wig_scores_to_list(args.input_wig, my_dict)
    write_to_bed_file(args.input_bed, final_results, args.output_bed, args.output_mean_conservation)


if __name__ == '__main__':
    main()
