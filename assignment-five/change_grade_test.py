import pytest
"""
    This program is used to change a grade in the grading book.
    (e.x. If the teacher needed to apply a curve to a grade)
    The first test will pass because the updated_grade isn't
    the same as the previous_grade.  The second test will not
    pass because the updated_grade is the same as the 
    previous_grade.
"""
def change_grade(old_grade):
    new_grade = old_grade + 4
    return new_grade
    
def test_change_grade_pass():
    previous_grade = 94
    updated_grade = change_grade(previous_grade)
    assert updated_grade != previous_grade
    
def test_change_grade_fail():
    previous_grade = 94
    updated_grade = change_grade(previous_grade)
    assert updated_grade == previous_grade
