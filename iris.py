import urllib2
import csv
from matplotlib import pyplot as plt

# constants for the names of the data fields
SEPAL_LENGTH = 0
SEPAL_WIDTH = 1
PETAL_LENGTH = 2
PETAL_WIDTH = 3
IRIS_CLASS = 4


def compute_avg(data, fields):
    """
    Returns a dictionary of dictionaries, where each dictionary maps a iris class to its average on the corresponding
    field
    :param data: iris data to parse
    :param fields: fields to compute the average on
    :return: dictionary of dictionaries of averages on each field
    """
    avgs = {}

    for field in fields:
        if field not in [0, 1, 2, 3]:
            return False

    for field in fields:
        name_field = field_to_str(field)
        avgs[name_field] = {}

    for row in data:
        if row:
            name_class = row[IRIS_CLASS]
            for field in fields:
                name_field = field_to_str(field)
                if name_class in avgs[name_field]:
                    s = avgs[name_field][name_class][0] + float(row[field])
                    n = avgs[name_field][name_class][1] + 1
                else:
                    s = float(row[field])
                    n = 1
                avgs[name_field][name_class] = [s, n]

    for name_field in avgs:
        for name_class in avgs[name_field]:
            s = avgs[name_field][name_class][0]
            n = avgs[name_field][name_class][1]
            avgs[name_field][name_class] = s / n

    return avgs


def field_to_str(field):
    """
    Returns a string representation of a data field
    :param field: the index of the data field
    :return: a string representation
    """
    if field == SEPAL_LENGTH:
        return "sepal length"
    elif field == SEPAL_WIDTH:
        return "sepal width"
    elif field == PETAL_LENGTH:
        return "petal length"
    elif field == PETAL_WIDTH:
        return "petal width"


def result_to_str(avgs):
    """
    Returns a string representation of the final result
    :param avgs: final result of all averages computed, which is a dictionary of dictionaries
    :return: a string representation of the result
    """
    s = ""
    for name_field in avgs.keys():
        s += "Average " + name_field + ": \n"
        for name_class in avgs[name_field].keys():
            s += name_class + ": " + str(avgs[name_field][name_class]) + "\n"
        s += "\n"
    return s

def main():
    # fetch CSV data from url
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    response = urllib2.urlopen(url)
    iris = csv.reader(response)

    # compute the averages
    fields = [SEPAL_LENGTH, PETAL_LENGTH] # fields to compute average on, sepal length and petal length by default
    avgs = compute_avg(iris, fields)

    # print the result
    result = result_to_str(avgs)
    print result


if __name__ == "__main__":
    main()