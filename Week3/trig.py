from manim import *
# a more efficient approach would have been using parametric curve :) not points..
class Trig(Scene):
    def construct(self):
        # Slightly smaller circle positioned to the left
        circle = Circle(radius=2.5, color=WHITE).shift(LEFT * 4)
        self.play(Create(circle))
        self.wait(0.5)


        # Moving dot around circle (angle θ)
        dot = Dot(color=YELLOW).move_to(circle.point_at_angle(0))
        theta_tracker = ValueTracker(0)  # angle in radians

        dot_path = TracedPath(
            dot.get_center,   # traces the position of the dot
            stroke_color= YELLOW,
            stroke_width=10     # thicker line
        )
        # Dynamic position on circle
        dot.add_updater(
            lambda d: d.move_to(
                circle.point_at_angle(theta_tracker.get_value())
            )
        )

        # Small stroked circle on the circumference to highlight θ
        theta_dot = always_redraw(
            lambda: Circle(
                radius=0.1,
                color=YELLOW,
                fill_opacity=0,  # No fill, only stroke
                stroke_width=4
            ).move_to(circle.point_at_angle(theta_tracker.get_value()))
        )

        # Lines for sine (vertical) and cosine (horizontal) in the circle
        sine_line = always_redraw(
            lambda: Line(
                start=[dot.get_x(), 0, 0],
                end=[dot.get_x(), dot.get_y(), 0],
                color=RED,
                stroke_width=10
            )
        )
        cosine_line = always_redraw(
            lambda: Line(
                start=circle.get_center(),  # Starts from circle's center
                end=[dot.get_x(), 0, 0],
                color=BLUE,
                stroke_width=10
            )
        )

        # Larger sine and cosine graphs on the right
        sine_graph_axes = Axes(
            x_range=[0, 2 * PI, PI/2],
            y_range=[-1, 1, 0.5],
            x_length=5,  # Scaled up
            y_length=3,  # Scaled up
        ).shift(RIGHT * 3 + UP * 2)
        cosine_graph_axes = Axes(
            x_range=[0, 2 * PI, PI/2],
            y_range=[-1, 1, 0.5],
            x_length=5,  # Scaled up
            y_length=3,  # Scaled up
  
        ).shift(RIGHT * 3 + DOWN * 2)

        sine_points = []
        cosine_points = []

        def update_sine_points():
            theta = theta_tracker.get_value()
            sine_points.append([theta, np.sin(theta), 0])
            return VGroup(*[Dot(sine_graph_axes.c2p(p[0], p[1]), color=RED) for p in sine_points])

        def update_cosine_points():
            theta = theta_tracker.get_value()
            cosine_points.append([theta, np.cos(theta), 0])
            return VGroup(*[Dot(cosine_graph_axes.c2p(p[0], p[1]), color=BLUE) for p in cosine_points])

        sine_plot = always_redraw(update_sine_points)
        cosine_plot = always_redraw(update_cosine_points)

        # Corresponding lines in the sine and cosine graphs
        sine_graph_line = always_redraw(
            lambda: Line(
                start=sine_graph_axes.c2p(theta_tracker.get_value(), 0),
                end=sine_graph_axes.c2p(theta_tracker.get_value(), np.sin(theta_tracker.get_value())),
                color=RED,
                stroke_width=10
            )
        )
        cosine_graph_line = always_redraw(
            lambda: Line(
                start=cosine_graph_axes.c2p(theta_tracker.get_value(), 0),
                end=cosine_graph_axes.c2p(theta_tracker.get_value(), np.cos(theta_tracker.get_value())),
                color=BLUE,
                stroke_width=10
            )
        )

        # Labels for sine and cosine, fixed position, updating values in radians
        sine_label = always_redraw(
            lambda: MathTex(f"\\sin(\\theta) = {np.sin(theta_tracker.get_value()):.2f}", color=RED)
            .next_to(sine_graph_axes, LEFT, buff=0.1).scale(0.9).shift(UP*1))
        cosine_label = always_redraw(
            lambda: MathTex(f"\\cos(\\theta) = {np.cos(theta_tracker.get_value()):.2f}", color=BLUE)
            .next_to(cosine_graph_axes, LEFT, buff=0.1).scale(0.9).shift(DOWN*1)
        )

        # Theta label between sine and cosine graphs
        theta_label = always_redraw(
            lambda: MathTex(f"\\theta = {theta_tracker.get_value():.2f}", color=YELLOW)
            .move_to(RIGHT * 3)  # Centered between graphs
        )

        # Add all elements
        self.add(dot_path)  # Add trace path first
        self.add(dot, theta_dot, sine_line, cosine_line, sine_graph_axes, cosine_graph_axes, sine_plot, cosine_plot, sine_graph_line, cosine_graph_line, sine_label, cosine_label, theta_label)
        self.wait(0.5)

        # Animate one full rotation
        self.play(theta_tracker.animate.set_value(2 * PI), run_time=20, rate_func=linear)
        self.wait(5)
