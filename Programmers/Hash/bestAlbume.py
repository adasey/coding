def solution(genres, plays):
    genres_total = {}
    genres_sum = {}
    reversed_sum = {}
    result = []

    for index, titles in enumerate(zip(genres, plays)):
        if titles[0] in genres_total:
            genres_sum[titles[0]] += titles[1]

            if titles[1] in genres_total[titles[0]]:
                genres_total[titles[0]][titles[1]].append(index)

            else:
                genres_total[titles[0]][titles[1]] = [index]
        else:
            genres_sum[titles[0]] = titles[1]
            genres_total[titles[0]] = {titles[1]: [index]}

    temp = sorted(genres_sum.values())
    
    for a, b in genres_sum.items():
        reversed_sum[b] = a

    two_genres = [reversed_sum[temp.pop()], reversed_sum[temp.pop()]]

    temp_f = genres_total[two_genres[0]]
    temp_t = genres_total[two_genres[1]]

    # if len(genres_total[two_genres[0]][two_music[0][0]]) < 2:
    #     result.append(genres_total[two_genres[0]][two_music[0][0]][0])
    #     result.append(genres_total[two_genres[0]][two_music[0][1]][0])

    # else:
    #     result.extend(genres_total[two_genres[0]][two_music[0][0]])

    # if len(genres_total[two_genres[1]][two_music[1][0]]) < 2:
    #     result.append(genres_total[two_genres[1]][two_music[1][0]][0])
    #     result.append(genres_total[two_genres[1]][two_music[1][1]][0])

    # else:
    #     result.extend(genres_total[two_genres[1]][two_music[0][0]])

    # return result