import pytest

from prosemirror_plain_text.document import my_doc
from prosemirror_plain_text.main import text_descendants


@pytest.fixture
def document():
    return my_doc


def test_text_content_method(document):
    """Test standard prosemirror text_content method stripping formatting but keeping inline content inline."""
    result = document.text_content
    expected = "Document TitleThis is a paragraph introducing the content.First itemSecond itemClick for detailsHere is the hidden information."
    assert result == expected


def test_text_descendants_method(document):
    """Test text_descendants method mapping plain text output with specialized functions via schema."""
    result = text_descendants(document)

    expected_lines = [
        "Document Title",
        "",
        "This is a paragraph introducing the content.",
        "",
        "1. First item",
        "2. Second item",
        "",
        "Click for details",
        "Here is the hidden information.",
    ]

    expected = "\n".join(expected_lines)
    assert result == expected
