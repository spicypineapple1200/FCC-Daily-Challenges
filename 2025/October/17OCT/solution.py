def mask(card):
    last4, separator = card[15:], card[4:5]
    answer = f'****{separator}****{separator}****{separator}{last4}'
    print(answer)
    return answer
