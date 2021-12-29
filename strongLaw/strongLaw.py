from manim import *

class MainScene(Scene):
    def construct(self):
        title = Text("Strong Law of Action Reaction")
        circ1 = Circle().set_fill(BLUE, opacity=1.0).set_stroke(BLUE).shift(RIGHT*2)
        circ2 = Circle().set_fill(RED, opacity=1.0).set_stroke(RED).shift(LEFT*2)

        m1 = MathTex("m_1").shift(RIGHT*2)
        m2 = MathTex("m_2").shift(LEFT*2)

        F2 = Arrow(start = RIGHT+DOWN, end = RIGHT+DOWN+.5*(4*LEFT+3*UP), color=RED)
        F1 = Arrow(start = 3*LEFT+2*UP, end = 3*LEFT+2*UP+.5*(4*RIGHT+3*DOWN), color=BLUE)

        loc1 = F1.get_center()
        loc2 = F2.get_center()

        centerLine = Line(start = RIGHT+DOWN, end = 3*LEFT+2*UP)

        point1 = LabeledDot(MathTex("m_1", color=BLUE)).shift(RIGHT*2)
        point2 = LabeledDot(MathTex("m_2", color = RED)).shift(LEFT*2)

        F1Text = MathTex(r"\vec F_{21}", color=BLUE)
        F2Text = MathTex(r"\vec F_{12}", color=RED)

        F1Text.next_to(F1)
        F2Text.next_to(F2)

        WeakLaw = MathTex(r"\vec F_{12} = -\vec F_{21}").shift(UP)

        part1 = MathTex(r"\bullet \text{Equal and Opposite}", font_size = 45).shift(2*UP+3*RIGHT)
        part2 = MathTex(r"\bullet \text{Forces are Central}", font_size = 45).shift(1*UP+3*RIGHT)

        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        self.play(Create(circ1), Create(circ2))
        self.play(DrawBorderThenFill(m1), DrawBorderThenFill(m2))
        self.wait(1)
        self.play(FadeOut(m1), FadeOut(m2))
        self.play(Transform(circ1, point1), Transform(circ2,point2))
        self.add(point1)
        self.add(point2)
        self.remove(circ1)
        self.remove(circ2)
        self.play(point2.animate.shift(UP*2+LEFT), point1.animate.shift(DOWN+LEFT))
        self.wait(1)
        self.play(GrowArrow(F1))
        self.play(Create(F1Text))
        self.wait(1)
        self.play(GrowArrow(F2))
        self.play(Create(F2Text))
        self.wait(1)
        self.play(FadeOut(F1Text),FadeOut(F2Text))
        self.play(F1.animate.move_to(ORIGIN), F2.animate.move_to(ORIGIN+LEFT), point1.animate.shift(RIGHT), point2.animate.shift(LEFT))
        self.play(Create(WeakLaw))
        self.play(Write(part1))
        self.wait(1)
        self.play(FadeOut(WeakLaw), F2.animate.shift(4*RIGHT), F1.animate.shift(4*RIGHT), point1.animate.shift(LEFT), point2.animate.shift(RIGHT))
        self.play(GrowFromCenter(centerLine))
        self.wait(1)
        self.play(F1.animate.move_to(loc1), F2.animate.move_to(loc2))
        self.play(FadeOut(centerLine))
        self.play(Write(part2))
        self.wait(3)
