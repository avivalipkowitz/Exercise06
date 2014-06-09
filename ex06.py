from sys import argv

filename= argv[1]

input_file= open(filename)

rest_rate={}

def make_dict():
    for line in input_file:
        line= line.rstrip()
        entry = line.split(':')

        rest_rate[entry[0]] = entry[1]
    return rest_rate


def create_rest_report():
    for restaurant, score in rest_rate.iteritems():
        print "Restaurant %s is rated at %s. \n" % (restaurant, score),


def main():

    make_dict()

    create_rest_report()


if __name__== "__main__":
    main()