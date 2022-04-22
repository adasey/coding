def solution(genres, plays):
    genres_count = {}
    result = ""
    
    for a, b in enumerate(zip(genres, plays)):
        if b[0] in genres_count:
            genres_count[b[0]][a] = b[1]
            
        else:
            genres_count[b[0]] = {a: b[1]}
            
    loved_song = plays.index(max(plays))
    
    for genre, play in genres_count.items():
        if loved_song in play:
            result = genre