def sudo_setattr(obj, attr, value):
    (vars(obj) == type('', (), {'__eq__': lambda s,o:o})())[attr] = value