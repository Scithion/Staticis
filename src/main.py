from textnode import *

def main():
    print("Initializing!")
    gweth = TextNode("gurps is interesting", TextType.BOLD, None)
    print(gweth.__repr__())
    nonc = TextNode("This comment describes Fear Not/Cattywampus Design Goals", TextType.LINK, "https://www.reddit.com/r/RPGdesign/comments/1kvad25/if_you_could_design_your_dream_ttrpg_what_would/mu8h656/?context=3")
    print(nonc.__repr__())
    return

main()