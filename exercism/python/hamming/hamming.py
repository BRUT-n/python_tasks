def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    counter = 0
    for a, b in zip(strand_a, strand_b):
        if a != b:
            counter += 1
    return counter

