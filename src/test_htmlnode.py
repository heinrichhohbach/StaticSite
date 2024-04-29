import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com" target="_blank"')
    
    def test_props_to_html_with_single_prop(self):
        node = HTMLNode(props={"href": "https://www.example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com"')

    def test_props_to_html_with_None_prop(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_leaf_node_to_html_with_no_Value(self):
        node = LeafNode(value=None, tag="p")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_node_to_html_with_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_node_to_html_without_props(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')

    def test_leaf_node_to_html_with_value_no_tag(self):
        node = LeafNode(tag=None,value="Just some text.")
        self.assertEqual(node.to_html(), "Just some text.")
    
    def test_leaf_node_to_html_with_empty_props(self):
        node = LeafNode(tag="p", value="Text with empty props.", props={})
        self.assertEqual(node.to_html(), "<p>Text with empty props.</p>")

    # This is an example test; implementation depends on if you handle HTML character escaping
    def test_leaf_node_to_html_with_special_characters(self):
        node = LeafNode(tag="p", value="5 < 6 and 10 > 7.")
        self.assertEqual(node.to_html(), "<p>5 < 6 and 10 > 7.</p>")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )






if __name__ == '__main__':
    unittest.main()