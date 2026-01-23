def solution(elements):
    answer = []
    l = len(elements)
    elements = elements + elements #[7, 9, 1, 1, 4,/// 7, 9, 1, 1, 4]
    for i in range(0, l):
        for j in range(1, l+1):
            answer.append(sum(elements[i:i+j]))

    return len(set(answer))