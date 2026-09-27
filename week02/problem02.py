# Name: Kuldeep Kumar
# Roll number: 2K24/CSME/30
# GitHub username: 2K24CSME30

# TODO 1: Multiply width, height, and bpp, then divide by 8.
def display_memory_bytes(width: int, height: int, bpp: int) -> int:
    """Return image memory in bytes."""
    return width * height * bpp // 8

# TODO 2: Remove #
expected_bytes = 1920 * 1080 * 24 // 8
assert display_memory_bytes(1920, 1080, 24) == expected_bytes
print(display_memory_bytes(1920, 1080, 24))
