from enum import Enum

# Enum to define various types of text that a TextNode can represent.
class TextType(Enum):
    TEXT = "text"       # Normal text
    BOLD = "bold"       # Bold text
    ITALIC = "italic"   # Italic text
    CODE = "code"       # Inline code
    LINK = "link"       # Hyperlink
    IMAGE = "image"     # Image representation

# Represents a text or visual node with optional metadata like type and URL.
class TextNode:
    def __init__(self, text, text_type, url=None):
        # Initialize a TextNode instance.
        # `text`: The content of the node (e.g., text or image description).
        # `text_type`: A `TextType` enum defining the type of this node.
        # `url`: Optional for items like links or images that require a URL.
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        # Checks equality between two TextNode instances.
        # Returns True if `text`, `text_type`, and `url` are identical.
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        # String representation of the TextNode instance.
        # Highlights the `text`, the `text_type`'s value, and `url` (if present).
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
