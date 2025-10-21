def solution(genres, plays):
    music = {}
    for i in range(len(genres)):
        if genres[i] not in music:
            music[genres[i]] = plays[i]
        else:
            music[genres[i]] += plays[i]
            
    music = sorted(music.items(), key = lambda x : x[1], reverse = True)
    
    tmp = {}
    for i in music:
        if i[0] in tmp:
            pass
        else:
            tmp[i[0]] = []
    
    answer = []
    for i in music:
        for j in range(len(genres)):
            if i[0] == genres[j]:
                tmp[i[0]].append([plays[j], j])
                
    tmp = tmp.items()
    for i in tmp:
        ans = sorted(i[1], key=lambda x : x[0], reverse=True)
        
        switch = 0
        for j in range(len(ans)):
            answer.append(ans[j][1])
            switch += 1
            if switch == 2:
                break
                
    return answer