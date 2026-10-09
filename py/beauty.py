import math, colorsys
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection

def bez(p0, p1, p2, n=30):
    return [
        (
        (1 - t)**2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0],
        (1 - t)**2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p2[1]
         ) 
         for t in [i / n for i in range(n + 1)]
        ]

def petal(a, L, W, S):
    d, p = (math.cos(a),math.sin(a)),(-math.sin(a),math.cos(a))
    tip = (d[0] * L * S, d[1] * L * S)
    cl = (d[0] * L * 0.55 * S + p[0] * W * S, d[1] * L * 0.55 * S + p[1] * W * S)
    cr = (d[0] * L * 0.55 * S - p[0] * W * S, d[1] * L * 0.55 * S - p[1] * W * S)
    # تم تصحيح (8,0) إلى (0,0)
    return bez((0,0), cl, tip) + bez(tip, cr, (0,0)) 

N, L, W, R = 18, 290, 70, 22
segs, cols = [], []

for k in range(N):
    a = 2 * math.pi * k / N 
    e = colorsys.hsv_to_rgb(k / N, 0.9, 0.95)
    for r in range(R):
        s = (r + 1) / R
        c = tuple((1 - s) + e[i] * s for i in range(3))
        pts = petal(a, L, W, s)
        # تم تصحيح المحاذاة والإزاحة هنا
        segs += list(zip(pts, pts[1:]))
        cols += [c] * (len(pts) - 1)

total = len(segs)
FPS = 30
DRAW_F, HOLD_F = FPS * 16, FPS * 2
FRAMES = DRAW_F + HOLD_F
per = max(1, total // DRAW_F)

fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_xlim(-330, 330)
ax.set_ylim(-330, 330)
ax.set_aspect("equal")
ax.axis("off")
plt.tight_layout(pad=0)

lc = LineCollection([], linewidths=1.6)
ax.add_collection(lc)

def update(f):
    e = min(total, (f + 1) *per)
    lc.set_segments(segs[:e])
    lc.set_color(cols[:e])
    return lc,

ani = animation.FuncAnimation(fig, update, frames=FRAMES, blit=True, interval=1000/FPS)


plt.show()