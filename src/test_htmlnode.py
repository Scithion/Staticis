from htmlnode import *

def test_htmlnode():
    test1 = HTMLNode(tag="p", value="This is a paragraph", props={"style": "color: red;"})
    test3 = HTMLNode(tag="h5", value="minor header")
    test2 = HTMLNode(tag="h2", value="Secondary header", children=[test1,test3], props={"style": "font-size: 30px"})

    print(test2.__repr__())
    
test_htmlnode()