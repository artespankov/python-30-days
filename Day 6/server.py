# RUN gunicorn server:app --reload\

def render_template(template_name='index.html', context=None):
    if context is None:
        context = {}
    with open(template_name, 'r') as f:
        html_str = f.read()
        html_str = html_str.format(**context)
    return html_str


def home(environ):
    return render_template(
        template_name="index.html",
        context={}
    )


def contact_us(environ):
    return render_template(
        template_name="contact.html",
        context={}
    )


def app(environ, start_response):
    """
    :param environ: metadata on request - uri, host, port, headers, cookies etc
    :param start_response:
    :return:
    """
    path = environ.get("PATH_INFO")
    if path == "/":
        data = home(environ)
    elif path == '/contact':
        data = contact_us(environ)
    else:
        data = render_template(template_name="404.html", context={"path": path})
    data = data.encode("utf-8")  # bytestring
    start_response(
        f"200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ]
    )
    return iter([data])
