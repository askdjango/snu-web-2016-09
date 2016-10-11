credit_sum = 0
score_sum = 0

alphabet = {
    "A+": 4.3, "a+": 4.3, "A0": 4.0, "a0": 4.0, "A-": 3.7, "a-": 3.7,
    "B+": 3.4, "b+": 3.4, "B0": 3.0, "b0": 3.0, "B-": 2.7, "b-": 2.7,
    "C+": 2.4, "c+": 2.4, "C0": 2.0, "c0": 2.0, "C-": 1.7, "c-": 1.7,
    "D+": 1.4, "d+": 1.4, "D0": 1.0, "d0": 1.0, "D-": 0.7, "d-": 0.7,
    "F": 0, "f": 0
}

while True:
    credit = int(input("몇 학점 짜리?"))
    credit_sum = credit_sum + credit
    score = input("받은 학점? (A+ ~ F)")
    score_sum = score_sum + credit*alphabet[score]
    score_average = score_sum/credit_sum
    if input("끝났어요? (y/n)") == "y":
        print(("총 학점 : {} \n 평점 : {}").format(credit_sum, score_average))
        break

