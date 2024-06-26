import yaml
from collections import OrderedDict


def ordered_yaml():
    """Support OrderedDict for yaml.
    Returns:
        yaml Loader and Dumper.
    """
    try:
        from yaml import CDumper as Dumper
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import Dumper, Loader

    _mapping_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG

    def dict_representer(dumper, data):
        return dumper.represent_dict(data.items())

    def dict_constructor(loader, node):
        return OrderedDict(loader.construct_pairs(node))

    Dumper.add_representer(OrderedDict, dict_representer)
    Loader.add_constructor(_mapping_tag, dict_constructor)
    return Loader, Dumper


def parse(opt_path):
    """Parse option file.
    Args:
        opt_path (str): Option file path.
        is_train (str): Indicate whether in training or not. Default: True.
    Returns:
        (dict): Options.
    """
    with open(opt_path, mode="r") as f:
        Loader, _ = ordered_yaml()
        opt = yaml.load(f, Loader=Loader)
    return opt


def dict2str(opt, indent_level=1):
    """dict to string for printing options.
    Args:
        opt (dict): Option dict.
        indent_level (int): Indent level. Default: 1.
    Return:
        (str): Option string for printing.
    """
    msg = "\n"
    for k, v in opt.items():
        if isinstance(v, dict):
            msg += " " * (indent_level * 2) + k + ":["
            msg += dict2str(v, indent_level + 1)
            msg += " " * (indent_level * 2) + "]\n"
        else:
            msg += " " * (indent_level * 2) + k + ": " + str(v) + "\n"
    return msg


def get_msg():
    msg = r"""
  _      _______      ________ _   _      _   
 | |    |_   _\ \    / /  ____| \ | |    | |  
 | |      | |  \ \  / /| |__  |  \| | ___| |_ 
 | |      | |   \ \/ / |  __| | . ` |/ _ \ __|
 | |____ _| |_   \  /  | |____| |\  |  __/ |_ 
 |______|_____|   \/   |______|_| \_|\___|\__|                      
    """
    return msg
