#!/usr/bin/env python

from manimlib.imports import *

# usage: python3 -m manim scenes.py SceneName -pl

class TikzMobject(TextMobject):
    CONFIG = {
        "stroke_width":3,
        "fill_opacity":0,
        "stroke_opacity":1
    }

class GravityBlock(Scene):
    def construct(self):
        left_arrow = Arrow(
            start=LEFT*3+UP, end=LEFT*2+UP,
        )
        left_arrow.set_stroke(width=8)
        left_label = TextMobject("Random error",
        )
        left_label.next_to(left_arrow, LEFT, MED_SMALL_BUFF)
        self.add(left_arrow)
        self.add(left_label)
        gravity = TextMobject("Gravity")
        box = SurroundingRectangle(gravity, 
            buff=LARGE_BUFF, color=WHITE
        )
        self.play(
            Write(gravity),
            DrawBorderThenFill(box)
        )
        right_arrow = Arrow(
            start=RIGHT*2, end=RIGHT*4,
        )
        right_label = TextMobject("$e(t)$",
        )
        right_label.next_to(right_arrow, RIGHT, MED_SMALL_BUFF)
        self.add(right_arrow)
        self.add(right_label)
        prev_arrow = Arrow(
            start=LEFT*3+DOWN, end=LEFT*2+DOWN
        )
        prev_arrow.set_stroke(width=8)
        prev_label = TextMobject("Previous error")
        prev_label.next_to(prev_arrow, LEFT, MED_SMALL_BUFF)
        feedback = [
            Line(RIGHT*4+RIGHT*MED_LARGE_BUFF+DOWN*MED_LARGE_BUFF, RIGHT*4+RIGHT*MED_LARGE_BUFF+DOWN*3),
            Line(RIGHT*4+RIGHT*MED_LARGE_BUFF+DOWN*3, LEFT*4+DOWN*3),
            Line(LEFT*4+DOWN*3, LEFT*4+DOWN+DOWN*MED_LARGE_BUFF)
        ]
        feedback = [obj.set_stroke(width=8) for obj in feedback]
        self.add(*feedback)
        self.add(prev_arrow)
        self.add(prev_label)
        self.wait()

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
        self.play(Write(line))
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
        self.add(left_arrow)
        self.add(left_label)
        gravity = TextMobject("Gravity")
        box = SurroundingRectangle(gravity, 
            buff=LARGE_BUFF, color=WHITE
        )
        self.play(
            Write(gravity),
            DrawBorderThenFill(box)
        )
        right_arrow = Arrow(
            start=RIGHT*2, end=RIGHT*4,
        )
        right_label = TextMobject("$e(t)$",
        )
        right_label.next_to(right_arrow, RIGHT, MED_SMALL_BUFF)
        self.add(right_arrow)
        self.add(right_label)
        prev_arrow = Arrow(
            start=LEFT*3+DOWN, end=LEFT*2+DOWN
        )
        prev_arrow.set_stroke(width=8)
        prev_label = TextMobject("wheels go brrr")
        prev_label.next_to(prev_arrow, LEFT, MED_SMALL_BUFF)
        bottom = Line(RIGHT*4+RIGHT*MED_LARGE_BUFF+DOWN*2, LEFT*4+DOWN*2)
        feedback = [
            Line(RIGHT*4+RIGHT*MED_LARGE_BUFF+DOWN*MED_LARGE_BUFF, RIGHT*4+RIGHT*MED_LARGE_BUFF+DOWN*2),
            bottom,
            Line(LEFT*4+DOWN*2, LEFT*4+DOWN+DOWN*MED_LARGE_BUFF)
        ]
        bottom_label = TextMobject("Proportional ($K_p e(t)$)")
        bottom_label.next_to(bottom, DOWN, MED_SMALL_BUFF)
        feedback = [obj.set_stroke(width=8) for obj in feedback]
        self.add(*feedback)
        self.add(bottom_label)
        self.add(prev_arrow)
        self.add(prev_label)
        self.wait()

class Auc(Scene):
    def construct(self):
        img = ImageMobject('../jbc2020/integral.png')
        img.scale(3)
        self.play(ShowCreation(img))
        left = SurroundingRectangle(img)
        left.stretch(0.4, 0, about_edge=LEFT)
        self.play(DrawBorderThenFill(left))
        right = SurroundingRectangle(img, color=RED)
        right.stretch(0.6, 0, about_edge=RIGHT)
        self.play(Transform(left, right))

class Test(Scene):
    

class Integral(Scene):
    def construct(self):
        left_arrow = Arrow(
            start=LEFT*3+UP, end=LEFT*2+UP,
        )
        left_arrow.set_stroke(width=8)
        left_label = TextMobject("Random error",
        )
        left_label.next_to(left_arrow, LEFT, MED_SMALL_BUFF)
        self.add(left_arrow)
        self.add(left_label)
        gravity = TextMobject("Gravity")
        box = SurroundingRectangle(gravity, 
            buff=LARGE_BUFF, color=WHITE
        )
        self.play(
            Write(gravity),
            DrawBorderThenFill(box)
        )
        right_arrow = Arrow(
            start=RIGHT*2, end=RIGHT*4,
        )
        right_label = TextMobject("$e(t)$",
        )
        right_label.next_to(right_arrow, RIGHT, MED_SMALL_BUFF)
        self.add(right_arrow)
        self.add(right_label)
        prev_arrow = Arrow(
            start=LEFT*3+DOWN, end=LEFT*2+DOWN
        )
        prev_arrow.set_stroke(width=8)
        prev_label = TextMobject("wheels go brrr")
        prev_label.next_to(prev_arrow, LEFT, MED_SMALL_BUFF)
        bottom = Line(RIGHT*4+RIGHT*MED_LARGE_BUFF+DOWN*2, LEFT*4+DOWN*2)
        feedback = [
            Line(RIGHT*4+RIGHT*MED_LARGE_BUFF+DOWN*MED_LARGE_BUFF, RIGHT*4+RIGHT*MED_LARGE_BUFF+DOWN*2),
            bottom,
            Line(LEFT*4+DOWN*2, LEFT*4+DOWN+DOWN*MED_LARGE_BUFF)
        ]
        bottom_label = TextMobject("Proportional ($K_p e(t)$)")
        bottom_label.next_to(bottom, DOWN, MED_SMALL_BUFF)
        feedback = [obj.set_stroke(width=8) for obj in feedback]
        self.add(*feedback)
        self.add(bottom_label)
        self.add(prev_arrow)
        self.add(prev_label)
        self.wait()