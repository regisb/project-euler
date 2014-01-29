import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pyramid shortest path")
    parser.add_argument("path", metavar="PATH", help="Path to pyramid text file")
    args = parser.parse_args()

    pyramid_string = open(args.path).read()
    pyramid = [map(int, line.split()) for line in pyramid_string.splitlines()]
    level_count = len(pyramid)
    longest_path = [[0]*len(level) for level in pyramid]

    # Longest path of last level
    longest_path[-1] = pyramid[-1][:]

    # Longest path of above levels
    for level_index in range(level_count-2, -1, -1):
        level_length = level_index + 1
        for i in range(0, level_length):
            longest_path[level_index][i] = pyramid[level_index][i] + max(longest_path[level_index+1][i], longest_path[level_index+1][i+1])


    print longest_path[0][0]
