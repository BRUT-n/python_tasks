def transform(legacy_data):
    new_format = {}
    for key, full_value in legacy_data.items():
        for ch in full_value:
            new_format.setdefault(ch.lower(), key)
    return new_format

