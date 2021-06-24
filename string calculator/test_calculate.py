from calculate import calculate

def test_calculate():
    assert True

def test_it_takes_two_comma_seperated_numbers_and_returns_a_sum():
    user_input = "1,2"
    result = calculate(user_input)

    assert result == 3