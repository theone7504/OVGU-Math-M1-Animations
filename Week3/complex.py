from manim import *
import numpy as np

class ComplexAddition(Scene):
    def construct(self):
        # Complex plane (Argand plane)
        plane = ComplexPlane(
            x_range=[-3, 5],
            y_range=[-3, 5],
            background_line_style={"stroke_opacity": 0.4}
        ).add_coordinates()
        self.play(Create(plane))

        # Define complex numbers
        z1 = 2 + 1j
        z2 = 1 + 2j
        z_sum = z1 + z2

        # Base vectors
        vec_z1 = Arrow(plane.n2p(0), plane.n2p(z1), buff=0, color=BLUE)
        vec_z2 = Arrow(plane.n2p(0), plane.n2p(z2), buff=0, color=ORANGE)

        # Labels with updaters (only for first addition)
        label_z1 = MathTex("z_1 = 2 + i", color=BLUE)
        label_z1.add_updater(lambda m: m.next_to(vec_z1.get_end(), RIGHT, buff=0.2))

        label_z2 = MathTex("z_2 = 1 + 2i", color=ORANGE)
        label_z2.add_updater(lambda m: m.next_to(vec_z2.get_end(), LEFT, buff=0.2))

        # Step 1 — show both base vectors
        self.play(GrowArrow(vec_z1), Write(label_z1))
        self.play(GrowArrow(vec_z2), Write(label_z2))
        self.wait(1)

        # Step 2 — move z2 to start at z1’s tip
        moved_vec_z2 = Arrow(
            plane.n2p(z1),
            plane.n2p(z_sum),
            buff=0,
            color=ORANGE
        )
        self.play(Transform(vec_z2, moved_vec_z2))
        self.wait(0.5)

        # Step 3 — show result point
        dot = Dot(plane.n2p(z_sum), color=WHITE)
        self.play(FadeIn(dot))
        self.wait(1)

        # Step 4 — now draw the result vector and its label
        vec_sum = Arrow(plane.n2p(0), plane.n2p(z_sum), buff=0, color=GREEN)
        label_sum = MathTex("z_1 + z_2 = 3 + 3i", color=GREEN)
        label_sum.add_updater(lambda m: m.next_to(vec_sum.get_end(), RIGHT, buff=0.2))
        self.play(GrowArrow(vec_sum), Write(label_sum))
        self.wait(1.5)

        # Step 5 — clear the result vector (keep base labels)
        self.play(FadeOut(vec_sum, label_sum))
        self.wait(0.5)

        # Step 6 — show commutative version (z2 + z1)
        vec_z1_new = Arrow(plane.n2p(z2), plane.n2p(z_sum), buff=0, color=BLUE)
        vec_z2_reset = Arrow(plane.n2p(0), plane.n2p(z2), buff=0, color=ORANGE)
        self.play(
            Transform(vec_z2, vec_z2_reset),
            Transform(vec_z1, vec_z1_new),
        )
        self.wait(0.5)

        # Step 7 — show same result point again
        dot2 = Dot(plane.n2p(z_sum), color=WHITE)
        self.play(FadeIn(dot2))
        self.wait(1)

        # Step 8 — show final vector and message
        vec_sum2 = Arrow(plane.n2p(0), plane.n2p(z_sum), buff=0, color=GREEN)
        self.play(GrowArrow(vec_sum2))
        self.wait(0.5)
        self.wait(10)



class ComplexConjugation(Scene):
    def construct(self):
        # Create Argand (complex) plane
        plane = ComplexPlane(
            x_range=[-3, 4],
            y_range=[-3, 3],
            background_line_style={"stroke_opacity": 0.4}
        ).add_coordinates()
        self.play(Create(plane))

        # Define complex number and its conjugate
        z = 2 + 1.5j
        z_conj = 2 - 1.5j

        # Points
        dot_z = Dot(plane.n2p(z), color=BLUE)
        dot_z_conj = Dot(plane.n2p(z_conj), color=ORANGE)

        # Labels
        label_z = MathTex("z = 2 + 1.5i", color=BLUE).next_to(dot_z, UP)
        label_z_conj = MathTex("\\overline{z} = 2 - 1.5i", color=ORANGE).next_to(dot_z_conj, DOWN)

        # Dotted vertical reflection line
        reflection_line = DashedLine(
            start=plane.n2p(z),
            end=plane.n2p(z_conj),
            color=WHITE
        )

        # Step 1 — show z
        self.play(FadeIn(dot_z), Write(label_z))
        self.wait(0.5)

        # Step 2 — reflect to get conjugate
        self.play(Create(reflection_line))
        self.play(FadeIn(dot_z_conj), Write(label_z_conj))
        self.wait(0.5)

        # Step 3 — show mirrored arrow
        arrow_z = Arrow(plane.n2p(0), plane.n2p(z), buff=0, color=BLUE)
        arrow_z_conj = Arrow(plane.n2p(0), plane.n2p(z_conj), buff=0, color=ORANGE)
        self.play(GrowArrow(arrow_z))
        self.wait(0.3)
        self.play(GrowArrow(arrow_z_conj))
        self.wait(1)
        self.wait(3)
