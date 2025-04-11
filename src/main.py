from textnode import TextNode, TextType

def main():
    # Create a TextNode instance with:
    # - "This is some text" as the displayed text.
    # - TextType.LINK which indicates that this text represents a hyperlink.
    # - "https://www.boot.dev" as the hyperlink's URL.
    node = TextNode("This is some text", TextType.LINK, "https://www.boot.dev")

    # Print the string representation of the TextNode instance.
    # Assumes that the __str__ or __repr__ method is implemented in the TextNode class.
    print(node)

# Entry point for the script—executes `main()` only if the script
# is run directly (not imported as a module).
if __name__ == "__main__":
    main()