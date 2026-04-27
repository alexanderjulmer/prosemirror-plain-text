from prosemirror.model import Schema


def doc_to_plain(node, **kwargs):
    leaf_text = kwargs.get("leaf_text")
    return "\n\n".join([leaf_text(node.child(i)) for i in range(node.child_count)])


def bullet_list_to_plain(node, **kwargs):
    leaf_text = kwargs.get("leaf_text")
    return "\n".join(
        [f"{i + 1}. {leaf_text(node.child(i))}" for i in range(node.child_count)]
    )


def details_to_plain(node, **kwargs):
    leaf_text = kwargs.get("leaf_text")
    return "\n".join([leaf_text(node.child(i)) for i in range(node.child_count)])


nodes = {
    "doc": {"content": "block+", "to_plain": doc_to_plain},
    "paragraph": {
        "content": "inline*",
        "group": "block",
    },
    "text": {"group": "inline"},
    "heading": {
        "content": "inline*",
        "group": "block",
        "defining": True,
    },
    "bullet_list": {
        "content": "list_item+",
        "group": "block",
        "to_plain": bullet_list_to_plain,
    },
    "list_item": {
        "content": "paragraph block*",
    },
    "details": {
        "content": "summary details_body",
        "group": "block",
        "to_plain": details_to_plain,
    },
    "summary": {
        "content": "inline*",
    },
    "details_body": {
        "content": "block+",
    },
}

my_schema = Schema({"nodes": nodes})
