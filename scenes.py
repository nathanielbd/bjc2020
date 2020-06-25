#!/usr/bin/env python

from manimlib.imports import *

# usage: python3 -m manim scenes.py SceneName -pl

# TODO: clean this up and document after the competition

class TikzMobject(TextMobject):
    CONFIG = {
        "stroke_width":3,
        "fill_opacity":0,
        "stroke_opacity":1
    }

class Segue(Scene):
    def construct(self):
        question = TextMobject("How does a Segway balance?")
        segue = VGroup(*TextMobject("Segue $\\rightarrow$ ", "Cybernetics!"))
        segue[1].set_color_by_gradient(GREEN, RED)
        self.play(Write(question))
        self.wait(2)
        self.play(Transform(question, segue))
        maintain = VGroup(*TextMobject("Complex systems ", "$\\nrightarrow$ chaos"))
        maintain[0].set_color(GREEN)
        maintain[1].set_color(RED)
        self.wait(2)
        self.play(
            FadeOutAndShiftDown(question),
            Write(maintain)
        )
        self.wait(2)

class GravityBlock(Scene):
    def construct(self):
        left_arrow = Arrow(
            start=LEFT*3+UP, end=LEFT*2+UP,
        )
        left_arrow.set_stroke(width=2)
        left_label = TextMobject("Random error",
        )
        left_label.next_to(left_arrow, LEFT, MED_SMALL_BUFF)
        gravity = TextMobject("Gravity")
        box = SurroundingRectangle(gravity, 
            buff=LARGE_BUFF, color=WHITE
        )
        right_arrow = Arrow(
            start=RIGHT*2, end=RIGHT*4,
        ).set_color(RED)
        right_label = TextMobject("$e(t)$",
        ).set_color(RED)
        right_label.next_to(right_arrow, RIGHT, MED_SMALL_BUFF)
        prev_arrow = Arrow(
            start=LEFT*3+DOWN, end=LEFT*2+DOWN
        )
        prev_arrow.set_stroke(width=2)
        prev_label = TextMobject("Previous error")
        prev_label.next_to(prev_arrow, LEFT, MED_SMALL_BUFF)
        feedback = [
            Line(RIGHT*4+RIGHT*MED_LARGE_BUFF+DOWN*MED_LARGE_BUFF, RIGHT*4+RIGHT*MED_LARGE_BUFF+DOWN*3),
            Line(RIGHT*4+RIGHT*MED_LARGE_BUFF+DOWN*3, LEFT*4+DOWN*3),
            Line(LEFT*4+DOWN*3, LEFT*4+DOWN+DOWN*MED_LARGE_BUFF)
        ]
        feedback = [obj.set_stroke(width=2) for obj in feedback]
        lower = VGroup(*feedback)
        self.play(
            Write(left_arrow),
            Write(left_label),
            Write(gravity),
            DrawBorderThenFill(box),
            Write(right_arrow),
            Write(right_label),
            Write(prev_arrow),
            Write(prev_label),
            Write(lower),
        )
        self.wait(1)
        self.play(
            Transform(prev_arrow, prev_arrow.copy().set_stroke(width=4)),
            Transform(right_arrow, right_arrow.copy().set_stroke(width=4)),
            Transform(lower, VGroup(*[obj.copy().set_stroke(width=4) for obj in feedback])),
        )
        self.wait(0.5)
        self.play(
            Transform(prev_arrow, prev_arrow.copy().set_stroke(width=8)),
            Transform(right_arrow, right_arrow.copy().set_stroke(width=8)),
            Transform(lower, VGroup(*[obj.copy().set_stroke(width=8) for obj in feedback])),
        )
        self.wait(0.5)
        self.play(
            Transform(prev_arrow, prev_arrow.copy().set_stroke(width=14)),
            Transform(right_arrow, right_arrow.copy().set_stroke(width=14)),
            Transform(lower, VGroup(*[obj.copy().set_stroke(width=14) for obj in feedback])),
        )
        self.wait(0.5)
        self.play(
            Transform(prev_arrow, prev_arrow.copy().set_stroke(width=22)),
            Transform(right_arrow, right_arrow.copy().set_stroke(width=22)),
            Transform(lower, VGroup(*[obj.copy().set_stroke(width=22) for obj in feedback])),
        )

class Closeup(Scene):
    def construct(self):
        aha = TextMobject("Changing the feedback loop")
        self.play(Write(aha))
        system = TikzMobject(
            r"""
            \begin{tikzpicture}[
                circlenode/.style={circle, draw},
                rectanglenode/.style={rectangle, draw, minimum width=2em},
                wheelnode/.style={circle, draw, minimum size=1.5em}
            ]
                \node[circlenode] at (-0.25,0) {};
                \draw (-0.25,0)--(0,-4);
                \node[rectanglenode] at (0,-4) {};
                \node[wheelnode] at (0.5,-4) {};
                \node[wheelnode] at (-0.5, -4) {};
            \end{tikzpicture}
            """
        )
        self.wait(1)
        self.play(
            FadeOutAndShiftDown(aha),
            Write(system)
        )
        line = Line(UP*2.65+UP*MED_SMALL_BUFF+LEFT*0.35, DOWN*2.75+LEFT*0.35)
        line.set_color(RED)
        invisible_line = Line(DOWN*2.75+LEFT*0.35, DOWN*2.75).set_color(BLACK)
        self.play(Write(line))
        brace = Brace(invisible_line, DOWN, buff = 0.1)
        self.play(Write(brace))
        self.wait(3)
        system_final = TikzMobject(
            r"""
            \begin{tikzpicture}[
                circlenode/.style={circle, draw},
                rectanglenode/.style={rectangle, draw, minimum width=2em},
                wheelnode/.style={circle, draw, minimum size=1.5em}
            ]
                \node[circlenode] at (-0.25,0) {};
                \draw (-0.25,0)--(-0.25,-4);
                \node[rectanglenode] at (-0.25,-4) {};
                \node[wheelnode] at (0.25,-4) {};
                \node[wheelnode] at (-0.75, -4) {};
            \end{tikzpicture}
            """
        ).shift(LEFT*0.35)
        arrow = Arrow(start=ORIGIN, end=LEFT).set_color(YELLOW)
        self.play(
            Write(arrow)
        )
        self.wait(2)
        self.play(
            FadeOutAndShiftDown(arrow),
            FadeOutAndShiftDown(invisible_line),
            FadeOutAndShiftDown(line),
            FadeOutAndShiftDown(brace),
            Transform(system, system_final)
        )
        self.wait()

class Proportional(Scene):
    def construct(self):
        left_arrow = Arrow(
            start=LEFT*3+UP, end=LEFT*2+UP,
        )
        left_arrow.set_stroke(width=8)
        left_label = TextMobject("Random error",
        )
        left_label.next_to(left_arrow, LEFT, MED_SMALL_BUFF)
        gravity = TextMobject("Gravity")
        box = SurroundingRectangle(gravity, 
            buff=LARGE_BUFF, color=WHITE
        )
        right_arrow = Arrow(
            start=RIGHT*2, end=RIGHT*4,
        )
        right_label = TextMobject("$e(t)$",
        )
        right_label.next_to(right_arrow, RIGHT, MED_SMALL_BUFF)
        brace = Brace(right_label, DOWN, buff=0.1)
        prev_arrow = Arrow(
            start=LEFT*3+DOWN, end=LEFT*2+DOWN
        )
        prev_arrow.set_stroke(width=8)
        prev_label = TextMobject("wheels go brrr")
        prev_label.next_to(prev_arrow, LEFT, MED_SMALL_BUFF)
        sensor = TextMobject("Sensor").next_to(right_label, DOWN, MED_LARGE_BUFF).set_color(BLUE)
        sensor_box = SurroundingRectangle(
            sensor, buff=SMALL_BUFF, color=BLUE
        )
        bottom_label = TextMobject("Proportional ($K_p e(t)$)").set_color(YELLOW) \
                        .next_to(box, DOWN, MED_LARGE_BUFF)
        bottom_box = SurroundingRectangle(
            bottom_label, buff = SMALL_BUFF, color=YELLOW
        )
        p_right = Line([sensor.get_center()[0], bottom_label.get_center()[1], 0], bottom_label.get_center()+RIGHT*2.5)
        feedback = [
            Line(sensor.get_center()+DOWN*0.5, [sensor.get_center()[0], bottom_label.get_center()[1], 0]), 
            p_right,
            Line([0, bottom_label.get_center()[1], 0]+LEFT*2.5, [prev_label.get_center()[0], bottom_label.get_center()[1], 0]),
            Line([prev_label.get_center()[0], bottom_label.get_center()[1], 0], prev_label.get_center()+DOWN*0.5)
        ]
        feedback = [obj.set_stroke(width=8) for obj in feedback]
        self.play(
            Write(gravity),
            Write(left_arrow),
            Write(left_label),
            Write(right_arrow),
            Write(right_label),
            DrawBorderThenFill(box),
            # Write(VGroup(*feedback)),
            # Write(bottom_label),
            # Write(prev_arrow),
            # Write(prev_label),
            # Write(sensor)
        )
        self.play(
            Write(sensor),
            DrawBorderThenFill(sensor_box)
        )
        self.play(
            Write(brace)
        )
        self.play(
            Write(VGroup(*feedback)),
            Write(prev_arrow),
            Write(prev_label)
        )
        self.wait(1)
        self.play(
            Write(bottom_label),
            DrawBorderThenFill(bottom_box)
        )
        self.wait()

import json

class Auc(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 8000,
        "y_min": -1.8,
        "y_max": 0.2,
        "x_tick_frequency": 1000,
        "y_tick_frequency": 0.2,
        "graph_origin": UP*2+LEFT*5,
        "x_axis_label": "$t$",
        "y_axis_label": "$e(t)$"
    }

    def construct(self):
        self.setup_axes(animate=True)
        with open('../bjc2020/demo_prop_data.json') as json_file:
            coords = json.load(json_file)
        # for coord in coords:
            # print(f"x: {coord['x']}, y: {coord['y']}")
        dots = VGroup(*[Dot(point=self.coords_to_point(coord['x'],coord['y']), radius=0.03, color=BLUE) for coord in coords if coord['x'] < 8000])
        self.play(Write(dots))
        integral = VGroup(*[Line(self.coords_to_point(coord['x'],0), self.coords_to_point(coord['x'],coord['y']), stroke_opacity=0.3).set_color(BLUE).set_stroke(width=8) for coord in coords if coord['x'] < 8000])
        left = SurroundingRectangle(dots)
        left.stretch(0.38, 0, about_edge=LEFT)
        self.wait(1)
        self.play(DrawBorderThenFill(left))
        right = SurroundingRectangle(dots, color=RED)
        right.stretch(0.62, 0, about_edge=RIGHT)
        self.wait(1)
        self.play(
            Transform(left, right)
        )
        self.wait(3)
        self.play(
            Write(integral)
        )
        self.wait(4)

class Integral(Scene):
    def construct(self):
        left_arrow = Arrow(
            start=LEFT*3+UP, end=LEFT*2+UP,
        )
        left_arrow.set_stroke(width=8)
        left_label = TextMobject("Random error",
        )
        left_label.next_to(left_arrow, LEFT, MED_SMALL_BUFF)
        gravity = TextMobject("Gravity")
        box = SurroundingRectangle(gravity, 
            buff=LARGE_BUFF, color=WHITE
        )
        right_arrow = Arrow(
            start=RIGHT*2, end=RIGHT*4,
        )
        right_label = TextMobject("$e(t)$",
        )
        right_label.next_to(right_arrow, RIGHT, MED_SMALL_BUFF)
        brace = Brace(right_label, DOWN, buff=0.1)
        prev_arrow = Arrow(
            start=LEFT*3+DOWN, end=LEFT*2+DOWN
        )
        prev_arrow.set_stroke(width=8)
        prev_label = TextMobject("wheels go brrr")
        prev_label.next_to(prev_arrow, LEFT, MED_SMALL_BUFF)
        sensor = TextMobject("Sensor").next_to(right_label, DOWN, MED_LARGE_BUFF).set_color(BLUE)
        sensor_box = SurroundingRectangle(
            sensor, buff=SMALL_BUFF, color=BLUE
        )
        bottom_label = TextMobject("Proportional ($K_p e(t)$)").set_color(YELLOW) \
                        .next_to(box, DOWN, MED_LARGE_BUFF)
        bottom_box = SurroundingRectangle(
            bottom_label, buff = SMALL_BUFF, color=YELLOW
        )
        p_right = Line([sensor.get_center()[0], bottom_label.get_center()[1], 0], bottom_label.get_center()+RIGHT*2.5)
        feedback = [
            Line(sensor.get_center()+DOWN*0.5, [sensor.get_center()[0], bottom_label.get_center()[1], 0]), 
            p_right,
            Line([0, bottom_label.get_center()[1], 0]+LEFT*2.5, [prev_label.get_center()[0], bottom_label.get_center()[1], 0]),
            Line([prev_label.get_center()[0], bottom_label.get_center()[1], 0], prev_label.get_center()+DOWN*0.5)
        ]
        feedback = VGroup(*[obj.set_stroke(width=8) for obj in feedback])
        integral_label = TextMobject("Integral ($K_i \\int_0^t e(\\tau) d\\tau$)").set_color(GREEN) \
                            .next_to(bottom_box, DOWN, MED_LARGE_BUFF)
        integral_box = SurroundingRectangle(
            integral_label, buff=SMALL_BUFF, color=GREEN
        )
        i_right = Line([sensor.get_center()[0], integral_label.get_center()[1], 0], integral_label.get_center()+RIGHT*2.6)
        integral_loop  = [
            Line(sensor.get_center()+DOWN*0.5, [sensor.get_center()[0], integral_label.get_center()[1], 0]),
            i_right,
            Line(integral_label.get_center()+LEFT*2.6, [prev_label.get_center()[0], integral_label.get_center()[1], 0]),
            Line([prev_label.get_center()[0], integral_label.get_center()[1], 0], prev_label.get_center()+DOWN*0.5)
        ]
        integral_loop = VGroup(*[obj.set_stroke(width=8) for obj in integral_loop])
        all = [
            gravity, left_arrow, left_label, right_arrow, right_label, box, feedback, bottom_label,
            prev_arrow, prev_label, sensor, brace, sensor_box, bottom_box, integral_label, integral_loop,
            integral_box
        ]
        VGroup(*all).shift(UP)
        self.play(
            Write(gravity),
            Write(left_arrow),
            Write(left_label),
            Write(right_arrow),
            Write(right_label),
            DrawBorderThenFill(box),
            Write(feedback),
            Write(bottom_label),
            Write(prev_arrow),
            Write(prev_label),
            Write(sensor),
            Write(brace),
            DrawBorderThenFill(sensor_box),
            DrawBorderThenFill(bottom_box), 
            Write(integral_label),
            Write(integral_loop)
        )
        self.play(
            DrawBorderThenFill(integral_box)
        )
        self.wait()

class Overshoot(Scene):
    def construct(self):
        system = TikzMobject(
            r"""
            \begin{tikzpicture}[
                circlenode/.style={circle, draw},
                rectanglenode/.style={rectangle, draw, minimum width=2em},
                wheelnode/.style={circle, draw, minimum size=1.5em}
            ]
                \node[circlenode] at (-0.25,0) {};
                \draw (-0.25,0)--(0,-4);
                \node[rectanglenode] at (0,-4) {};
                \node[wheelnode] at (0.5,-4) {};
                \node[wheelnode] at (-0.5, -4) {};
            \end{tikzpicture}
            """
        )
        line = Line(UP*2.65+UP*MED_SMALL_BUFF+LEFT*0.35, DOWN*2.75+LEFT*0.35)
        line.set_color(RED)
        arrow = Arrow(start=ORIGIN, end=LEFT).set_color(YELLOW)
        self.play(
            Write(system),
            Write(line)# ,
            # Write(arrow)
        )
        # invisible_line = Line(DOWN*2.75+LEFT*0.35, DOWN*2.75).set_color(BLACK)
        # brace = Brace(invisible_line, DOWN, buff = 0.1)
        # self.play(Write(brace))
        self.wait(1)
        self.play(
            Write(arrow)
        )
        system_final = TikzMobject(
            r"""
            \begin{tikzpicture}[
                circlenode/.style={circle, draw},
                rectanglenode/.style={rectangle, draw, minimum width=2em},
                wheelnode/.style={circle, draw, minimum size=1.5em}
            ]
                \node[circlenode] at (-0.25,0) {};
                \draw (-0.25,0)--(-0.25,-4);
                \node[rectanglenode] at (-0.25,-4) {};
                \node[wheelnode] at (0.25,-4) {};
                \node[wheelnode] at (-0.75, -4) {};
            \end{tikzpicture}
            """
        ).shift(LEFT*0.35)
        self.wait(1)
        self.play(
            FadeOutAndShiftDown(arrow),
            # FadeOutAndShiftDown(invisible_line),
            # FadeOutAndShiftDown(line),
            # FadeOutAndShiftDown(brace),
            Transform(system, system_final)
        )
        system_overshoot = TikzMobject(
            r"""
            \begin{tikzpicture}[
                circlenode/.style={circle, draw},
                rectanglenode/.style={rectangle, draw, minimum width=2em},
                wheelnode/.style={circle, draw, minimum size=1.5em}
            ]
                \node[circlenode] at (-0.5,0) {};
                \draw (-0.5,0)--(-0.75,-4);
                \node[rectanglenode] at (-0.75,-4) {};
                \node[wheelnode] at (-0.25,-4) {};
                \node[wheelnode] at (-1.25, -4) {};
            \end{tikzpicture}
            """
        ).shift(LEFT*1.05)
        self.wait(1)
        self.play(
            # FadeOutAndShiftDown(line),
            # Write(line.shift(LEFT*0.35)),
            Transform(line, line.copy().shift(LEFT*0.35)),
            Transform(system, system_overshoot)
        )
        self.wait()

class Tangent(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 8000,
        "y_min": -0.4,
        "y_max": 1.6,
        "x_tick_frequency": 1000,
        "y_tick_frequency": 0.2,
        "x_axis_label": "$t$",
        "y_axis_label": "$e(t)$"
    }
    def construct(self):
        self.setup_axes(animate=True)
        with open('../bjc2020/demo_int_data.json') as json_file:
            coords = json.load(json_file)
        # for coord in coords:
            # print(f"x: {coord['x']}, y: {coord['y']}")
        dots = VGroup(*[Dot(point=self.coords_to_point(coord['x'],coord['y']), radius=0.03, color=BLUE) for coord in coords if coord['x'] < 8000])
        self.play(Write(dots), run_time=0.5)
        inflections = [3950, 4375, 4775, 5200, 5600, 6020, 6460, 7000]
        arrow = Arrow(start=self.coords_to_point(3950, 0)+DOWN, end=self.coords_to_point(3950, 0))
        self.play(Write(arrow), run_time=0.5)
        for inflection in inflections[1:]:
            self.play(Transform(arrow, Arrow(start=self.coords_to_point(inflection, 0)+DOWN, end=self.coords_to_point(inflection, 0))), run_time=0.2)
            self.play(Write(Dot(point=self.coords_to_point(inflection,0), radius=0.05, color=YELLOW)), run_time=0.2)
        self.play(FadeOutAndShiftDown(arrow))
        flat_curve = self.get_graph(lambda x: 4/(x+1), GREEN)
        self.play(ShowCreation(flat_curve), FadeOutAndShiftDown(dots))
        self.wait(4)
        self.play(FadeOutAndShiftDown(flat_curve), FadeIn(dots))
        derivatives = [self.get_graph(
            # point slope form in a one-liner lambda func is ugly...
            lambda x: ((coords[i]['y']-coords[i-1]['y'])/(coords[i]['x']-coords[i-1]['x']))*x+(coords[i-1]['y']-coords[i-1]['x']*((coords[i]['y']-coords[i-1]['y'])/(coords[i]['x']-coords[i-1]['x']))),
            PURPLE
        ) for i in range(1,len(dots)) if coords[i]['x'] < 8000]
        slopes = [[i, (coords[i]['y']-coords[i-1]['y'])/(coords[i]['x']-coords[i-1]['x'])] for i in range(1,len(dots)) if coords[i]['x'] < 8000]
        self.play(ShowCreation(derivatives[0]))
        for x,y,z in zip(derivatives[::], derivatives[1::], slopes):
            self.play(ReplacementTransform(x,y), run_time=0.0002)
            self.add(Dot(point=self.coords_to_point(z[0], z[1]), radius=0.03, color=PURPLE))
        # for j in range(0, len(derivatives)-1):
        #     self.play(ShowCreation(derivatives[j]))
        #     self.play(Transform(derivatives[j], derivatives[j+1]))
        # derivative = VGroup(*[Line(self.coords) for coord in coords[1:] if coord['x'] < 8000])

class PID(Scene):
    def construct(self):
        left_arrow = Arrow(
            start=LEFT*3+UP, end=LEFT*2+UP,
        )
        left_arrow.set_stroke(width=8)
        left_label = TextMobject("Random error",
        )
        left_label.next_to(left_arrow, LEFT, MED_SMALL_BUFF)
        gravity = TextMobject("Gravity")
        box = SurroundingRectangle(gravity, 
            buff=LARGE_BUFF, color=WHITE
        )
        right_arrow = Arrow(
            start=RIGHT*2, end=RIGHT*4,
        )
        right_label = TextMobject("$e(t)$",
        )
        right_label.next_to(right_arrow, RIGHT, MED_SMALL_BUFF)
        brace = Brace(right_label, DOWN, buff=0.1)
        prev_arrow = Arrow(
            start=LEFT*3+DOWN, end=LEFT*2+DOWN
        )
        prev_arrow.set_stroke(width=8)
        prev_label = TextMobject("wheels go brrr")
        prev_label.next_to(prev_arrow, LEFT, MED_SMALL_BUFF)
        sensor = TextMobject("Sensor").next_to(right_label, DOWN, MED_LARGE_BUFF).set_color(BLUE)
        sensor_box = SurroundingRectangle(
            sensor, buff=SMALL_BUFF, color=BLUE
        )
        bottom_label = TextMobject("Proportional ($K_p e(t)$)").set_color(YELLOW) \
                        .next_to(box, DOWN, MED_LARGE_BUFF)
        bottom_box = SurroundingRectangle(
            bottom_label, buff = SMALL_BUFF, color=YELLOW
        )
        p_right = Line([sensor.get_center()[0], bottom_label.get_center()[1], 0], bottom_label.get_center()+RIGHT*2.5)
        feedback = [
            Line(sensor.get_center()+DOWN*0.5, [sensor.get_center()[0], bottom_label.get_center()[1], 0]), 
            p_right,
            Line([0, bottom_label.get_center()[1], 0]+LEFT*2.5, [prev_label.get_center()[0], bottom_label.get_center()[1], 0]),
            Line([prev_label.get_center()[0], bottom_label.get_center()[1], 0], prev_label.get_center()+DOWN*0.5)
        ]
        feedback = VGroup(*[obj.set_stroke(width=8) for obj in feedback])
        integral_label = TextMobject("Integral ($K_i \\int_0^t e(\\tau) d\\tau$)").set_color(GREEN) \
                            .next_to(bottom_box, DOWN, MED_LARGE_BUFF)
        integral_box = SurroundingRectangle(
            integral_label, buff=SMALL_BUFF, color=GREEN
        )
        i_right = Line([sensor.get_center()[0], integral_label.get_center()[1], 0], integral_label.get_center()+RIGHT*2.6)
        integral_loop  = [
            Line(sensor.get_center()+DOWN*0.5, [sensor.get_center()[0], integral_label.get_center()[1], 0]),
            i_right,
            Line(integral_label.get_center()+LEFT*2.6, [prev_label.get_center()[0], integral_label.get_center()[1], 0]),
            Line([prev_label.get_center()[0], integral_label.get_center()[1], 0], prev_label.get_center()+DOWN*0.5)
        ]
        integral_loop = VGroup(*[obj.set_stroke(width=8) for obj in integral_loop])
        derivative_label = TextMobject("Derivative ($K_d \\frac{de(t)}{dt}$)").set_color(PURPLE) \
                            .next_to(integral_box, DOWN, MED_LARGE_BUFF)
        derivative_box = SurroundingRectangle(
            derivative_label, buff=SMALL_BUFF, color=PURPLE
        )
        d_right = Line([sensor.get_center()[0], derivative_label.get_center()[1], 0], derivative_label.get_center()+RIGHT*2.4)
        derivative_loop = [
            Line(sensor.get_center()+DOWN*0.5, [sensor.get_center()[0], derivative_label.get_center()[1], 0]),
            d_right,
            Line(derivative_label.get_center()+LEFT*2.4, [prev_label.get_center()[0], derivative_label.get_center()[1], 0]),
            Line([prev_label.get_center()[0], derivative_label.get_center()[1], 0], prev_label.get_center()+DOWN*0.5)
        ]
        derivative_loop = VGroup(*[obj.set_stroke(width=8) for obj in derivative_loop])
        all = [
            gravity, left_arrow, left_label, right_arrow, right_label, box, feedback, bottom_label,
            prev_arrow, prev_label, sensor, brace, sensor_box, bottom_box, integral_label, integral_loop,
            integral_box, derivative_loop, derivative_label, derivative_box
        ]
        VGroup(*all).shift(UP*2)
        self.play(
            Write(gravity),
            Write(left_arrow),
            Write(left_label),
            Write(right_arrow),
            Write(right_label),
            DrawBorderThenFill(box),
            Write(feedback),
            Write(bottom_label),
            Write(prev_arrow),
            Write(prev_label),
            Write(sensor),
            Write(brace),
            DrawBorderThenFill(sensor_box),
            Write(integral_label),
            Write(integral_loop),
            Write(derivative_loop),
            Write(derivative_label)
        )
        self.play(
            DrawBorderThenFill(bottom_box) 
        )
        self.play(
            DrawBorderThenFill(integral_box)
        )
        self.play(DrawBorderThenFill(derivative_box))
        self.play(FadeOutAndShiftDown(VGroup(*all)))
        first = VGroup(*TextMobject("Proportional", " + ", "Integral", " + ", "Derivative"))
        first[0].set_color(YELLOW)
        first[2].set_color(GREEN)
        first[4].set_color(PURPLE)
        second = VGroup(*TextMobject("PID ", "Controller"))
        second[0].set_color_by_gradient(YELLOW, GREEN)
        second[1].set_color_by_gradient(GREEN, PURPLE)
        self.play(Write(first))
        self.play(Transform(first, second))
        self.wait()

class ThankYou(Scene):
    def construct(self):
        love = TextMobject("Hand-coded with $\\heartsuit$ using ", "Manim ", "and ", "matter.js")
        love[1].set_color(BLUE)
        love[3].set_color(YELLOW)
        demo = TextMobject("Tune your own PID controller: ", "https://SASE-Labs-2021.gitub.io/inverted-pendulum")
        demo[1].set_color(GREEN)
        learn = TextMobject("How to tune a PID controller: ", "https://nathanielbd.github.io/posts/segue-from-segways/")
        learn[1].set_color(GREEN)
        love.shift(UP*1.5)
        learn.shift(DOWN*1.5)
        segway = TextMobject("RIP Segway (2001-2020)")
        segway.shift(DOWN*3)
        self.play(
            Write(love)
        )
        self.play(
            Write(demo)
        )
        self.play(
            Write(learn)
        )
        self.play(
            Write(segway)
        )
        self.wait()
