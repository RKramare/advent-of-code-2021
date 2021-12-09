
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [line.strip().split(" | ") for line in file]
        
    return inputs

def get_a(segs):
    output = [seg[1].split(" ") for seg in segs]
    # print(look)
    count = 0
    for seg in output:
        for inner in seg:
            l = len(inner)
            if l == 2 or l == 3 or l == 4 or l == 7:
                count += 1
    return count


def get_235(o):
    return ""

def get_069(o):
    return ""

def check_seg(pattern, output):
    num = ""
    for o in output:
        l = len(o)
        if l == 2: #1
            num += "1"
        elif l == 3: #7
            num += "7"
            return 7
        elif l == 4: #4
            num += "4"
            return 4
        elif l == 7: #8
            num += "8"
            return 8
        elif l == 5: # 2 3 5
            num += get_235(o)
        elif l == 6: # 0 6 9
            num += get_069(o)
            
        


def get_b(segs):
    patterns = []
    outputs = []
    for p, o in segs:
        patterns.append(p.split(" "))
        outputs.append(o.split(" "))
    #print("Pat", pattern, "\nOut:", output)

    

if __name__ == "__main__":
    #segments = get_inputs("inputs/day08")
    segments = get_inputs("test/test08")

    print(segments)
    get_b(segments)
    #print(get_a(segments))
    #print(get_b())