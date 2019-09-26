import pytest

"""
    This program will test if the remove_Student function is working.
    The remove_Student function takes a student from a list and deletes it.
    (ex. If a Student needs to drop a course)
    There are 2 pytests in this function.  The first one will pass and the
    second one will fail due to the wrong name of the student being passed
    into the function.
"""

def remove_Student(name, list):
    list.remove(name)
    
def test_remove_Student():
    Student_List = ["Student 1", "Student 2", "Student 3"]
    remove_Student("Student 2", Student_List)
    assert "Student 2" not in Student_List
    
def test_remove_Student_fail():
    Student_List = ["Student 1", "Student 2", "Student 3"]
    remove_Student("Student 4", Student_List)
    assert "Student 4" not in Stuent_List