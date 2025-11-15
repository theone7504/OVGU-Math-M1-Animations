from manim import *

class InequalitySignReversal(Scene):
    def construct(self):
        # Number line
        number_line = NumberLine(
            x_range=[-10, 10, 1],
            length=10,
            include_numbers=True,
        )
        origin = number_line.n2p(0)
        self.play(Create(number_line))
        self.wait(1)

        # Example values
        a_val, b_val = 3, 5

        # Arrows from 0 to a and 0 to b
        arrow_a = Arrow(start=origin, end=number_line.n2p(a_val), buff=0)
        arrow_b = Arrow(start=origin, end=number_line.n2p(b_val), buff=0)
        arrow_a.set_color(BLUE)
        arrow_b.set_color(RED)
        label_a = MathTex("a").next_to(arrow_a.get_end(), UP)
        label_b = MathTex("b").next_to(arrow_b.get_end(), UP)

        # Draw arrows and labels
        self.play(GrowArrow(arrow_a), GrowArrow(arrow_b))
        self.play(Write(label_a), Write(label_b))
        self.wait(1.5)

        text = MathTex("a", "<", "b").to_edge(UP)
        text[0].set_color(BLUE)  # 'a'
        text[2].set_color(RED)   # 'b'
        self.play(Write(text))
        self.wait(1.5)
        self.play(FadeOut(label_a), FadeOut(label_b))
        self.wait(0.3)


        # Rotate the arrows (visual flip)
        self.play(Rotate(arrow_a, angle=PI, about_point=origin), run_time=2.5)
        self.play(Rotate(arrow_b, angle=PI, about_point=origin), run_time=2.5)
        self.wait(0.3)

        new_arrow_a = Arrow(start=origin, end=number_line.n2p(-a_val), buff=0).set_color(BLUE)
        new_arrow_b = Arrow(start=origin, end=number_line.n2p(-b_val), buff=0).set_color(RED)
        self.play(
            Transform(arrow_a, new_arrow_a),
            Transform(arrow_b, new_arrow_b),
            run_time=0.6
        )
        self.wait(0.5)

        label_na = MathTex("-a").next_to(new_arrow_a.get_end(), UP)
        label_nb = MathTex("-b").next_to(new_arrow_b.get_end(), UP)
        self.play(FadeIn(label_na), FadeIn(label_nb))
        self.wait(0.6)

        new_text = MathTex("-", "a", ">", "-", "b").to_edge(UP)
        new_text[1].set_color(BLUE)  # 'a'
        new_text[4].set_color(RED)   # 'b'
        self.play(FadeTransform(text, new_text))
        self.wait(1.5)


        idea = Tex("Multiplying by $-1$ reflects points across zero").next_to(number_line, DOWN)
        self.play(Write(idea))
        self.wait(2)
