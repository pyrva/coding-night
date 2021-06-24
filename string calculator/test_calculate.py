import random

from calculate import calculate


def test_calculate():
    assert True

def test_it_takes_two_comma_seperated_numbers_and_returns_a_sum():
    user_input = "1,2"
    result = calculate(user_input)

    assert result == 3

def test_it_handles_n_amount_of_numbers():
    terms_we_will_test = random.randint(2, 12)

    terms = []
    checksum = 0
    for _ in range(terms_we_will_test):
        term = random.randint(1, 1000)
        checksum = checksum + term
        terms.append(str(term))

    result = calculate(",".join(terms))

    assert isinstance(result, int)
    assert checksum == result