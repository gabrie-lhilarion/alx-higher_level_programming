#!/usr/bin/python3
"""Defines an object attributes abd methods lookup function."""

def lookup(obj):
    return [attr for attr in dir(obj)]


