# src/test_htmlnode.py
import unittest
from htmlnode import HTMLNode, LeafNode  # Import from the same directory

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_no_props(self):
        # Test that when no props (attributes) are passed, the method returns an empty string.
        node = HTMLNode("p", "Hello, world!", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_one_prop(self):
        # Test that a single property (e.g., href) is rendered correctly.
        node = HTMLNode("a", "Click me", None, {"href": "https://www.example.com"})
        # Props should render as a single space followed by key="value".
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com"')

    def test_props_to_html_with_multiple_props(self):
        # Test that multiple props (attributes) are rendered correctly.
        # For example, class, target, and href should all appear in the output.
        node = HTMLNode("a", "Click me", None, {
            "href": "https://www.example.com",
            "target": "_blank",
            "class": "link"
        })
        # `props_to_html` should include all keys and values as properly formatted attributes.
        props_html = node.props_to_html()
        self.assertIn(' href="https://www.example.com"', props_html)
        self.assertIn(' target="_blank"', props_html)
        self.assertIn(' class="link"', props_html)

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_basic_tag(self):
        # Test rendering a simple <p> tag with text content.
        node = LeafNode("Hello, world!", "p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        # Test rendering raw text when `tag=None`.
        node = LeafNode("Just raw text", None)
        self.assertEqual(node.to_html(), "Just raw text")

    def test_leaf_to_html_with_attributes(self):
        # Test rendering a tag with additional attributes.
        attributes = {"href": "https://www.boot.dev"}
        node = LeafNode("Click me!", "a", attributes)
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Click me!</a>')

    def test_leaf_to_html_value_required(self):
        # Test that a ValueError is raised when `value=None`.
        with self.assertRaises(ValueError):
            LeafNode(None, "p")

    def test_leaf_to_html_empty_value(self):
        # Test rendering an empty value if no content is provided.
        node = LeafNode("", "p")
        self.assertEqual(node.to_html(), "<p></p>")

if __name__ == "__main__":
    unittest.main()