def z_value(confidence_level):
    if confidence_level == 80:
        return 1.282
    elif confidence_level == 85:
        return 1.440
    elif confidence_level == 90:
        return 1.645
    elif confidence_level == 95:
        return 1.960
    elif confidence_level == 99:
        return 2.576
    elif confidence_level == 99.5:
        return 2.807
    elif confidence_level == 99.9:
        return 3.291
    else:
        return None