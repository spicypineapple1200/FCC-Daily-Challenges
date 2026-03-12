def is_valid_domino_chain(dominoes):
    check = dominoes[0][1]
    ans = True
    for item in dominoes[1:]:
        if item[0] != check: 
            ans = False
            break
        else: pass
        check = item[1]
    print(ans)
    return ans
