#!/bin/sh

PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
OS=mac

gyp --depth=. -DOS=$OS

echo "project dir : "$PROJECT_DIR
