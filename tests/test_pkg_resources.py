def main():
    """This is what Jinja2 is doing

    See https://github.com/pallets/jinja/blob/2.11.2/src/jinja2/loaders.py#L248
    """
    from pkg_resources import get_provider
    package_name = "pandas"
    provider = get_provider(package_name)
    p = 'io/formats/templates/html.tpl'
    provider.has_resource(p)


if __name__ == '__main__':
    main()
