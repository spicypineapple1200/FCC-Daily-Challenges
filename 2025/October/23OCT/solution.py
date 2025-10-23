def favorite_songs(playlist):
    plays = []
    for item in range(len(playlist)):
        item = playlist[item]["plays"]
        plays.append(item)
    plays.sort()
    song1plays, song2plays = plays[-1], plays[-2]
    song1, song2 = '', ''
    answer = []
    for listing in playlist:
        if listing['plays'] == song1plays:song1 = listing['title']
        elif listing['plays'] == song2plays:song2 = listing['title']
    answer.append(song1)
    answer.append(song2)
    print(answer)
    return answer
