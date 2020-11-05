def mode_data(data):
    try:
        return max(data, key = data.count)
    except ValueError:
        print("Empty list")
