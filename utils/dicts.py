def get_val(collection, key, default='git'):
    """Функция возвращает значение из словаря по переданному ключу,
    если ключ существует. В ином случае возвращается значение
    default"""
    if key in collection.keys():
        for k, i in collection.items():
            if k == key:
                return i
    else:
        return default

