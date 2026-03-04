def card_values(cards):
    checks, ans = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"], []
    for card in cards:
        if card[0] in "JQK" or "10" in card: ans.append(10)
        else: ans.append(checks.index(card[0])+1)
    print(ans)
    return ans
