from sys import argv

filename = argv[1]

input_file = open(filename)

rest_rate = {}

def make_dict():
    for line in input_file:
        line = line.rstrip()
        entry = line.split(':')

        rest_rate[entry[0]] = entry[1]

        sorted_rest_rate_list = sorted(rest_rate)
    
    return sorted_rest_rate_list

sorted_rest_list = []

def make_sorted_rest_list():
    sorted_rest_list = sorted(rest_rate)
    return sorted_rest_list

def create_rest_report(sorted_rest_list):
    for restaurant in sorted_rest_list:
        print "Restaurant %s is rated at %s. \n" % (restaurant, rest_rate[restaurant]),


def main():

    make_dict()

    sorted_rest_list = make_sorted_rest_list()

    create_rest_report(sorted_rest_list)


if __name__ == "__main__":
    main()