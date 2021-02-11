import jinja2


def main():
    loader = jinja2.PackageLoader("pandas", "io/formats/templates")
    env = jinja2.Environment(loader=loader, trim_blocks=True)
    template = env.get_template("html.tpl")


if __name__ == '__main__':
    main()
