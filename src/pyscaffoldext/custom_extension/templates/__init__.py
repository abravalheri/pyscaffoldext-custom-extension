from pkg_resources import resource_string
import os
import string


def get_template(name):
    file_name = "{name}.template".format(name=name)
    data = resource_string("pyscaffoldext.custom_extension.templates",file_name)
    return string.Template(data.decode("UTF-8"))


def extension():

    template = get_template("extension")
    return template.safe_substitute({"extension_class_name":"TestClass"})

def setup(opts):
    template = get_template("setup.py")
    return template.safe_substitute(opts)