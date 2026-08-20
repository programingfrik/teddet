# -*- coding: utf-8 -*-

import tkinter as tki
from tkinter import Toplevel
import math

X = 0
Y = 1

def rotate_point(p, a):
    global X, Y
    prx = p[X] * math.cos(a) - p[Y] * math.sin(a)
    pry = p[X] * math.sin(a) + p[Y] * math.cos(a)
    return prx, pry

def normalize(v):
    global X, Y
    modulus = math.sqrt(v[X] ** 2 + v[Y] ** 2)
    vn = v[X] / modulus, v[Y] / modulus
    return vn

def calc_perpendicular(a, b, h):
    global X, Y

    # Calculate the middle point between a and b
    mid = (b[X] + a[X]) / 2, (b[Y] + a[Y]) / 2

    # Calculate the "real vector"
    rv = b[X] - a[X], b[Y] - a[Y]

    # Normalize the vector
    nrv = normalize(rv)

    # Rotate 270 degrees, or 3 * pi / 2, the normalized real vector
    rnrv = rotate_point(nrv, 3 * math.pi / 2)

    # The only thing left is multiply by h so that it has the
    # solicitated height and translate it to the middlepoint.
    pv = (rnrv[X] * h) + mid[X], (rnrv[Y] * h) + mid[Y]

    return pv

class about_teddet(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.create_content()
        self.resizable(height = False, width = False)

    def create_content(self):
        cvlogoTD = tki.Canvas(self, height = 200, width = 200)
        cvlogoTD.grid(row = 0, column = 1)
        self.draw_logoTD(cvlogoTD, 200, "#77F", "#55A")

        cvlogoPF = tki.Canvas(self, height = 200, width = 200)
        cvlogoPF.grid(row = 1, column = 1)
        self.draw_logoPF(cvlogoPF, 200, "", "", "#550")

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
        self.draw_logoHX(cvlogoHX, 200, colors)

        cvlogoPY = tki.Canvas(self, height = 200, width = 200)
        cvlogoPY.grid(row = 2, column = 2)
        self.draw_logoPY(cvlogoPY, 200, "#306998", "#FFD43B", "#FFF")

    def rectTS(self, canvas, scale, t, a, b, fill, outline, width):
        global X, Y
        canvas.create_rectangle(
            (scale * a[X]) + t[X], (scale * a[Y]) + t[Y],
            (scale * b[X]) + t[X], (scale * b[Y]) + t[Y],
            fill = fill, outline = outline, width = width)

    def arcTS(self, canvas, scale, t, a, b, fill, outline, start,
              extent, style, width):
        global X, Y
        canvas.create_arc(
            (scale * a[X]) + t[X], (scale * a[Y]) + t[Y],
            (scale * b[X]) + t[X], (scale * b[Y]) + t[Y],
            fill = fill, outline = outline, start = start,
            extent = extent, style = style, width = width)

    def ovalTS(self, canvas, scale, t, a, b, fill, outline, width):
        global X, Y
        canvas.create_oval((scale * a[X]) + t[X], (scale * a[Y]) + t[Y],
                           (scale * b[X]) + t[X], (scale * b[Y]) + t[Y],
                           fill = fill, outline = outline, width = width)

    def draw_T(self, canvas, scale, t, fg, bg):
        global X, Y
        t = (scale * t[X], scale * t[Y])
        self.rectTS(canvas, scale, t, (0, 0), (12, 4), fg, fg, 1)
        self.rectTS(canvas, scale, t, (4, 4), (8, 12), fg, fg, 1)

    def draw_D(self, canvas, scale, t, fg, bg):
        global X, Y
        t = (scale * t[X], scale * t[Y])
        self.rectTS(canvas, scale, t, (0, 0), (4, 12), fg, fg, 1)
        self.arcTS(canvas, scale, t, (4, 0), (12, 12), fg, fg,
                   -90, 180, tki.CHORD, 1)
        self.rectTS(canvas, scale, t, (4, 0), (8, 12), fg, fg, 1)
        self.arcTS(canvas, scale, t, (4, 4), (8, 8), bg, bg,
                   -90, 180, tki.CHORD, 1)
        self.rectTS(canvas, scale, t, (4, 4), (6, 8), bg, bg, 1)

    def draw_E(self, canvas, scale, t, fg, bg):
        global X, Y
        t = (scale * t[X], scale * t[Y])
        self.rectTS(canvas, scale, t, (0, 0), (6, 7), fg, fg, 1)
        self.rectTS(canvas, scale, t, (1, 1), (5, 6), bg, bg, 1)
        self.rectTS(canvas, scale, t, (2, 2), (5, 3), fg, fg, 1)
        self.rectTS(canvas, scale, t, (2, 4), (5, 5), fg, fg, 1)

    def draw_logoTD(self, canvas, scale, fg, bg):
        step = scale // 28
        self.rectTS(canvas, step, (1, 1), (1, 1), (28, 28), bg, bg, 1)
        self.draw_T(canvas, step, (2, 2), fg, bg)
        self.draw_D(canvas, step, (15, 2), fg, bg)
        self.draw_E(canvas, step, (12, 7), fg, bg)
        self.draw_D(canvas, step, (2, 15), fg, bg)
        self.draw_T(canvas, step, (15, 15), fg, bg)
        self.draw_E(canvas, step, (12, 20), fg, bg)

    def draw_logoPF(self, canvas, scale, cwhi, cbla, cora):
        canvas.create_rectangle(0, 0, 200, 200, fill = cora)

    def draw_triHX(self, canvas, scale, a, b, c, color):
        canvas.create_polygon(*list(a + b + c),
                              fill = color, width = 0)

    def draw_wingHX(self, canvas, scale, a, b, colors):
        ha = int(scale * 0.40)
        hb = int(scale * 0.063)
        c = calc_perpendicular(a, b, ha)
        self.draw_triHX(canvas, scale, a, b, c, colors[0])
        d = calc_perpendicular(a, c, hb)
        self.draw_triHX(canvas, scale, a, c, d, colors[1])
        e = calc_perpendicular(c, b, hb)
        self.draw_triHX(canvas, scale, c, b, e, colors[2])

    def draw_logoHX(self, canvas, scale, colors):
        # canvas.create_rectangle(0, 0, scale, scale, fill = colors[0])
        size = (scale // 3)
        center = (scale // 2)
        a = (center, center - size)
        b = (center + size, center)
        c = (center, center + size)
        d = (center - size, center)
        canvas.create_polygon(*list(a + b + c + d),
                              fill = colors[1], width = 0)
        self.draw_wingHX(canvas, scale, a, b, colors[2:5])
        self.draw_wingHX(canvas, scale, b, c, colors[5:8])
        self.draw_wingHX(canvas, scale, c, d, colors[8:11])
        self.draw_wingHX(canvas, scale, d, a, colors[11:14])

    def draw_python(self, canvas, scale, sense, col1, col2, cwhi):
        center = scale // 2
        step = (scale // 84) * sense

        md = 20 # medium distance
        ld = 35 # large distance
        ce = 0 # center
        ma = 2 # margin
        ov = 8 # oval distante
        ed = 3 # eye distance

        os = ld + ov # oval superior
        oi = ld - ov # oval inferior
        mm = md + ma # medium plus margin
        mb = ma // 2 # margin bottom
        ex = (md // 2) # eye X
        ey = int(md * 1.5) # eye Y
        eb = ex + ed # eye before
        ea = ex - ed # eye after
        es = ey + ed # eye superior
        ei = ey - ed # eye inferior
        cd = md // 2 # curve distance
        cx = -md + cd # curve x
        cy = cd + mb # curve y
        cb = cx + cd # curve before
        ca = -md
        cs = cy + cd # curve superior
        ci = cy - cd # curve infecior
        ub = cb + ma # outward before
        ua = ca - ma # outward after
        us = cs + ma # outward superior
        ui = ci - ma # outward inferior

        cp = (center, center) # central point

        self.rectTS(canvas, step, cp, (ub, us), (ua, ui), col2, cwhi, 0)
        self.ovalTS(canvas, step, cp, (ub, us), (ua, ui), cwhi, cwhi, 0)
        self.ovalTS(canvas, step, cp, (cb, cs), (ca, ci), col1, cwhi, 0)

        self.rectTS(canvas, step, cp, (-md, ld), (-mm, cy), cwhi, cwhi, 0)
        self.rectTS(canvas, step, cp, (-cx, mb), (cx, -mb), cwhi, cwhi, 0)
        self.rectTS(canvas, step, cp, (md, mm), (ce, md), cwhi, cwhi, 0)

        self.rectTS(canvas, step, cp, (md, ld), (-md, mm), col1, cwhi, 0)
        self.ovalTS(canvas, step, cp, (md, os), (-md, oi), col1, cwhi, 0)

        self.rectTS(canvas, step, cp, (ld, md), (mm, -md), col1, cwhi, 0)
        self.ovalTS(canvas, step, cp, (os, md), (oi, -md), col1, cwhi, 0)

        self.rectTS(canvas, step, cp, (mm, md), (cx, mb), col1, cwhi, 0)
        self.rectTS(canvas, step, cp, (ce, mm), (-md, cy), col1, cwhi, 0)
        self.ovalTS(canvas, step, cp, (eb, es), (ea, ei), cwhi, cwhi, 0)

    def draw_logoPY(self, canvas, scale, cblue, cyell, cwhi):
        canvas.create_rectangle(0, 0, scale, scale, fill = cwhi)
        self.draw_python(canvas, scale, -1, cblue, cyell, cwhi)
        self.draw_python(canvas, scale, 1, cyell, cblue, cwhi)
