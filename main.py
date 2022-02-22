import LSystemDrawer
from SentenceGenerator import SentenceGenerator as SG

# Input values for L-system
rules_dragon_curve = {
    "F": "F+G",
    "G": "F-G"
}
axiom_dragon_curve = "F"


rules_sierpinski_triangle = {
    "F": "F-G+F+G-F",
    "G": "GG"
}
axiom_sierpinski_triangle = "F-G-G"

rules_tree = {
    "M": "S[+M][-M]SM",
    "S": "SS"
}
axiom_tree = "M"


rules_random_object = {
    "A": "B++[-A|B]+A",
    "B": "--A"
}
axiom_random_object = "B"


# Build up sentences
sentences_dragon_curve = SG.generate_word(
    axiom=axiom_dragon_curve,
    rules=rules_dragon_curve,
    iter_count=4
)
sentences_sierpinski_triangle = SG.generate_word(
    axiom=axiom_sierpinski_triangle,
    rules=rules_sierpinski_triangle,
    iter_count=5
)
sentences_tree = SG.generate_word(
    axiom=axiom_tree,
    rules=rules_tree,
    iter_count=5
)
sentences_random_object = SG.generate_word(
    axiom=axiom_random_object,
    rules=rules_random_object,
    iter_count=6
)

print("DRAGON CURVE: ", sentences_dragon_curve)
print("SIERPINSKI TRIANGLE: ", sentences_sierpinski_triangle)
print("TREE:  ", sentences_tree)
print("RANDOM OBJECT: ", sentences_random_object)

drawer = LSystemDrawer.LSystemDrawer(size=20)
drawer.draw_object(sentences=sentences_dragon_curve, angle=90, object_name="dragon curve")
drawer.draw_object(sentences=sentences_sierpinski_triangle, angle=120, object_name="sierpinski triangle")
drawer.draw_object(sentences=sentences_tree, angle=45, object_name="tree")
drawer.draw_object(sentences=sentences_random_object, angle=60, object_name="random object")



