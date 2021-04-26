import math


def median(list_of_values):
    """
    Calculates median of list's values
    :argument: list_of_values
    :param path: None
    :return: Median
    """
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values)/2) # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values)%2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index-1])/2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    """
    Calculates mean of list's values
    :argument: list_of_values
    :param path: None
    :return: Mean
    """
    return sum(list_of_values)/len(list_of_values)


def variance(list_of_values):
    """
    Calculates variance of list's values
    :argument: list_of_values
    :param path: None
    :return: Variance
    """
    average = mean(list_of_values)
    squared_sum = sum([(x - average)**2 for x in list_of_values])
    return squared_sum/(len(list_of_values)-1)


def covariance(first_list_of_values, second_list_of_values):
    """
    Calculates covariance of 2 list's values
    :argument: first_list_of_values, second_list_of_values
    :param path: None
    :return: Covariance
    """
    result = 0
    # Place your code here
    mean1 = mean(first_list_of_values)
    mean2 = mean(second_list_of_values)
    for i in range(len(first_list_of_values)):
        result += ((first_list_of_values[i] - mean1) * (second_list_of_values[i] - mean2))
    return result/(len(first_list_of_values)-1)


def correlation(first_list_of_values, second_list_of_values):
    """
    Calculates correlation of 2 list's values
    :argument: first_list_of_values, second_list_of_values
    :param path: None
    :return: Correlation
    """
    result = 0
    # Place your code here
    deviation_x = math.sqrt(variance(first_list_of_values))
    deviation_y = math.sqrt(variance(second_list_of_values))
    result = covariance(first_list_of_values, second_list_of_values) / (deviation_x * deviation_y)
    return result

