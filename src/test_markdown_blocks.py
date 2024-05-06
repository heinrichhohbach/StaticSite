import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_type_code,
    block_to_block_type,
    block_type_heading,
    block_type_ordered_list,
    block_type_paragraph,
    block_type_quote,
    block_type_unordered_list,
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_type_paragraph(self):
        block = "This is **bolded** paragraph"
        self.assertEqual(block_type_paragraph, block_to_block_type(block))

    def test_block_to_block_type_paragraph_with_code(self):
        block = """This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line"""
        self.assertEqual(block_type_paragraph, block_to_block_type(block))

    def test_block_to_block_type_paragraph(self):
        block = """```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```"""
        self.assertEqual(block_type_code, block_to_block_type(block))

    def test_block_to_block_type_heading(self):
        block = "# This is a header"
        self.assertEqual(block_type_heading, block_to_block_type(block))

    def test_block_to_block_type_multiple_heading(self):
        block = "### This is a header"
        self.assertEqual(block_type_heading, block_to_block_type(block))
        
    def test_block_to_block_type_multiple_unolist(self):
        block = """* This is a list
* with items"""
        self.assertEqual(block_type_unordered_list, block_to_block_type(block))

    def test_block_to_block_type_multiple_olist(self):
        block = """1. This is a list
2. with items"""
        self.assertEqual(block_type_ordered_list, block_to_block_type(block))

if __name__ == "__main__":
    unittest.main()