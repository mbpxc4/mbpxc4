import pytest
"""
    This program will calculate the average of two tests taken
    after given a certain input of total points earned.  The 
    first test will pass because 188 / 2 = 94.  The second test
    will fail because the average score when passed through to 
    the function is not 100.
"""


def average_Score(total_points):
    average = total_points / 2
    return average

def test_calculate_Average_Score_Pass():
    total_points = 188
    average = average_Score(total_points)
    assert (average) == pytest.approx(94.0)
    
def test_calculate_Average_Score_Fail():
    total_points = 188
    average = average_Score(total_points)
    assert (average) == pytest.approx(100.0)