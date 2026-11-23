#!/usr/bin/env python3
"""
Root Launcher for IncuBrix Visibility Engine
Delegates to incubrix-visibility-engine/run.py
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENGINE_DIR = os.path.join(BASE_DIR, "incubrix-visibility-engine")

if ENGINE_DIR not in sys.path:
    sys.path.insert(0, ENGINE_DIR)

from run import main

if __name__ == "__main__":
    main()
