#!/bin/bash

PROJECT_NAME=$1

if [ -z "$PROJECT_NAME" ]; then
    echo "Usage: ./create_project.sh <project_name>"
    exit 1
fi

ROOT_DIR=~/Desktop/DATAFORGE_ANALYTICS
TEMPLATE_DIR=$ROOT_DIR/SHARED_ASSETS/project_template
TARGET_DIR=$ROOT_DIR/PROJECTS/$PROJECT_NAME

cp -r "$TEMPLATE_DIR" "$TARGET_DIR"

echo "Project created at:"
echo "$TARGET_DIR"