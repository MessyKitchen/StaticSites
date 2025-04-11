from htmlnode import ParentNode, LeafNode

# Reproducing the test case, you are trying to fix:
leaf = LeafNode("hello", "span")
parent = ParentNode("div", [leaf])

# Output debug info
print(parent.to_html())  # This should match "<div><span>Hello</span></div>"
print(leaf.to_html())
