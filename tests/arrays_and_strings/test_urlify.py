from arrays_and_strings.urlify import urlify


class TestURLify:
    def test_usual_cases(self) -> None:
        assert urlify('Mr John Smith    ', 13) == 'Mr%20John%20Smith'
        assert urlify('Hello World  ', 11) == 'Hello%20World'
        assert urlify('Hello World  ', 5) == 'Hello'
        assert urlify('  Spaces  ', 9) == '%20%20Spaces%20'
        assert urlify('', 0) == ''
        assert urlify('NoSpaces', 8) == 'NoSpaces'

    def test_edge_cases(self) -> None:
        assert urlify(' ' * 1000, 1) == '%20'
        assert urlify('   ', 3) == '%20%20%20'
