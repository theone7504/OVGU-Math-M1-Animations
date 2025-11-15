from manim import *

class QuadraticInequality(Scene):
    def construct(self):
        #Draw axes and the parabola
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=9,
            y_length=6,
            axis_config={"color": GREY},
            tips=False
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))
        self.wait(1)

        # Parabola y = x^2 + 2x - 3
        parabola = axes.plot(lambda x: x**2 + 2*x - 3, color=BLUE)
        func_label = MathTex("y = x^2 + 2x - 3").next_to(axes, UP)
        self.play(Create(parabola), Write(func_label))
        self.wait(1.5)

        # Highlight vertex
        vertex_point = axes.coords_to_point(-1, -4)
        vertex_dot = Dot(vertex_point, color=YELLOW)
        vertex_label = MathTex("(-1, -4)").next_to(vertex_dot, DOWN)
        self.play(FadeIn(vertex_dot), Write(vertex_label))
        self.wait(1.5)

        #Show roots
        x1, x2 = -3, 1
        root1 = Dot(axes.coords_to_point(x1, 0), color=RED)
        root2 = Dot(axes.coords_to_point(x2, 0), color=RED)
        label1 = MathTex("x_1=-3").next_to(root1, DOWN)
        label2 = MathTex("x_2=1").next_to(root2, DOWN)
        self.play(FadeIn(root1, root2))
        self.play(Write(label1), Write(label2))
        self.wait(1.5)

        # Shade region where f(x) < 0 (between roots)
        # Create shaded area under the curve between -3 and 1
        shaded = axes.get_area(
            graph=parabola,
            x_range=[x1, x2],
            color=BLUE,
            opacity=0.4
        )
        self.play(FadeIn(shaded))
        region_text = Tex("Region where $f(x) < 0$").next_to(shaded, UP)
        self.play(Write(region_text))
        self.wait(2)

        #Show the inequality solution
        solution = MathTex("-3 < x < 1").to_edge(UP)
        solution.set_color_by_tex("x", YELLOW)
        self.play(Write(solution))
        self.wait(2)

        # Dim everything except the conclusion
        self.play(
            FadeOut(parabola),
            FadeOut(vertex_dot),
            FadeOut(vertex_label),
            FadeOut(root1), FadeOut(root2),
            FadeOut(label1), FadeOut(label2),
            FadeOut(region_text),
            FadeOut(shaded),
            FadeOut(func_label),
            FadeOut(axes), FadeOut(labels),
            run_time=2
        )
        self.wait(0.5)

        # Keep the conclusion on screen
        self.play(solution.animate.scale(1.3).set_color(YELLOW))
        self.wait(2)
