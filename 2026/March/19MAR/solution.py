def invert_matrix(matrix):
    ans = []
    first, second = matrix[0][0], matrix[0][1]
    for item in matrix:
        build = []
        for piece in item:
            if piece == first: build.append(second)
            else: build.append(first)
        ans.append(build)
    print(ans)
    return ans
