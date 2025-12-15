def title_case(title):
    answer = ' '.join([item.title() for item in title.split(' ')])
    print(answer)
    return answer
