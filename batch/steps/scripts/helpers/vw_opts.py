import json
import itertools
import functools

def serialize(opts):
    if not isinstance(opts, dict):
        raise Error('opts are not dict')
    return json.dumps(opts)

def deserialize(s):
    candidate = json.loads(s)
    if not isinstance(candidate, dict):
        raise Error('candidate opts are not dict')
    return candidate

def union(first, second):
    return dict(first, **second)

def cartesian(*dimensions):
    return functools.reduce(lambda d1, d2: 
                  list(map(lambda tuple: union(tuple[0], tuple[1]), itertools.product(d1, d2))),
                  dimensions)

def dimension(name, values):
    return list(map(lambda v : dict([(name, str(v))]), values))

if __name__ == '__main__':
    multiprocessing.freeze_support()