from .document import my_doc


def leaf_text(node):
    if "to_plain" in node.type.spec:
        return node.type.spec["to_plain"](node, leaf_text=leaf_text)
    return node.text_content


def text_descendants(doc):
    return leaf_text(doc)


def main():
    # Method 1: doc.text_content
    method1_export = my_doc.text_content

    # Method 2: doc.text_descendants (custom logic for traversing descendants)
    method2_export = text_descendants(my_doc)

    with open("exports/text_content.txt", "w") as f:
        f.write(method1_export)

    with open("exports/text_descendants.txt", "w") as f:
        f.write(method2_export)

    print(
        "Successfully exported documents to exports/text_content.txt and exports/text_descendants.txt"
    )


if __name__ == "__main__":
    main()
