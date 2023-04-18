with open("shit.csv", "r") as file:
    data = file.readlines()
    
    proc = {}
    ov = {}

    for l in data[1:]:
        l = l.strip().split(",")
        l[0] = int(l[0])
        l[2] = list(map(int, l[2].strip().split(";")))
        l[1] = int(l[1])
        proc[l[0]] = [l[1], l[2]]

    for key, value in proc.items():
        prev = [0]
        for k in value[1]:
            if k == 0:
                continue
            prev.append(ov[k])
        
        ov[key] = value[0] + max(prev)


    print(ov)
        
    print(max(ov.values()))
