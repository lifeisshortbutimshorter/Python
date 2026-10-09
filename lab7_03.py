passed_count = 0
failed_count = 0
valid_scores = []

for i in range(0, 10):
    student_number = i + 1
    student_score = float(input(f"Student {student_number} score: "))
    
    print("\nStudent {}: ".format(student_number))
    print("Score: {}".format(student_score))
    if student_score < 0 or student_score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        continue
    if student_score >= 80:
        grade = 'A'
    elif student_score >= 70:
        grade = 'B'
    elif student_score >= 60:
        grade = 'C'
    elif student_score >= 50:
        grade = 'D'
    else:
        grade = 'F'
    

    print("Grade: {}".format(grade))
    if student_score >= 100:
        print("Invalid score. Please enter a score between 0 and 100.")
    else:
        if student_score >= 50:
            print("Pass")
            passed_count += 1
        else:
            print("Fail")
            failed_count += 1
    valid_scores.append(student_score)
average_score = sum(valid_scores) / len(valid_scores) if valid_scores else 0
print("----------------------------")
print(" SCORE SUMMARY")
print("----------------------------")    
print("\nValid scores : ", valid_scores)  
print(f"\npassed: {passed_count}")
print(f"failed: {failed_count}")
print(f"average score: {average_score:.2f}")
print(f"highest score: {max(valid_scores)}")
print(f"lowest score: {min(valid_scores)}")