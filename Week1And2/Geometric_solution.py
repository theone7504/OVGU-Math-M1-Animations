from manim import *

class QuadraticInequality(Scene):
    def construct(self):
        # Coefficients for f(x) = ax^2 + bx + c
        a, b, c = 1, 2, -3
        curve_color = YELLOW
        axis_color = BLUE


        title = MathTex(r"x^2 + 2x - 3 <", "0")
        title[1].set_color(axis_color)  # make the '0' same color as the x-axis
        eq = MathTex(r"f(x) = x^2 + 2x - 3")
        fact = MathTex(r"(x+3)(x-1) = 0")
        zeros_text = MathTex(r"\text{zeros: } x = -3,\; x = 1")

        vertex_formula = MathTex(r"x_v = -\frac{b}{2a},\quad y_v = c - \frac{b^2}{4a}")
        compute_vertex = MathTex(r"x_v = -1,\quad y_v = -4")

        text_block = VGroup(title, eq, fact, zeros_text, vertex_formula, compute_vertex)
        text_block.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        text_block.to_edge(UP, buff=0.4)



        eq[0].set_color(curve_color)


        for m in text_block:
            self.play(Write(m), run_time=1.8)
            self.wait(0.8)



        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 2],
            x_length=12,
            y_length=6,
            axis_config={"include_tip": True, "numbers_to_include": range(-5,6,1)},
        )
        axes.x_axis.set_color(axis_color)
        axes.y_axis.set_color(axis_color)
        axes.to_edge(DOWN, buff=0.6)

        # Axis labels
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")
        axis_labels.scale(1)

        self.play(Transform(text_block, axes), Write(axis_labels))
        self.wait(0.2)

        # --- Important points: zeros and vertex ---
        zero_coords = [(-3, 0), (1, 0)]
        zeros = VGroup()
        zero_labels = VGroup()
        for x_val, y_val in zero_coords:
            # open dots to indicate strict inequality
            circ = Circle(radius=0.1, stroke_width=3)
            circ.set_fill(opacity=0)
            circ.set_stroke(width=3)
            circ.move_to(axes.c2p(x_val, y_val))
            circ.set_color(WHITE)  # same color as x-axis
            zeros.add(circ)

            lbl = MathTex(str(x_val)).next_to(circ, UL, buff=0.2)
            zero_labels.add(lbl)

        # Vertex point
        x_v = -b / (2 * a)
        y_v = c - b ** 2 / (4 * a)
        vertex_dot = Dot(axes.c2p(x_v, y_v)).set_color(TEAL_A)
        vertex_label = MathTex(r"(x_v, y_v)")
        numeric_vertex = MathTex(f"({x_v:.0f}, {y_v:.0f})").next_to(vertex_dot, DOWN + LEFT, buff=0.12).scale(0.5)

        # Show zeros and vertex
        self.play(LaggedStart(*[Create(z) for z in zeros], lag_ratio=0.3))
        self.play(LaggedStart(*[Write(l) for l in zero_labels], lag_ratio=0.2))
        self.wait(0.2)
        self.play(FadeIn(vertex_dot), Write(numeric_vertex))
        self.wait(0.2)

        # Comment
        direction_comment = Text("The curve opens upward since x squared is positive",
                                 font_size=24).next_to(axes, UP, buff=0.5).scale(0.5)
        self.play(Write(direction_comment))
        self.wait(0.3)

        # THE PARABOLA
        def parabola_func(x):
            return a * x ** 2 + b * x + c

        graph = axes.plot(parabola_func, x_range=[-6, 6], stroke_width=4, color=curve_color)

        # Write f(x) label in the same color as the curve
        fx_label = MathTex(r"y = f(x)")
        # place fx_label next to the curve at x=2
        fx_label.next_to(axes.c2p(2, parabola_func(2)), UR, buff=0.3)
        fx_label.set_color(curve_color)

        # Draw the parabola with points and labels still visible
        self.play(Create(graph), Write(fx_label), run_time=4)
        self.wait(0.9)

        # AREA WHERE f(x) < 0 (between the zeros)
        area = axes.get_area(graph, x_range=[-3, 1])
        area.set_fill(RED_A, opacity=0.2)
        area.set_stroke(opacity=0)


        self.play(Create(area), run_time=2)
        self.wait(1)

        # open circles stay on top and visible
        for z in zeros:
            self.bring_to_front(z)

        self.wait(0.6)

        #the solution interval
        solution_text = MathTex(r"\text{Solution: } x \in (-3,\,1)")
        solution_text.move_to(axes.c2p(2, -4)+ RIGHT*1)
        self.play(Write(solution_text))
        self.wait(2)
