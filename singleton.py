def singleton(cls):

    instance = {}
    
    def wrap(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    
    return wrap

