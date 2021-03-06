from pkg_resources import resource_string
import os
import string


def get_template(name):
    file_name = "{name}.template".format(name=name)
    data = resource_string("pyscaffoldext.custom_extension.templates",file_name)
    return string.Template(data.decode("UTF-8"))


def extension(class_name):

    template = get_template("extension")
    return template.safe_substitute({"extension_class_name":class_name})

def setup(opts):
    template = get_template("setup.py")
    return template.safe_substitute(opts)

def entry_point(opts):

    template = get_template("entry_point")
    return template.safe_substitute(opts)