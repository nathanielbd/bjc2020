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
        self.wait()

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
        self.wait(2)
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
        self.play(Write(system))
        line = Line(UP*2.65+UP*MED_SMALL_BUFF+LEFT*0.35, DOWN*2.75+LEFT*0.35)
        line.set_color(RED)
        invisible_line = Line(DOWN*2.75+LEFT*0.35, DOWN*2.75).set_color(BLACK)
        self.play(Write(line))
        brace = Brace(invisible_line, DOWN, buff = 0.1)
        self.play(Write(brace))
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
        p_right = Line(sensor.get_center()+DOWN, sensor.get_center()+DOWN+LEFT*1.85)
        feedback = [
            Line(sensor.get_center()+DOWN*0.5, sensor.get_center()+DOWN), 
            p_right,
            Line(LEFT*2.5+DOWN*2, LEFT*4+DOWN*2),
            Line(LEFT*4+DOWN*2, LEFT*4+DOWN+DOWN*MED_LARGE_BUFF)
        ]
        bottom_label = TextMobject("Proportional ($K_p e(t)$)").set_color(YELLOW) \
                        .next_to(box, DOWN, MED_LARGE_BUFF)
        bottom_box = SurroundingRectangle(
            bottom_label, buff = SMALL_BUFF, color=YELLOW
        )
        feedback = [obj.set_stroke(width=8) for obj in feedback]
        self.play(
            Write(gravity),
            Write(left_arrow),
            Write(left_label),
            Write(right_arrow),
            Write(right_label),
            DrawBorderThenFill(box),
            Write(VGroup(*feedback)),
            Write(bottom_label),
            Write(prev_arrow),
            Write(prev_label),
            Write(sensor)
        )
        self.play(
            Write(brace)
        )
        self.play(
            DrawBorderThenFill(sensor_box)
        )
        self.play(
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
        self.play(DrawBorderThenFill(left))
        right = SurroundingRectangle(dots, color=RED)
        right.stretch(0.62, 0, about_edge=RIGHT)
        self.play(
            Transform(left, right),
            Write(integral)
        )

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
        p_right = Line(sensor.get_center()+DOWN, sensor.get_center()+DOWN+LEFT*1.85)
        feedback = [
            Line(sensor.get_center()+DOWN*0.5, sensor.get_center()+DOWN), 
            p_right,
            Line(LEFT*2.5+DOWN*2, LEFT*4+DOWN*2),
            Line(LEFT*4+DOWN*2, LEFT*4+DOWN+DOWN*MED_LARGE_BUFF)
        ]
        bottom_label = TextMobject("Proportional ($K_p e(t)$)").set_color(YELLOW) \
                        .next_to(box, DOWN, MED_LARGE_BUFF)
        bottom_box = SurroundingRectangle(
            bottom_label, buff = SMALL_BUFF, color=YELLOW
        )
        feedback = VGroup(*[obj.set_stroke(width=8) for obj in feedback])
        i_right = Line(sensor.get_center()+DOWN*2, sensor_box.get_center()+DOWN*2+LEFT*1.75)
        integral_loop  = [
            Line(sensor.get_center()+DOWN*0.5, sensor.get_center()+DOWN*2),
            i_right,
            Line(LEFT*2.6+DOWN*3, LEFT*4+DOWN*3),
            Line(LEFT*4+DOWN*3, LEFT*4+DOWN+DOWN*MED_LARGE_BUFF)
        ]
        integral_loop = VGroup(*[obj.set_stroke(width=8) for obj in integral_loop])
        integral_label = TextMobject("Integral ($K_i \\int_0^t e(\\tau) d\\tau$)").set_color(GREEN) \
                            .next_to(bottom_box, DOWN, MED_LARGE_BUFF)
        integral_box = SurroundingRectangle(
            integral_label, buff=SMALL_BUFF, color=GREEN
        )
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
        self.play(Write(dots))
        derivatives = [self.get_graph(
            lambda x: ((coords[i]['y']-coords[i-1]['y'])/(coords[i]['x']-coords[i-1]['x']))*x+(coords[i-1]['y']-coords[i-1]['x']*((coords[i]['y']-coords[i-1]['y'])/(coords[i]['x']-coords[i-1]['x']))),
            PURPLE
        ) for i in range(1,len(dots)) if coords[i]['x'] < 8000]
        self.play(ShowCreation(derivatives[0]))
        for x,y in zip(derivatives[::], derivatives[1::]):
            self.play(ReplacementTransform(x,y), run_time=0.02)
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
        p_right = Line(sensor.get_center()+DOWN, sensor.get_center()+DOWN+LEFT*1.85)
        feedback = [
            Line(sensor.get_center()+DOWN*0.5, sensor.get_center()+DOWN), 
            p_right,
            Line(LEFT*2.5+DOWN*2, LEFT*4+DOWN*2),
            Line(LEFT*4+DOWN*2, LEFT*4+DOWN+DOWN*MED_LARGE_BUFF)
        ]
        bottom_label = TextMobject("Proportional ($K_p e(t)$)").set_color(YELLOW) \
                        .next_to(box, DOWN, MED_LARGE_BUFF)
        bottom_box = SurroundingRectangle(
            bottom_label, buff = SMALL_BUFF, color=YELLOW
        )
        feedback = VGroup(*[obj.set_stroke(width=8) for obj in feedback])
        i_right = Line(sensor.get_center()+DOWN*2, sensor_box.get_center()+DOWN*2+LEFT*1.75)
        integral_loop  = [
            Line(sensor.get_center()+DOWN*0.5, sensor.get_center()+DOWN*2),
            i_right,
            Line(LEFT*2.7+DOWN*3, LEFT*4+DOWN*3),
            Line(LEFT*4+DOWN*3, LEFT*4+DOWN+DOWN*MED_LARGE_BUFF)
        ]
        integral_loop = VGroup(*[obj.set_stroke(width=8) for obj in integral_loop])
        integral_label = TextMobject("Integral ($K_i \\int_0^t e(\\tau) d\\tau$)").set_color(GREEN) \
                            .next_to(bottom_box, DOWN, MED_LARGE_BUFF)
        integral_box = SurroundingRectangle(
            integral_label, buff=SMALL_BUFF, color=GREEN
        )
        d_right = Line(sensor.get_center()+DOWN*3.5, sensor_box.get_center()+DOWN*3.5+LEFT*1.85)
        derivative_loop = [
            Line(sensor.get_center()+DOWN*0.5, sensor.get_center()+DOWN*3.5),
            d_right,
            Line(LEFT*2.5+DOWN*4.5, LEFT*4+DOWN*4.5),
            Line(LEFT*4+DOWN*4.5, LEFT*4+DOWN+DOWN*MED_LARGE_BUFF)
        ]
        derivative_loop = VGroup(*[obj.set_stroke(width=8) for obj in derivative_loop])
        derivative_label = TextMobject("Derivative ($K_d \\frac{de(t)}{dt}$)").set_color(PURPLE) \
                            .next_to(integral_box, DOWN, MED_LARGE_BUFF)
        derivative_box = SurroundingRectangle(
            derivative_label, buff=SMALL_BUFF, color=PURPLE
        )
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
