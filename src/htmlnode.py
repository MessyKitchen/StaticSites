
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # Base class for all HTML nodes, serving as the foundation.
        # `tag`: The HTML tag (e.g., 'div', 'p', etc.), can be None for raw text nodes.
        # `value`: The inner content or text of the node.
        # `children`: A list of child nodes (or None for leaf/nested-less nodes).
        # `props`: A dictionary of tag attributes like `class`, `href`, etc.
        self.tag = tag
        self.value = value
        self.props = props
        self.children = children

    def to_html(self):
        # Abstract method: Must be implemented by any subclass.
        # Represents how the node renders itself as an HTML string.
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        # Handle the conversion of `props` into a string of HTML attributes.
        # Example: `props={"href": "https://example.com", "class": "my-link"}`
        # Returns: ' href="https://example.com" class="my-link"'
        if self.props is None:
            return ""
        
        props_html = ""
        # Iterates over props to convert each key-value pair into a `key="value"` attribute.
        for prop, value in self.props.items():
            props_html += f' {prop}="{value}"'

        return props_html

    def __repr__(self):
        # String representation for debugging and inspection.
        # Example: HTMLNode('div', 'Hello', None, {'class': 'container'})
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        # A leaf node has no children and represents an HTML element or raw text.
        # `value`: The text content inside the tag (required).
        # `tag`: The type of the HTML tag (optional, can be None for raw text).
        # `props`: Optional tag attributes, e.g., {'href': 'example.com'}.
        if value is None:
            raise ValueError("Value is required for a LeafNode.")
        # Call the parent constructor, enforcing no `children` for a leaf node.
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        # Converts the LeafNode to an HTML string.
        # If `tag` is None, return raw `value`. 
        # If `props` exist, add them as attributes to the opening tag.
        if self.tag is None:
            return self.value
        if self.props:
            attributes = " ".join(f'{key}="{value}"' for key, value in self.props.items())
            return f"<{self.tag} {attributes}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
