# src/test_htmlnode.py
import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode  # Import from the same directory

#HTMLNode
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

# LeafNode
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

# ParentNode
class TestParentNode(unittest.TestCase):

    # Test for a single child in a ParentNode and proper HTML rendering.
    def test_simple_parent_with_leaf(self):
        child_node = LeafNode("hello", "span")
        parent_node = ParentNode("div", props=None, children=[child_node])
        print(parent_node.to_html())
        assert parent_node.to_html() == "<div><span>hello</span></div>"
        

    # Test for multiple children in a ParentNode to ensure all children are rendered correctly.
    def test_multiple_children(self):
        child1 = LeafNode("Bold", "b")
        child2 = LeafNode("Normal", None)
        child3 = LeafNode("Italic", "i")
        parent_node = ParentNode("p", props=None, children=[child1, child2, child3])
        assert parent_node.to_html() == "<p><b>Bold</b>Normal<i>Italic</i></p>"

    # Test for nested ParentNode objects to ensure recursion works as expected.
    def test_nested_parent_nodes(self):
        grandchild_node = LeafNode("grandchild", "b")
        child_node = ParentNode("span", props=None, children=[grandchild_node])
        parent_node = ParentNode("div", props=None, children=[child_node])
        assert parent_node.to_html() == "<div><span><b>grandchild</b></span></div>"

    # Test that a ParentNode raises a ValueError when 'tag' is missing.
    def test_missing_tag(self):
        try:
            parent_node = ParentNode(None, props=None, children=[LeafNode("Hello", "span")])
        except ValueError as e:
            assert str(e) == "ParentNode cannot render HTML without a tag."
        else:
            assert False, "Expected ValueError was not raised." 

    # Test that a ParentNode raises a ValueError when 'children' is empty.
    def test_empty_children(self):
        try:
            parent_node = ParentNode("div", props=None, children=[])
        except ValueError as e:
            assert str(e) == ("Children is required for a ParentNode and cannot be empty.")
        else:
            assert False, "Expected ValueError was not raised."


if __name__ == "__main__":
    unittest.main()