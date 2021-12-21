
def get_inputs(path):
    with open(path, 'r') as file:
        #iea = ['0' if c == '.' else '1' for c in file.readline()]
        iea = file.readline()
        _ = file.readline()
        image = [line.strip() for line in file]

    return iea, image


def print_image(image):
    for l in image:
        print(l)


def pad_image(image):
    padded = []
    for l in image:
        padded.append('.' + l + '.')
    ins = '.' * len(padded[0])
    padded.insert(0, ins)
    padded.append(ins)
    return padded


def get_pixel(image, iea, x, y):
    assert x > 0
    assert y > 0
    assert x < len(image[0]) - 2
    assert y < len(image) - 2

    res = ''
    for row in range(y - 1, y + 2):
        tmp = ''
        for col in range(x - 1, x + 2):
            if image[row][col] == '.':
                tmp += '0'
            else:
                tmp += '1'
        res += tmp
    index = int(res, 2)
    enhanced = iea[index]

    return enhanced


def run_iea(image, iea):
    image = pad_image(image)
    image = pad_image(image)
    image = pad_image(image)
    image = pad_image(image)
    image = pad_image(image)
    image = pad_image(image)
    # print("Before:")
    # print_image(image)

    enhanced_image = []
    for y in range(1, len(image) - 2):
        tmp = ""
        for x in range(1, len(image[0]) - 2):
            tmp += get_pixel(image, iea, x, y)
        enhanced_image.append(tmp)
    
    # print("After:")
    # print_image(enhanced_image)
    
    return enhanced_image


def count_lit(image):
    res = 0
    for row in image:
        res += row.count('#')
    return res


if __name__ == "__main__":
    iea, image = get_inputs("inputs/day20")
    # iea, image = get_inputs("test/test20")


    for i in range(50):
        print(i)
        image = run_iea(image, iea)

    print_image(image)
    print(count_lit(image))


