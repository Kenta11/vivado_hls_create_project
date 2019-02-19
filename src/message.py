#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def print_INFO(message):
    print("INFO: ", message)

def print_WARNING(message):
    print("INFO:", message)

def print_ERROR(message):
    print("ERROR:", message, file=sys.stderr)

if __name__ == '__main__':
    print_INFO("This is INFO")
    print_WARNING("This is WARNING")
    print_ERROR("This is ERROR")
