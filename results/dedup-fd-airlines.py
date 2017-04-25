
with open('flightdiary-airlines.csv', 'r') as f:
    with open('fd-airlines-deduped.csv','a') as tar:
        lines = f.readlines()

        ids = set()
        for l in lines:
            id = l.split(',')[-1]
            
            if id in ids:
                continue

            tar.write(l)
            print id
            ids.add(id)
