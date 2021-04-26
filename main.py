from statistics import mean, median, variance, correlation
from math import fabs
import csv


def load_data(path):
    """
    Loads data from given path
    :param path: path to csv file
    :return: returns data as dict {name_of_feature: list_of_values}
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        read_header = None
        data = {}
        index_to_column_name = {}
        for row in reader:
            if not read_header:
                # we are at first row with names of columns
                for i, column_name in enumerate(row):  # enumerate generates index together with value
                    data[column_name] = []  # initializing as empty list
                    index_to_column_name[i] = column_name
                read_header = True
            else:
                # need to append values to data lists. We don't know column name, only index.
                for i, value in enumerate(row):
                    current_column_name = index_to_column_name[i]  # reproducing column name
                    data[current_column_name].append(float(value))
    return data


def run_analysis():
    """
    Run analysis on data then prints information
    :param path: None
    :return: None
    """
    file_path = './winequality.csv'
    data = load_data(file_path)

    # first way of printing. Everything casted to string, and spaces put automatically between passed values.
    print('Number of features:', len(data))
    for feature_name, list_of_values in sorted(data.items()):
        # second way of printing. We print single string after format function.
        # Format function fills {} with values passed as arguments. It has nice applications for better printing,
        # like limiting number of digits for floats or other formatting tools.
        print('"{0}". Mean: {1:.2f}, Median: {2:.2f}, Std: {3:.4f}'.format(
            feature_name, mean(list_of_values), median(list_of_values), variance(list_of_values)**0.5))

    # here you should compute correlations. Be careful, pair should be sorted before printing
    keys=data.keys()
    strongest_pair = ("aaa", "bbb")
    high_correlation = -0.9
    weakest_pair = ("aaa", "bbb")
    low_correlation = 0.1
    for key1 in keys:
        for key2 in keys:
            current_correlation = correlation(data[key1], data[key2])

            if current_correlation > high_correlation and key1 is not key2:
                strongest_pair = (key1, key2)
                high_correlation = current_correlation
            elif fabs(current_correlation) < fabs(low_correlation):
                weakest_pair = (key1, key2)
                low_correlation = current_correlation
    strongest_pair = sorted(strongest_pair)
    weakest_pair = sorted(weakest_pair)

    print('The strongest linear relationship is between: "{0}","{1}". '
          'The value is: {2:.4f}'.format(strongest_pair[0], strongest_pair[1], high_correlation))
    print('The weakest linear relationship is between: "{0}","{1}". '
          'The value is: {2:.4f}'.format(weakest_pair[0], weakest_pair[1], low_correlation))  # * converts list to arguments.
    # Line 53 is equivalent to line 48, this is just other way to use list as arguments


if __name__ == '__main__':
    run_analysis()
