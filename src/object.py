from utils import sudo_setattr

def object_to_list_impl(self):
    return list(self)
sudo_setattr(object, "to_list", object_to_list_impl)

def object_to_tuple_impl(self):
    return tuple(self)
sudo_setattr(object, "to_tuple", object_to_tuple_impl)

def object_to_set_impl(self):
    return set(self)
sudo_setattr(object, "to_set", object_to_set_impl)

def object_to_str_impl(self):
    return str(self)
sudo_setattr(object, "to_str", object_to_str_impl)

