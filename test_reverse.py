from reverse_multidimensional import reverse_main
import unittest


class TestReverse(unittest.TestCase):
    """
    Test the reverse_main function to check if array is being reversed
    """

    def test_reverse_1(self):
        """
        Input: [1, 2, [3, 4, 5], [6, [7, 8], 9]])
        Output: [[9, [8, 7], 6], [5, 4, 3], 2, 1]
        """
        result = reverse_main([1, 2, [3, 4, 5], [6, [7, 8], 9]])
        self.assertEqual(result, [[9, [8, 7], 6], [5, 4, 3], 2, 1])

    def test_reverse_2(self):
        """
        Input: [1, 2, [3, 4,[12,14,[16,18,19],15], 5], [6, [7, 8], 9]]
        Output: [[9, [8, 7], 6], [5, [15, [19, 18, 16], 14, 12], 4, 3], 2, 1]
        """
        result = reverse_main([1, 2, [3, 4,[12,14,[16,18,19],15], 5], [6, [7, 8], 9]])
        self.assertEqual(result, [[9, [8, 7], 6], [5, [15, [19, 18, 16], 14, 12], 4, 3], 2, 1])

    def test_reverse_3(self):
        """
        Input: [1,2,[3,[4,5,[6,7,[8],[9,10]]]]]
        Output: [[[[[10, 9], [8], 7, 6], 5, 4], 3], 2, 1]
        """
        result = reverse_main([1,2,[3,[4,5,[6,7,[8],[9,10]]]]])
        self.assertEqual(result, [[[[[10, 9], [8], 7, 6], 5, 4], 3], 2, 1])

    def test_reverse_4(self):
        """
        Input: ['a', 'b', ['c', 'd', 'e'], ['f', ['g', 'h'], 'i']]
        Output: [['i', ['h', 'g'], 'f'], ['e', 'd', 'c'], 'b', 'a']
        """
        result = reverse_main(['a', 'b', ['c', 'd', 'e'], ['f', ['g', 'h'], 'i']])
        self.assertEqual(result, [['i', ['h', 'g'], 'f'], ['e', 'd', 'c'], 'b', 'a'])

    def test_reverse_5(self):
        """
        Input: ['+',['~','*'], '-', ['=', '!',[',','.','/'], '@'], ['$', ['^', '"'], '}']]
        Output: [['}', ['"', '^'], '$'], ['@', ['/', '.', ','], '!', '='], '-', ['*', '~'], '+']
        """
        result = reverse_main(['+',['~','*'], '-', ['=', '!',[',','.','/'], '@'], ['$', ['^', '"'], '}']])
        self.assertEqual(result, [['}', ['"', '^'], '$'], ['@', ['/', '.', ','], '!', '='], '-', ['*', '~'], '+'])

    def test_reverse_6(self):
        """
        Input: [1, [[],[]], [3, [], 5], [6, [7,[], 8], 9]]
        Output: [[9, [8, [], 7], 6], [5, [], 3], [[], []], 1]
        """
        result = reverse_main([1, [[],[]], [3, [], 5], [6, [7,[], 8], 9]])
        self.assertEqual(result, [[9, [8, [], 7], 6], [5, [], 3], [[], []], 1])

    def test_reverse_7(self):
        """
        Input: [1, 2, [3, 4, 5],[[1, 2, [3, 4,[12,14,[16,18,[19,[31,32,35]]],15], 5], [6, [7,
                [['+',['~','*'], '-', ['=', '!',[',','.','/'], '@'], ['$', ['^', '"'], '}']]], 8], 9]]], [6, [7, 8], 9]]
        Output: [[9, [8, 7], 6], [[[9, [8, [[['}', ['"', '^'], '$'], ['@', ['/', '.', ','], '!', '='], '-',
                ['*', '~'], '+']], 7], 6], [5, [15, [[[35, 32, 31], 19], 18, 16], 14, 12], 4, 3], 2, 1]], [5, 4, 3], 2, 1]
        """
        result = reverse_main([1, 2, [3, 4, 5],[[1, 2, [3, 4,[12,14,[16,18,[19,[31,32,35]]],15], 5], [6, [7,
                            [['+',['~','*'], '-', ['=', '!',[',','.','/'], '@'], ['$', ['^', '"'], '}']]], 8], 9]]], [6, [7, 8], 9]])
        self.assertEqual(result, [[9, [8, 7], 6], [[[9, [8, [[['}', ['"', '^'], '$'], ['@', ['/', '.', ','], '!', '='], '-',
                                ['*', '~'], '+']], 7], 6], [5, [15, [[[35, 32, 31], 19], 18, 16], 14, 12], 4, 3], 2, 1]], [5, 4, 3], 2, 1])

    def test_reverse_8(self):
        """
        Input: [1, [[],[]], [3, [], 5],[['a', 'b', ['c', 'd', 'e'], ['f', ['g', 'h'], 'i']]], [6, [7,[], 8], 9]]
        Output: [[9, [8, [], 7], 6], [[['i', ['h', 'g'], 'f'], ['e', 'd', 'c'], 'b', 'a']], [5, [], 3], [[], []], 1]
        """
        result = reverse_main([1, [[],[]], [3, [], 5],[['a', 'b', ['c', 'd', 'e'], ['f', ['g', 'h'], 'i']]], [6, [7,[], 8], 9]])
        self.assertEqual(result, [[9, [8, [], 7], 6], [[['i', ['h', 'g'], 'f'], ['e', 'd', 'c'], 'b', 'a']], [5, [], 3], [[], []], 1])

if __name__ == '__main__':
    print(unittest.main())
