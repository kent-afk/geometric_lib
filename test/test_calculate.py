import calculate

test_cases = [
    {'figure': 'circle', 'function': 'area', 'size': [
        5], 'expected': "area of circle is 78.53981633974483\n"},
    {'figure': 'circle', 'function': 'perimeter', 'size': [
        5], 'expected': "perimeter of circle is 31.41592653589793\n"},
    {'figure': 'square', 'function': 'area', 'size': [
        5], 'expected': "area of square is 25\n"},
    {'figure': 'square', 'function': 'perimeter', 'size': [
        5], 'expected': "perimeter of square is 20\n"},
]

for case in test_cases:
    def test_calc(capsys):

        figure = case['figure']
        function = case['function']
        size = case['size']
        expected = case['expected']

        calculate.calc(figure, function, size)

        captured = capsys.readouterr()
        assert captured.out == expected
