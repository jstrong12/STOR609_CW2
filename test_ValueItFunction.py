from ValueIt.ValueItFunction import Value_iteration

#Define the Sam Weekend Example
S1=["healthy","sick"]
A1=["relax","party"]
def R1(sdash,s,a):
    if s == "healthy":
        if a == "relax":
            return 7
        else:
            return 10
    else:
        if a == "relax":
            return 0
        else:
            return 2
def P1(sdash,s,a):
    if s == "healthy":
        if a == "relax":
            p=0.95
        else:
            p=0.7
    else:
        if a == "relax":
            p=0.5
        else:
            p=0.1
    if sdash == "healthy":
        return p
    else:
        return 1-p

#Test that we return both the optimal policy and value, and that they are the same length
def test_value_iteration1():
    result = Value_iteration(S1,A1,P1,R1,0.7,0.001,1)
    assert len(result) == 2
    assert len(result[0]) == len(result[1])

#Test for correct policy
def test_value_iteration2():
    result = Value_iteration(S1,A1,P1,R1,0.9,0.00001,1)[0]
    assert result == ["party","relax"]

#Test for correct value
from pytest import approx
def test_value_iteration3():
    result = Value_iteration(S1,A1,P1,R1,0.9,0.00001,1)[1]
    assert result == [approx(67.07309),approx(54.87796)]

