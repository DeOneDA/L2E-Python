def lru_cache(max_size):
    cache = {}
    def decorator(func):
        def wrapper(*args):
            res = func(*args)
            if len(cache) < max_size:
                if args not in cache:
                    wrapper.misses += 1
                    wrapper.hits = 0
                    cache[args] = wrapper.hits
                elif args in cache:
                    wrapper.hits += 1
                    cache[args] = wrapper.hits
            else:
                if args not in cache:
                    wrapper.misses += 1
                    wrapper.hits = 0
                    least = min(cache.values())
                    for key, value in cache.items():
                        if value == least:
                            cache.pop(key)
                            cache[args] = wrapper.hits
                            break
                elif args in cache:
                    wrapper.hits += 1
                    cache[args] = wrapper.hits
            wrapper.cache = cache
            return res
        wrapper.hits = 0
        wrapper.misses = 0
        wrapper.cache = cache
        return wrapper
    return decorator


def fifo(max_size):
    cache = {}
    def decorator(func):
        def wrapper(*args):
            res = func(*args)
            if len(cache) < max_size:
                if args not in cache:
                    wrapper.misses += 1
                    cache[args] = 0
                elif args in cache:
                    cache[args] += 1
                    wrapper.hits += 1
            else:
                if args not in cache:
                    wrapper.missess += 1
                    most = max(cache.values())
                    for key, value in cache.items():
                        if value == most:
                            cache.pop(key)
                            cache[args] = 0
                            break
                elif args in cache:
                    wrapper.hits += 1
                    cache[args] += 1

            wrapper.cache = cache
            return res
        wrapper.hits = 0
        wrapper.misses = 0
        return wrapper
    return decorator



@lru_cache(max_size=2)
def multiply(x):
    return x*x

multiply(1)
multiply(1)
multiply(1)
print(multiply.hits)
multiply(2)
multiply(3)
print(multiply.cache)