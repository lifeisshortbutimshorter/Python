for student in range(1,4):
    student_name = input("Enter the student's name: ")
    print(f"============ {student_name} ============")
    for subject in range(1,3):
        def calculate_total_score(report_score, midterm_score, final_score):
            total_score = report_score + midterm_score + final_score
            return total_score
        print(f"Subject {subject} : ")
        report_score = int(input("Enter the score: "))
        midterm_score = int(input("Enter the midterm score: "))
        final_score = int(input("Enter the final score: "))
        total_score = calculate_total_score(report_score, midterm_score, final_score)

        def grade(total_score):
            if total_score >= 80:
                grade = "A"
                status = "Pass"
            elif total_score >= 70:
                grade = "B"
                status = "Pass"
            elif total_score >= 60:
                grade = "C"
                status = "Pass"
            elif total_score >= 50:
                grade = "D"
                status = "Pass"
            else:
                grade = "F"
                status = "Fail"
            return grade,status
        grade,status = grade(total_score)
        
        print(f"\nTotal score for Subject {subject}: {total_score}")
        print(f"Grade: {grade}")
        print(f"Status : {status}")

