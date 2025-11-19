def convert(heading):
    p1 = list(heading.split('M')[0])
    h_check = len([item for item in p1 if item == "#"])
    if '#' in p1 and p1[-1] == ' ' and h_check < 6:
        mid = ''.join(list(heading.split('My')[1].split("heading")[0])).strip()
        num = len([item for item in p1 if item == "#"])
        answer = f"<h{num}>My {mid} heading</h{num}>"
    else:
        answer = "Invalid format"
    print(answer)
    return answer
