from arrays_and_strings.check_permutation import check_permutation


class TestCheckPermutation:
    def test_empty_strings(self) -> None:
        assert check_permutation('', '') is True

    def test_single_character(self) -> None:
        assert check_permutation('a', 'a') is True
        assert check_permutation('a', 'b') is False

    def test_same_characters(self) -> None:
        assert check_permutation('hello', 'olleh') is True
        assert check_permutation('hello', 'llohe') is True
        assert check_permutation('hello', 'world') is False

    def test_different_lengths(self) -> None:
        assert check_permutation('abc', 'ab') is False
        assert check_permutation('abcd', 'abc') is False

    def test_whitespace_permutations(self) -> None:
        assert check_permutation('listen  ', ' silent') is False
        assert check_permutation('the eyes', 'they see') is True

    def test_case_sensitive(self) -> None:
        assert check_permutation('AbC', 'bca') is False
        assert check_permutation('AbC', 'CbA') is True
