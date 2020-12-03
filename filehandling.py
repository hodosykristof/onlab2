
def write_to_file(filename, data):
    f = open(filename, "w")
    # find types of timestamps
    # for i in range(0, len(data)):
    #     if data[i][0] == '2':
    #         if data[i] != data[i-1] or i == 0:
    #             f.write(data[i] + '\n')
    #
    #     else:
    #         f.write(data[i] + '\n')

    # write all data into file
    for i in range(0, len(data)):
        f.write(str(data[i]) + '\n')

    f.close()
