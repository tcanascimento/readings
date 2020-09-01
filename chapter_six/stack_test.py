import unittest

from stack import Stack


class TestStack(unittest.TestCase):

    def test_issue_first(self):
        stack = Stack(3)
        self.assertTrue(stack.is_empty())
        stack.push("cat")
        stack.push("dog")
        stack.push("horse")
        self.assertTrue(stack.full())
        self.assertEqual(stack.show_top(), "horse")
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_issue_second(self):
        stack = Stack(3)
        self.assertTrue(stack.is_empty())
        stack.push("cat")
        self.assertEqual(stack.show_top(), "cat")
        stack.push("dog")
        self.assertEqual(stack.show_top(), "dog")
        stack.push("horse")
        self.assertTrue(stack.full())
        self.assertEqual(stack.show_top(), "horse")
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertTrue(stack.is_empty())
