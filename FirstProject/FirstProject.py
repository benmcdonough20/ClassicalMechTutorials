from manim import *

class CreateCircle(Scene):
    def construct(self):
        triangle = Triangle()
        triangle.set_fill(RED, opacity= 1.0)
        
        circle = Circle()
        circle.set_fill(PURPLE, opacity=1.0)

        square = Square()
        square.set_fill(BLUE, opacity=1.0)

        self.play(Create(triangle))
        self.play(Transform(triangle, circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(square))
