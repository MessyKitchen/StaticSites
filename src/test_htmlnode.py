# src/test_htmlnode.py
import unittest
from htmlnode import HTMLNode  # Import from the same directory

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_no_props(self):
        node = HTMLNode("p", "Hello, world!", None, None)
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_with_one_prop(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://www.example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com"')
    
    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode("a", "Click me", None, {
            "href": "https://www.example.com",
            "target": "_blank",
            "class": "link"
        })
        props_html = node.props_to_html()
        self.assertIn(' href="https://www.example.com"', props_html)
        self.assertIn(' target="_blank"', props_html)
        self.assertIn(' class="link"', props_html)

if __name__ == "__main__":
    unittest.main()