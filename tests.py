#!/usr/bin/python


def createFiles():
    for i in range(100):
        filename = str(i).zfill(3) + ".pp"
        str_in_file = 'myfile' + str(i).zfill(3)

        with open("sample_class.txt", "rt") as fin:
            with open(filename, "wt") as fout:
                for line in fin:
                    fout.write(line.replace('myfile000', str_in_file))


createFiles()
