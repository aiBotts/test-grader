# This program gets a numeric test score from the user and displays the matching letter grade
# Named constants to represent the grade thresholds.

A_GRADE = 90
B_GRADE = 80
C_GRADE = 70
D_GRADE = 60

# Get a test score from the user.
score = int(input('Enter your test grade:' ))

# Determine the grade.
if score >= A_GRADE:
    print('Your grade is an A.')
elif score >= B_GRADE:
    print('Your grade is a B.')
elif score >= C_GRADE:
    print('Your grade is a C.')
elif score >= D_GRADE:
    print('Your grade is a D.')
else:
    print('Your grade is a F.')