import LSystemDrawer
from SentenceGenerator import SentenceGenerator as SG

# Input values for L-system
rules_dragon_curve = {
    "F": "F+G",
    "G": "F-G"
}
axiom_dragon_curve = "F"


rules_fractal_plant = {
    "X": "F+[[X]-X]-F[-FX]+X",
    "F": "FF"
}
axiom_fractal_plant = "X"


rules_sierpinski_triangle = {
    "F": "F−G+F+G−F",
    "G": "GG"
}
axiom_sierpinski_triangle = "F-G-G"


# Build up sentences
sentences_dragon_curve = SG.generate_word(
    axiom=axiom_dragon_curve,
    rules=rules_dragon_curve,
    iter_count=8
)
sentences_fractal_plant = SG.generate_word(
    axiom=axiom_fractal_plant,
    rules=rules_fractal_plant,
    iter_count=4
)
sentences_sierpinski_triangle = SG.generate_word(
    axiom=axiom_sierpinski_triangle,
    rules=rules_sierpinski_triangle,
    iter_count=5
)

print("DRAGON CURVE: ", sentences_dragon_curve)
print("FRACTAL PLANT: ", sentences_fractal_plant)
print("SIERPINSKI TRIANGLE: ", sentences_sierpinski_triangle)

drawer = LSystemDrawer.LSystemDrawer()
drawer.draw_dragon_curve(sentences=sentences_dragon_curve)


