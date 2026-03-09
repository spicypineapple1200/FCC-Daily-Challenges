def get_element_size(window_size, element_vw, element_vh):
    window_size = window_size.split(" ")
    element_vw = int(element_vw.split("v")[0])/100
    element_vh = int(element_vh.split("v")[0])/100

    part1 = int(float(window_size[0])*float(element_vw))
    part2 = int(float(window_size[2])*float(element_vh))

    ans = f"{part1} x {part2}"
    print(ans)
    return ans
