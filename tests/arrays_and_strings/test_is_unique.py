from arrays_and_strings.is_unique import (
    is_unique,
    is_unique_no_additional_data_structure,
)


def test_is_unique() -> None:
    assert is_unique('abcdef') is True
    assert is_unique('aabbcc') is False
    assert is_unique('') is True
    assert is_unique(' ') is True


def test_is_unique_no_additional_data_structure() -> None:
    assert is_unique_no_additional_data_structure('abcdef') is True
    assert is_unique_no_additional_data_structure('aabbcc') is False
    assert is_unique_no_additional_data_structure('') is True
    assert is_unique_no_additional_data_structure(' ') is True
