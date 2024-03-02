import sys
import os


BUFFER_SIZE = 8192

def tail(file, count=10):
    # Open the file in binary mode, so that we can read it in chunks backwards
    f = open(file, 'rb')

    # Move the cursor to the end of the file
    f.seek(0, os.SEEK_END)

    # Read the file in reverse until we have read the number of lines requested
    newlines = 0
    while f.tell() > 0 and newlines <= count:
        # Go back by BUFFER_SIZE
        f.seek(-BUFFER_SIZE, os.SEEK_CUR)

        # Read forward by BUFFER_SIZE
        lines = f.read(BUFFER_SIZE).split(b"\n")

        # Count the number of newlines
        newlines += lines.count(b'')

        # Go back again.
        f.seek(-BUFFER_SIZE, os.SEEK_CUR)

    # Read the last lines
    for line in f.readlines()[-count:]:
        print(line.decode('utf-8'), end='')

    # Close the file
    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:\n\tpython tail.py <file>")
        sys.exit(1)

    tail(sys.argv[1])
