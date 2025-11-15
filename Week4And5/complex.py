from manim import *

class Polar(Scene):
    def construct(self):
        
        cartesian = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=6,
            y_length=6,
            tips=False
        ).add_coordinates().shift(LEFT * 3.5)
        
        cartesian_title = Text("Cartesian: z = x + iy").scale(0.6).next_to(cartesian,UP,buff=0.2).scale(0.8)

        polar = PolarPlane(
            radius_max=4,
            radius_step=1,
            size=6,
        ).add_coordinates().shift(RIGHT * 3.5)
        
        polar_title = MathTex("Polar: z = r e^{i\\theta}").scale(0.6).next_to(polar,UP,buff=0.2)

        self.add(cartesian, cartesian_title, polar, polar_title)

        r_tracker = ValueTracker(2)
        theta_tracker = ValueTracker(PI / 4)

        def get_x():
            return r_tracker.get_value() * np.cos(theta_tracker.get_value())
        
        def get_y():
            return r_tracker.get_value() * np.sin(theta_tracker.get_value())

        cartesian_dot = Dot(color=TEAL)
        cartesian_vec = Arrow(
            cartesian.c2p(0, 0),
            cartesian.c2p(get_x(), get_y()),
            buff=0, stroke_width=4, color=TEAL
        )
        x_line = DashedLine(cartesian.c2p(get_x(), 0), cartesian.c2p(get_x(), get_y()), color=BLUE)
        y_line = DashedLine(cartesian.c2p(0, get_y()), cartesian.c2p(get_x(), get_y()), color=DARK_BROWN)

        polar_dot = Dot(color=TEAL)
        polar_vec = Arrow(
            polar.get_origin(),
            polar.polar_to_point(r_tracker.get_value(), theta_tracker.get_value()),
            buff=0, stroke_width=4, color=TEAL
        )
        
        polar_arc = always_redraw(
            lambda: Arc(
                radius=0.5,
                start_angle=0,
                angle=theta_tracker.get_value(),
                color=RED
            ).move_arc_center_to(polar.get_origin())
        )

        r_label = always_redraw(
            lambda: VGroup(
                MathTex("r = ",color=TEAL),
                DecimalNumber(r_tracker.get_value(), num_decimal_places=2, color=TEAL)
            ).arrange(RIGHT, buff=0.2).next_to(polar_title,LEFT, buff = 0.5)
        )
        
        theta_label = always_redraw(
            lambda: VGroup(
                MathTex("\\theta = ",color=RED),
                DecimalNumber(theta_tracker.get_value(), num_decimal_places=2, color=RED),
                MathTex(" \\text{ rad}", color=RED)
            ).arrange(RIGHT, buff=0.2).next_to(r_label, DOWN)
        )

        x_label = always_redraw(
            lambda: VGroup(
                MathTex("x = ",color=DARK_BROWN),
                DecimalNumber(get_x(), num_decimal_places=2, color=DARK_BROWN)
            ).arrange(RIGHT, buff=0.2).to_edge(UL,buff=0).scale(0.7)
        )

        y_label = always_redraw(
            lambda: VGroup(
                MathTex("y = ",color=BLUE),
                DecimalNumber(get_y(), num_decimal_places=2, color=BLUE)
            ).arrange(RIGHT, buff=0.2).next_to(x_label, DOWN, buff=0.5).scale(0.7)
        )
        
        self.add(r_label, theta_label, x_label, y_label)

        cartesian_dot.add_updater(lambda d: d.move_to(cartesian.c2p(get_x(), get_y())))
        cartesian_vec.add_updater(
            lambda v: v.put_start_and_end_on(
                cartesian.c2p(0, 0), cartesian_dot.get_center()
            )
        )
        x_line.add_updater(
            lambda l: l.put_start_and_end_on(
                cartesian.c2p(get_x(), 0), cartesian_dot.get_center()
            )
        )
        y_line.add_updater(
            lambda l: l.put_start_and_end_on(
                cartesian.c2p(0, get_y()), cartesian_dot.get_center()
            )
        )
        
        polar_dot.add_updater(
            lambda d: d.move_to(polar.polar_to_point(r_tracker.get_value(), theta_tracker.get_value()))
        )
        polar_vec.add_updater(
            lambda v: v.put_start_and_end_on(
                polar.get_origin(), polar_dot.get_center()
            )
        )

        self.add(
            cartesian_dot, cartesian_vec, x_line, y_line,
            polar_dot, polar_vec, polar_arc
        )

        self.wait(1)
        
        self.play(r_tracker.animate.set_value(2.5), run_time=5)
        self.wait(1)
        
        self.play(theta_tracker.animate.set_value(5 * PI / 4), run_time=6)
        self.wait(1)
        
        self.play(
            r_tracker.animate.set_value(1),
            theta_tracker.animate.set_value(PI),
            run_time=9
        )
        self.wait(2)






from manim import *
import numpy as np

class Unity(Scene):
    def construct(self):
        plane = ComplexPlane(
            x_range=[-2, 2, 0.5],
            y_range=[-2, 2, 0.5],
            x_length=8,
            y_length=8,
            tips=True
        ).add_coordinates()
        
        origin = plane.n2p(0)
        point_one = plane.n2p(1)
        radius = np.linalg.norm(point_one - origin)
        
        unit_circle = Circle(radius=radius, color=YELLOW).move_to(origin)

        self.play(FadeIn(plane), Create(unit_circle))
        self.wait(0.5)

        current_polygon = Polygon(ORIGIN, color=BLUE, fill_opacity=0.3)
        current_roots = VGroup()
        
        k_str = "0"
        current_formula = MathTex(
            fr"\begin{{aligned}} z_k &= e^{{\frac{{2\pi i k}}{{1}}}} \\ n &= 1 \\ k &= {k_str} \end{{aligned}}",
            color=WHITE
        ).scale(0.8).to_corner(UL)

        self.add(current_polygon, current_roots, current_formula)
        
        for n in range(1, 11):
            
            new_vertices = []
            new_roots_list = []

            for k in range(n):
                angle = (2 * PI * k) / n
                z = np.exp(1j * angle)
                point = plane.n2p(z)
                
                new_vertices.append(point)
                
                if n <= 5:
                    new_roots_list.append(Vector(point, color=RED))
                else:
                    new_roots_list.append(Dot(point, color=RED))
            
            new_polygon = Polygon(*new_vertices, color=BLUE, fill_opacity=0.3)
            new_roots = VGroup(*new_roots_list)

            k_str = "0" if n == 1 else fr"0, \dots, {n-1}"
            new_formula = MathTex(
                fr"\begin{{aligned}} z_k &= e^{{\frac{{2\pi i k}}{{{n}}}}} \\ n &= {n} \\ k &= {k_str} \end{{aligned}}",
                color=WHITE
            ).scale(0.8).to_corner(UL)

            animations = []
            
            animations.append(ReplacementTransform(current_polygon, new_polygon))
            animations.append(ReplacementTransform(current_formula, new_formula))
            
            if n == 6:
                animations.append(FadeOut(current_roots))
                animations.append(FadeIn(new_roots))
            else:
                animations.append(ReplacementTransform(current_roots, new_roots))

            self.play(*animations, run_time=1.4)
            self.wait(0.6)
            
            current_polygon = new_polygon
            current_roots = new_roots
            current_formula = new_formula

        self.wait(3)