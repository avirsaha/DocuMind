#!/bin/bash

# Read changes from commit messages
CHANGES=$(git log --pretty=format:"- %s" <commit_range>)

# Update CHANGELOG.md
echo -e "## [$(date +'%Y-%m-%d')]\n$CHANGES\n\n$(cat CHANGELOG.md)" > CHANGELOG.md

# Commit and push changes
git add CHANGELOG.md
git commit -m "Update CHANGELOG.md"
git push origin master