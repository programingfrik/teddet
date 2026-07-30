# -*- coding: utf-8 -*-

import tkinter as tki
from tkinter import Toplevel

class about_teddet(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.create_content()
        self.resizable(height = False, width = False)

    def create_content(self):
        cvlogoTD = tki.Canvas(self, height = 200, width = 200)
        cvlogoTD.grid(row = 0, column = 1)
        self.dibujar_logoTD(cvlogoTD, 10, "#55F", "#55A")

    def dibujar_T(self, canvas, scale, x, y, fg, bg):
        canvas.create_rectangle(x, y, (scale * 12) + x, (scale * 4) + y,
                                fill = fg, outline = fg)
        canvas.create_rectangle((scale * 4) + x, (scale * 4) + y,
                                (scale * 8) + x, (scale * 12) + y,
                                fill = fg, outline = fg)

    def dibujar_D(self, canvas, scale, x, y, fg, bg):
        canvas.create_rectangle(x, y, (scale * 4) + x, (scale * 12) + y,
                                fill = fg, outline = fg)
        canvas.create_arc((scale * 4) + x, y,
                          (scale * 12) + x, (scale * 12) + y,
                          fill = fg, outline = fg, start = -90,
                          extent = 180, style = tki.CHORD)
        canvas.create_rectangle((scale * 4) + x, y,
                                (scale * 8) + x, (scale * 12) + y,
                                fill = fg, outline = fg)
        canvas.create_arc((scale * 4) + x, (scale * 4) + y,
                          (scale * 8) + x, (scale * 8) + y,
                          fill = bg, outline = bg, start = -90,
                          extent = 180, style = tki.CHORD)
        canvas.create_rectangle((scale * 4) + x, (scale * 4) + y,
                                (scale * 6) + x, (scale * 8) + y,
                                fill = bg, outline = bg)

    def dibujar_logoTD(self, canvas, scale, fg, bg):
        canvas.create_rectangle(0, 0, (scale * 27), (scale * 27),
                                fill = bg, width = 0)
        self.dibujar_T(canvas, scale, scale, scale, fg, bg)
        self.dibujar_D(canvas, scale, scale * 14, scale, fg, bg)
        self.dibujar_D(canvas, scale, scale, scale * 14, fg, bg)
        self.dibujar_T(canvas, scale, scale * 14, scale * 14, fg, bg)

