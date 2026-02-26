def is_valid_trick(trick_name):
    first = ["Misty", "Ghost", "Thunder", "Solar", "Sky", "Phantom", "Frozen", "Polar"]
    second = ["Twister", "Icequake", "Avalanche", "Vortex", "Snowstorm", "Frostbite", "Blizzard", "Shadow"]
    word = trick_name.split(" ")
    if word[0] in first and word[1] in second:
        ans = True
    else: ans = False
    print(ans)
    return ans
