qbfile = open("qbdata.txt", "r")
for line in qbfile:
    values = line.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )
qbfile.close()