from prosemirror.model import DOMSerializer

from prosemirror_plain_text.document import my_doc
from prosemirror_plain_text.schema import to_plain, my_schema


def main():
    with open("../../exports/text_content.txt", "w") as f:
        f.write(my_doc.text_content)

    with open("../../exports/text_between.txt", "w") as f:
        f.write(my_doc.text_between(0, my_doc.content.size, "\n\n"))

    with open("../../exports/text_custom.txt", "w") as f:
        f.write(to_plain(my_doc))

    with open("../../exports/text.html", "w") as f:
        html = DOMSerializer.from_schema(my_schema).serialize_fragment(my_doc.content)
        f.write(str(html))

    print(
        "Successfully exported documents to exports/text_content.txt"
        "and exports/text_between.txt and exports/text_custom.txt"
    )

if __name__ == "__main__":
    main()
