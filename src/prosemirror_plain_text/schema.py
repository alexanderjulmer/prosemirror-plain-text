from prosemirror.model import Schema


def to_plain(node):
    if "to_plain" in node.type.spec:
        return node.type.spec["to_plain"](node)
    return node.text_content


def doc_to_plain(node):
    """
    Custom to_plain function for the 'doc' node type that concatenates the plain text
    of its child nodes with double newlines in between.
    """
    return "\n\n".join([to_plain(node.child(i)) for i in range(node.child_count)])


def bullet_list_to_plain(node, **kwargs):
    """
    Custom to_plain function for the 'bullet_list' node type that formats its child nodes
    as a numbered list in plain text.
    """
    return "\n".join(
        [f"{i + 1}. {to_plain(node.child(i))}" for i in range(node.child_count)]
    )


def details_to_plain(node, **kwargs):
    return "\n".join([to_plain(node.child(i)) for i in range(node.child_count)])


nodes = {
    "doc": {"content": "block+", "to_plain": doc_to_plain },
    "paragraph": {
        "content": "inline*",
        "group": "block",
        "toDOM": lambda node: ["p", 0],
    },
    "text": {"group": "inline"},
    "heading": {
        "content": "inline*",
        "group": "block",
        "defining": True,
        "toDOM": lambda node: ["h1", 0],
    },
    "bullet_list": {
        "content": "list_item+",
        "group": "block",
        "to_plain": bullet_list_to_plain,
        "toDOM": lambda node: ["ul", 0],
    },
    "list_item": {
        "content": "paragraph block*",
        "toDOM": lambda node: ["li", 0],
    },
    "details": {
        "content": "summary details_body",
        "group": "block",
        "to_plain": details_to_plain,
        "toDOM": lambda node: ["details", 0],
    },
    "summary": {
        "content": "inline*",
        "toDOM": lambda node: ["summary", 0],
    },
    "details_body": {
        "content": "block+",
        "toDOM": lambda node: ["div", 0],
    },
}

my_schema = Schema({"nodes": nodes})
