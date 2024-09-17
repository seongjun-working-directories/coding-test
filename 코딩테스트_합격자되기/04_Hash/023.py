'''
[문제 023] - https://programmers.co.kr/learn/courses/30/lessons/42579
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

[제약조건]
- genres[i]는 고유번호가 i인 노래의 장르입니다.
- plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
- genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
- 장르 종류는 100개 미만입니다.
- 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
- 모든 장르는 재생된 횟수가 다릅니다.

[입출력 예]
genres	                                            plays	                    return
["classic", "pop", "classic", "classic", "pop"]	    [500, 600, 150, 800, 2500]	[4, 1, 3, 0]
'''
def solution(genres, plays):
    answer = []
    genre_dict = {}
    play_dict = {}
    
    # 장르별 총 재생 횟수 및 각 곡의 재생 횟수
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in genre_dict:
            genre_dict[genre] = []
            play_dict[genre] = 0
        
        genre_dict[genre].append((i, play))
        play_dict[genre] += play
    
    # 총 재생 횟수가 많은 장르 순으로 정렬
    # play_dict.items() -> dict_items([('classic', 1450), ('pop', 3100)])
    sorted_genres = sorted(play_dict.items(), key=lambda x: x[1], reverse=True)

    # sorted_genres -> [('pop', 3100), ('classic', 1450)]
    # genre_dict.items() -> dict_items([('classic', [(0, 500), (2, 150), (3, 800)]), ('pop', [(1, 600), (4, 2500)])])
    for genre, _ in sorted_genres:
        # 내림차순 재생 횟수 정렬: "먼저" 재생 횟수에 따라 내림차순으로 정렬됩니다. -x[1]로 인해 재생 횟수가 큰 곡이 먼저 오게 됩니다.
        # 오름차순 고유 번호 정렬: 재생 횟수가 동일한 곡들이 있다면, 고유 번호가 작은 곡이 먼저 오게 됩니다. x[0]을 기준으로 오름차순으로 정렬합니다.
        sorted_songs = sorted(genre_dict[genre], key=lambda x: (-x[1], x[0]))
        # [(4, 2500), (1, 600)] -> [(3, 800), (0, 500), (2, 150)]

        # extend는 인자로 들어온 배열을 원소 단위로 분해하여 answer 배열에 삽입
        answer.extend([idx for idx, _ in sorted_songs[:2]])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))