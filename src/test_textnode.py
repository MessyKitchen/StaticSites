import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_equal_nodes(self):
        # Create two identical nodes
        node1 = TextNode("Sample text", TextType.BOLD)
        node2 = TextNode("Sample text", TextType.BOLD)
        # This test passes if node1 equals node2
        self.assertEqual(node1, node2)

    def test_different_text(self):
        # Create nodes with different text
        node1 = TextNode("First text", TextType.BOLD)
        node2 = TextNode("Second text", TextType.BOLD)
        # This test passes if node1 does NOT equal node2
        self.assertNotEqual(node1, node2)

    def test_different_text_types(self):
        # Create nodes with identical text but different text types
        node1 = TextNode("Sample text", TextType.BOLD)
        node2 = TextNode("Sample text", TextType.ITALIC)
        # This test passes if node1 does NOT equal node2
        self.assertNotEqual(node1, node2)   

    def test_different_urls(self):
        # Create nodes with a URL vs without a URL
        node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://different.com")
        # This test passes if node1 does NOT equal node2
        self.assertNotEqual(node1, node2)

    def test_url_vs_no_url(self):
        # Create a node with a URL and one without
        node1 = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK)  # Default URL is None
        # This test passes if node1 does NOT equal node2
        self.assertNotEqual(node1, node2)

    def test_all_properties_different(self):
        # Create nodes with all different properties
        node1 = TextNode("Text one", TextType.BOLD, None)
        node2 = TextNode("Text two", TextType.ITALIC, "https://example.com")
        # This test passes if node1 does NOT equal node2
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()