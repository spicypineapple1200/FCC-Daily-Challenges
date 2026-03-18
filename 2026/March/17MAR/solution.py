def get_milestone(years):
    status = [
        "0-Newlyweds",
        "1-Paper",
        "5-Wood",
        "10-Tin",
        "25-Silver",
        "40-Ruby",
        "50-Gold",
        "60-Diamond",
        "70-Platinum"
        ]
    for item in status:
        num1 = int(item.split("-")[0])
        if item == status[-1]:
            num2 = 1000000
        else: num2 = int(status[status.index(item)+1].split("-")[0])
        if num1 <= years and years <= num2:
            ans = item.split("-")[1]
    print(ans)
    return ans
