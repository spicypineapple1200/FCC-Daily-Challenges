def image_search(images, term):
    answer = []
    for image in images:
        if term.lower() in image.lower():
            answer.append(image)
    print(answer)
    return answer
