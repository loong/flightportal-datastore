with open('flightdiary-airlines.csv', 'r') as f:
    lines = f.readlines()
    ids = set()

    for l in lines:
        ids.add(l.split(',')[-1].strip())

    with open('fd-airline-ids.txt', 'w') as w:
        for id in ids:
            w.write(id+"\n")

        w.close()
