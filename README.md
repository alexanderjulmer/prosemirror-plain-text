This repository explores the conversion of Prosemirror documents into plain text
via different methods:

1. `doc.text_content`: This method extracts the text content from the
   Prosemirror document, effectively stripping away all formatting and
   structure.
2. `doc.text_descendants`: This method traverses the Prosemirror document and
   collects text from all descendant nodes, preserving some of the structure
   while still providing a plain text representation. It allows for using the
   `leaf_text` property to specify how text from leaf nodes should be handled.

We use Python with the `prosemirror` library, not the JavaScript version, to
demonstrate these methods.
