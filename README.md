This repository explores the conversion of Prosemirror documents into plain text via different methods:

1. `doc.text_content`: This method extracts the text content from the Prosemirror document, effectively stripping away
   all formatting and structure.
2. `doc.text_between`: This method traverses the Prosemirror document and collects text from all descendant nodes.
   Adding a separator allows for preserving some structure in the output.
3. `to_plain()` (**incomplete**) is a custom method to convert to plain text while preserving as much of the original
   structure as possible. It handles various node types and formats the output accordingly.

We use Python with the `prosemirror` library, not the JavaScript version, to demonstrate these methods.

Additionally, we use Pandoc to convert the exported HTML to plain text to compare our efforts.