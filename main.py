G = {'Python': [10, 10, 10], 'Git': [1], 'Gist': [10]}


def average_grade(grades, courses):
    _sum = sum(G.setdefault(courses))
    _len = len(grades.values())
    avg = _sum / _len
    return avg


print(average_grade(G, 'Python'))
print(len(G.values()))