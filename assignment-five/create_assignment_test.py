import pytest

"""
    This program creates a new assignment into a list of all of the
    assignments.  The first test will pass because the right
    assignment was added to the list. The second test will fail 
    because the wrong assignment was added to the list.
"""

def create_assignment(name, list):
    list.append(name)
    
def test_create_assignment_pass():
    Assignment_List = ["Assignment 1", "Assignment 2", "Assignment 3"]
    create_assignment("Assignment 4", Assignment_List)
    assert "Assignment 4" in Assignment_List
    
def test_create_assignment_fail():
    Assignment_List = ["Assignment 1", "Assignment 2", "Assignment 3"]
    create_assignment("Assignment 5", Assignment_List)
    assert "Assignment 4" in Assignment_List