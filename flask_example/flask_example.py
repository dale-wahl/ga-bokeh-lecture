from __future__ import print_function

import flask

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

app = flask.Flask(__name__)


@app.route("/")
def flask_example():
    p = figure()
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    p.line(x, y, line_width=3)
    script, div = components(p)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    html = flask.render_template(
        'embed.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)

if __name__ == "__main__":
    print(__doc__)
    app.run(port=5050)
