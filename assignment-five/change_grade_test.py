import pytest

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