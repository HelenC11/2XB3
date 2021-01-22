#defining are_valid_groups
def are_valid_groups(nums, groups):
    for group in groups:
        if len(group) > 3 or len(group) < 2:
            return False
    seen = set()
    for x in nums:
        if x in seen: return False
        seen.add(x)

    for x in nums:
        result = any(x in sl for sl in groups)
        if result == False:
            return False

    return result

