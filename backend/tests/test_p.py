import pytest
# fixture
# pytest.mark.parameterized(", , ,",[])

def add(num1,num2):
    return num1+num2


@pytest.mark.parametrize("num1, num2, exp",[
    (2,3,5),
    (3,4,7)
])
def test_add(num1,num2,exp):
    result = add(num1,num2)
    assert result==exp
