"""

svggearslib/gears.py

written by: Oliver Cordes 2020-07-10
changed by: Oliver Cordes 2020-07-10

"""

import svgwrite

def solid_gear():
    dwg = svgwrite.Drawing(None, profile='tiny')
    dwg.add(dwg.line((0, 0), (100, 100), stroke=svgwrite.rgb(100, 10, 16, '%')))
    dwg.add(dwg.text('Test', insert=(100, 100)))

    return dwg
