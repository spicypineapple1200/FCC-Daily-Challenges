def convert_list_item(markdown):
    answer = ''
    nums = [str(num) for num in range(1, 10)]
    for num in nums:
        start = f"{num}. "
        if start in markdown:
            index = markdown.index(start)
            markdown = markdown[index:].split(start)[-1].strip()
            answer = f"<li>{markdown}</li>"
            break
        else:answer = "Invalid format"
    print(answer)
    return answer
