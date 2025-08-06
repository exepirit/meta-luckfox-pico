def parse_partition(partition):
    def parse_size(size):
        units = {"K": 2**10, "M": 2**20, "G": 2**30, "T": 2**40}
        number, unit = size[:-1], size[-1]
        return int(float(number)*units[unit])

    size_offset, name = tuple(partition.rstrip(")").split("("))
    size_offset = size_offset.split("@")
    size = parse_size(size_offset[0])
    if len(size_offset) > 1:
        offset = parse_size(size_offset[1])
    else:
        offset = -1
    return (name, size, offset)


def iterate_partitions(env_str):
    offset = 0
    for part in env_str.split(","):
        name, size, defined_offset = parse_partition(part)
        if defined_offset >= 0:
            yield (name, size, defined_offset)
            offset = defined_offset + size
        else:
            yield (name, size, offset)
            offset += size


def get_partition(env_str, partition_name):
    for i, partition in enumerate(iterate_partitions(env_str)):
        name, size, offset = partition
        if name == partition_name:
            return (i+1, size, offset)
    raise Exception(f"Partition {partition_name} not found in environment string")


def get_partition_index(env_str, partition_name):
    index, _, _ = get_partition(env_str, partition_name)
    return index


def get_partition_size(env_str, partition_name):
    _, size, _ = get_partition(env_str, partition_name)
    return hex(size)


def get_partition_offset(env_str, partition_name):
    _, _, offset = get_partition(env_str, partition_name)
    return hex(offset)
