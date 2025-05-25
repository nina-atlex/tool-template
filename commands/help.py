# LUBRJ(Nina)

import os
import importlib

def commands():
    out = []
    folder = os.path.dirname(__file__)

    for filename in os.listdir(folder):
        temp = []
        if filename.endswith(".py") and filename != os.path.basename(__file__):
            mod_name = filename[:-3]
            module = importlib.import_module(f"commands.{mod_name}")
            temp.append(f"{mod_name} ")

            args = module.command.__code__.co_varnames[:module.command.__code__.co_argcount]
            defaults = module.command.__defaults__ or ()
            non_defaults = len(args) - len(defaults)

            for i, name in enumerate(args):
                has_default = i >= non_defaults
                if has_default:
                    temp.append("{"+f"{name}"+"} ")
                else:
                    temp.append(f"[{name}] ")

            temp.append(f"- {getattr(module, 'discription', 'No description')}")
            out.append("".join(temp))

    return out

def command():
    print(" Commands:")
    for command in commands():
        print(f"     {command}")



