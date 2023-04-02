
import os


class SVG:

    def __init__(self, name, background_color="black"):
        self.name = name

        self.source = f'<svg viewBox="0 0 1 1" \
xmlns="http://www.w3.org/2000/svg" \
style="background-color:{background_color}>\n</svg>'

    def add_points(self, points, stroke="white", 
                   stroke_width="0.001", fill="none"):

        d = f"M {points[0][0]} {points[0][1]} "
        for i in points[1:]:
            d += f"L {i[0]} {i[1]} "
        d += "Z"

        self.add_path(d, stroke=stroke, 
                      stroke_width=stroke_width, fill=fill)

    def add_path(self, d, stroke="white", 
                 stroke_width="0.001", fill="none"):

        path = f'<path d="{d}" style="stroke:{stroke}; \
stroke-width:{stroke_width}; \
fill:{fill}"/>'

        n = self.source.rfind("<") - 1
        self.source = self.source[:n] + "\n" + path + self.source[n:]

    def save(self):
        dir = "output/" + self.name
        if not os.path.exists(dir):
            os.mkdir(dir)

        self.file = open(f"{dir}/{self.name}.svg", "w")
        self.file.write(self.source)
        self.file.close()

