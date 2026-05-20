from adding import add
import pytest

def test_pytest_is_working():
    assert 1 == 1

def test_adding_two_numbers_gives_the_correct_answer():
    # Arrange
    first_num = 3
    second_num = 5
    expected = 8

    # Act
    result = add(first_num, second_num)

    # Assert
    assert expected == result

# Big numbers
# Negatives
# Decimals
def test_adding_two_large_numbers_gives_the_correct_answer():
    assert add(1_000_000, 1_000_000) == 2_000_000

# Parameterizing our tests
# Decorate my function
@pytest.mark.parametrize("first_num, second_num, expected", [
    (-1, -1, -2),
    (-1_000_000, 10, -999_990),
    (-19, 20, 1),
])
def test_adding_pairs_of_numbers_gives_the_correct_answer(first_num, second_num, expected):
    assert add(first_num, second_num) == expected


def test_adding_decimals_gives_the_correct_answer():
    assert add(0.1, 0.2) == pytest.approx(0.3, 10)

def test_adding_two_strings_causes_an_error():
    with pytest.raises(TypeError):
        add("one", "two")

@pytest.mark.parametrize("num1, num2", [
    ([], []),
    ({}, {}),
    (True, []),
    (True, True)
])
def test_adding_any_non_number_causes_an_error(num1, num2):
    with pytest.raises(TypeError):
        add(num1, num2)
