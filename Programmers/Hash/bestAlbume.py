def solution(genres, plays):
    genres_sum = {}
    best_genres = []
    result = []

    fst = 0

    temp_sum, genres_total = list(changeValues(genres, plays))

    for a, b in temp_sum.items():
        if b > fst:
            fst = b

        genres_sum[b] = a

    genres_count = len(genres_sum)

    for a in range(genres_count):
        best_genres.append(genres_sum.pop(max(genres_sum)))

        temp = bigValueIndex(genres_total[best_genres[a]], []).copy()
        
        result.extend(temp)
        
    return result

def changeValues(genres, plays):
    genres_total = {}
    temp_sum = {}

    for index, titles in enumerate(zip(genres, plays)):
        if titles[0] in genres_total:
            temp_sum[titles[0]] += titles[1]

            if titles[1] in genres_total[titles[0]]:
                genres_total[titles[0]][titles[1]].append(index)

            else:
                genres_total[titles[0]][titles[1]] = [index]
        else:
            temp_sum[titles[0]] = titles[1]
            genres_total[titles[0]] = {titles[1]: [index]}

    return temp_sum, genres_total

def bigValueIndex(play, temp):
    try:
        temp.extend(play.pop(max(play))[:2])

    except:
        return temp

    if len(temp) >= 2:
        return temp

    else:
        return bigValueIndex(play, temp)