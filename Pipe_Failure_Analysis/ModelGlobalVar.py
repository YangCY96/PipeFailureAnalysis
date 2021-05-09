
class Global_Var:
    global _global_dict
    _global_dict = {}
    pass

def set_value(name, value):
    _global_dict[name] = value
    pass

def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue