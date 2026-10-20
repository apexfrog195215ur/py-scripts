
def chunk(items, size):
    # split into fixed-size lists
    buf = []
    for it in items:
        buf.append(it)
        if len(buf) >= size:
            yield buf
            buf = []
    if buf:
        yield buf


if __name__ == "__main__":
    for c in chunk(range(10), 3):
        print(c)
