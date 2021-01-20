from my_code import pay_calculator


def test_pay_calculator():
    assert 610 == pay_calculator(40)
    assert 152.5 == pay_calculator(10)

