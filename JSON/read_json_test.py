import sys
import json
import pprint


def read_json(fp):
    print(fp)
    try:
        f = open(fp, "r")
        data = f.read()
        jdict = json.loads(data)
    except IOError:
        print "Failed to read JSON Input file. Please check if the file is present"
        sys.exit(-1)
    except ValueError:
        print "Failed to read json data from Input file. Please check if there is any syntax error"
        sys.exit(-1)
    #pprint.pprint(jdict)

    print(jdict.keys())
    #print(type(jdict.keys()))

    for key in jdict.keys():
        print(type(jdict[key]))
        print key
        for i in jdict[key].keys():
            print(type(jdict[key][i]))
            print(i)

    print(type(jdict["quiz"]["sport"]["q1"]["options"]))
    for i in jdict["quiz"]["sport"]["q1"]["options"]:
        print i
    with open('new_data.json', 'w') as fp:
        json.dump(jdict, fp)


if __name__ == '__main__':
    print(sys.argv)
    read_json(sys.argv[1])
