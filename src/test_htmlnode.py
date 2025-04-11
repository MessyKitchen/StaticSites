# src/test_htmlnode.py
import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextType, TextNode

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


#Text_to_HTML
    class TestTextNodeToHtmlNode(unittest.TestCase):
        
        def test_text(self):
            # Testing conversion of a TextNode with TEXT type to an HTMLNode
            # This is the most basic case - plain text without any formatting
            node = TextNode("This is a text node", TextType.TEXT)
            html_node = text_node_to_html_node(node)
            
            # For plain text, we don't want any HTML tag - it should just be rendered as is
            # So the tag should be None to indicate no wrapping element
            self.assertEqual(html_node.tag, None)
            
            # The text content should be preserved exactly as it was
            # This ensures the conversion doesn't alter the original text
            self.assertEqual(html_node.value, "This is a text node")
    
    # Note: We don't test for props here since plain text doesn't need any HTML attributes

        def test_bold(self):
            # Testing conversion of a TextNode with BOLD type to an HTMLNode
            # We're verifying that a bold text node is properly converted to an HTML <b> element
            node = TextNode("Bold text", TextType.BOLD)
            html_node = text_node_to_html_node(node)

            # The HTML representation of bold text uses the <b> tag
            self.assertEqual(html_node.tag, "b")

            # The text content should be preserved during conversion
            self.assertEqual(html_node.value, "Bold text")

            # Bold text doesn't need any special HTML attributes/properties
            self.assertEqual(html_node.props, {})

        def test_link(self):
            # Testing conversion of a TextNode with LINK type to an HTMLNode
            # Links need both text content and a URL to be valid
            node = TextNode("Click here", TextType.LINK, "https://example.com")
            html_node = text_node_to_html_node(node)

            # The HTML representation of a link uses the <a> tag
            self.assertEqual(html_node.tag, "a")

            # The link text should appear as the content of the <a> tag
            self.assertEqual(html_node.value, "Click here")

            # The URL must be set as the "href" attribute for the link to work in HTML
            self.assertEqual(html_node.props, {"href": "https://example.com"})

if __name__ == "__main__":
    unittest.main()