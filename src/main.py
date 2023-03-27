#!/usr/bin/env python
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args


def main(args=None):
    print("hello micro-py")


if __name__ == "__main__":
    sys.exit(main(parse_args()))
