def drink_validator(request_data: dict):
    if (
        'title' not in request_data
        and 'recipe' not in request_data
    ):
        return False

    if (
        not isinstance(request_data['title'], str)
        and not isinstance(request_data['recipe'], list)
    ):
        return False

    # the required datatype is [{'color': string, 'name':string, 'parts':number}]
    for r in request_data['recipe']:
        if (
            'color' not in r
            and 'name' not in r
            and 'parts' not in r
        ):
            return False

        if (
            not isinstance(r['color'], str)
            and not isinstance(r['name'], str)
            and not isinstance(r['parts'], int)
        ):
            return False

    return True
