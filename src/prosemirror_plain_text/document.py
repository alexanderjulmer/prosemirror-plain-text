from prosemirror.model import Node
from .schema import my_schema

document_json = {
    "type": "doc",
    "content": [
        {"type": "heading", "content": [{"type": "text", "text": "Document Title"}]},
        {
            "type": "paragraph",
            "content": [
                {"type": "text", "text": "This is a paragraph introducing the content."}
            ],
        },
        {
            "type": "bullet_list",
            "content": [
                {
                    "type": "list_item",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [{"type": "text", "text": "First item"}],
                        }
                    ],
                },
                {
                    "type": "list_item",
                    "content": [
                        {
                            "type": "bullet_list",
                            "content": [
                                {
                                    "type": "list_item",
                                    "content": [
                                        {
                                            "type": "paragraph",
                                            "content": [{"type": "text", "text": "First item"}],
                                        }
                                    ],
                                },
                                {
                                    "type": "list_item",
                                    "content": [
                                        {
                                            "type": "paragraph",
                                            "content": [{"type": "text", "text": "Second item"}],
                                        }
                                    ],
                                },
                            ],
                        }
                    ],
                },
            ],
        },
        {
            "type": "details",
            "content": [
                {
                    "type": "summary",
                    "content": [{"type": "text", "text": "Click for details"}],
                },
                {
                    "type": "details_body",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "Here is the hidden information.",
                                }
                            ],
                        }
                    ],
                },
            ],
        },
    ],
}

my_doc = Node.from_json(my_schema, document_json)
