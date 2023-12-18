from utils import sudo_setattr
from functools import reduce

def list_filter_impl(self, fn):
    return filter(fn, self)
sudo_setattr(list, "filter", list_filter_impl)
sudo_setattr(range, "filter", list_filter_impl)

def list_map_impl(self, fn):
    return map(fn, self)
sudo_setattr(list, "map", list_map_impl)
sudo_setattr(range, "map", list_map_impl)

def list_reduce_impl(self, fn, init):
    return reduce(fn, self, init)
sudo_setattr(list, "reduce", list_reduce_impl)
sudo_setattr(range, "reduce", list_reduce_impl)

del sudo_setattr

