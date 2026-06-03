#!/usr/bin/env bash
set -e

echo "Installing MiniJoyse..."

PROJECT_DIR="$(dirname "$(dirname "$(realpath "$0")")")"
INSTALL_DIR="$HOME/.local/share/MiniJoyse"

mkdir -p "$INSTALL_DIR"

rm -rf "$INSTALL_DIR"/*

cp -r "$PROJECT_DIR"/* "$INSTALL_DIR"

echo "MiniJoyse installed!"
