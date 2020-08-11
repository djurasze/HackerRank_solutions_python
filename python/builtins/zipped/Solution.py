

if __name__ == '__main__':
    f = open("data.txt", "r")

    students_count, subjects_count = map(int, f.readline().strip().split())
    subject_ratings = [list(map(float, f.readline().strip().split())) for subject in range(subjects_count)]
    print(students_count)
    print(subjects_count)
    print(subject_ratings)
    students_ratings = list(zip(*subject_ratings))
    students_rating_avg = list(map(lambda ratings: sum(ratings)/len(ratings), students_ratings))
    print(students_ratings)
    print(students_rating_avg)
