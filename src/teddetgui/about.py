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
        self.draw_logoTD(cvlogoTD, 5, "#77F", "#55A")

        cvlogoPF = tki.Canvas(self, height = 200, width = 200)
        cvlogoPF.grid(row = 1, column = 1)
        self.draw_logoPF(cvlogoPF, 5, "", "", "#550")

        cvlogoHX = tki.Canvas(self, height = 200, width = 200)
        cvlogoHX.grid(row = 2, column = 1)
        colors = ["#FFF"]
        colors += [""] * 13
        colors[7] = colors[1] = "#F68712"
        colors[2] = "#F47216"
        colors[13] = colors[3] = "#FBC707"
        colors[6] = colors[4] = "#F1471D"
        colors[9] = colors[5] = "#F25C19"
        colors[8] = "#F89C0E"
        colors[12] = colors[10] = "#FFF200"
        colors[11] = "#FAB20B"
        self.draw_logoHX(cvlogoHX, 5, colors)

        cvlogoPY = tki.Canvas(self, height = 200, width = 200)
        cvlogoPY.grid(row = 2, column = 2)
        self.draw_logoPY(cvlogoPY, 5, "#005", "", "")

    def rectTS(self, canvas, scale, t, a, b, fill, outline):
        canvas.create_rectangle(
            (scale * a[0]) + t[0], (scale * a[1]) + t[1],
            (scale * b[0]) + t[0], (scale * b[1]) + t[1],
            fill = fill, outline = outline)

    def arcTS(self, canvas, scale, t, a, b, fill, outline, start,
              extent, style):
        canvas.create_arc(
            (scale * a[0]) + t[0], (scale * a[1]) + t[1],
            (scale * b[0]) + t[0], (scale * b[1]) + t[1],
            fill = fill, outline = outline, start = start,
            extent = extent, style = style)

    def draw_T(self, canvas, scale, t, fg, bg):
        t = (scale * t[0], scale * t[1])
        self.rectTS(canvas, scale, t, (0, 0), (12, 4), fg, fg)
        self.rectTS(canvas, scale, t, (4, 4), (8, 12), fg, fg)

    def draw_D(self, canvas, scale, t, fg, bg):
        t = (scale * t[0], scale * t[1])
        self.rectTS(canvas, scale, t, (0, 0), (4, 12), fg, fg)
        self.arcTS(canvas, scale, t, (4, 0), (12, 12), fg, fg,
                   -90, 180, tki.CHORD)
        self.rectTS(canvas, scale, t, (4, 0), (8, 12), fg, fg)
        self.arcTS(canvas, scale, t, (4, 4), (8, 8), bg, bg,
                   -90, 180, tki.CHORD)
        self.rectTS(canvas, scale, t, (4, 4), (6, 8), bg, bg)

    def draw_E(self, canvas, scale, t, fg, bg):
        t = (scale * t[0], scale * t[1])
        self.rectTS(canvas, scale, t, (0, 0), (6, 7), fg, fg)
        self.rectTS(canvas, scale, t, (1, 1), (5, 6), bg, bg)
        self.rectTS(canvas, scale, t, (2, 2), (5, 3), fg, fg)
        self.rectTS(canvas, scale, t, (2, 4), (5, 5), fg, fg)

    def draw_logoTD(self, canvas, scale, fg, bg):
        self.rectTS(canvas, scale, (0, 0), (0, 0), (27, 27), bg, bg)
        self.draw_T(canvas, scale, (1, 1), fg, bg)
        self.draw_D(canvas, scale, (14, 1), fg, bg)
        self.draw_E(canvas, scale, (11, 6), fg, bg)
        self.draw_D(canvas, scale, (1, 14), fg, bg)
        self.draw_T(canvas, scale, (14, 14), fg, bg)
        self.draw_E(canvas, scale, (11, 19), fg, bg)

    def draw_logoPF(self, canvas, scale, cwhi, cbla, cora):
        canvas.create_rectangle(0, 0, 200, 200, fill = cora)


    def draw_triHX(self, canvas, scale, a, b, c, color):
        pass

    def draw_wingHX(self, canvas, scale, a, b, colors):
        ha = 15
        hb = 5
        c = (0, 0)
        self.draw_triHX(canvas, scale, a, b, c, colors[0])

    def draw_logoHX(self, canvas, scale, colors):
        canvas.create_rectangle(0, 0, 200, 200, fill = colors[0])
        a = (100, 50)
        b = (150, 100)
        c = (100, 150)
        d = (50, 100)
        canvas.create_polygon(*list(a + b + c + d),
                              fill = colors[1], width = 0)
        self.draw_wingHX(canvas, scale, a, b, colors[2:5])
        self.draw_wingHX(canvas, scale, b, c, colors[5:8])
        self.draw_wingHX(canvas, scale, c, d, colors[8:11])
        self.draw_wingHX(canvas, scale, d, a, colors[11:14])

    def draw_logoPY(self, canvas, scale, cblue, cyell, cwhi):
        canvas.create_rectangle(0, 0, 200, 200, fill = cblue)
        pass

