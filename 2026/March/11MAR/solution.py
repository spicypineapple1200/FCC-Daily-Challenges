def convert_words(s):
    ans = " ".join([str(len(word)) for word in s.split(" ")])
    print(ans)
    return ans
