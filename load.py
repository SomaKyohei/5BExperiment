def loadData():

    import os

    path = 'loaddata.txt'
    if os.path.isfile(path):
        with open(path) as f:
        loaddata = [s.strip() for s in f.readlines()]
        print(loaddata)

    print(loaddata[1])

    def split_list(l, n):
        for idx in range(0, len(l), n):
            yield l[idx:idx + n]

    result = list(split_list(loaddata, 7))

    Record.setRecord(result)

        
