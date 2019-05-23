from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def convert_file_to_list(input_file):
    list_of_means = []
    with open(input_file, 'r') as infile:
        for line in infile:
            split_line = line.strip().split()
            if split_line[1] != "None":
                list_of_means.append(float(split_line[1]))
    return list_of_means


def calculate_z_scores(list_of_means):
    np_list_of_means = np.array(list_of_means)
    return stats.zscore(np_list_of_means)


def plot_zscore(list_of_zscores):
    #sorted_zscores = list_of_zscores.sort()
    plt.hist(list_of_zscores, bins=100, color='pink', edgecolor="black", linewidth="0.5")
    plt.xlabel('Z-scores')
    plt.ylabel('Frequency')
    plt.title('Histogram of Human CDS conservation')
    plt.show()


my_list = convert_file_to_list("HS_CDS_cons.tsv")
list_of_zscores = calculate_z_scores(my_list)
plot_zscore(list_of_zscores)
