Invariant/Baseline Builds for Nikola
====================================

This repo contains the build workflow and built demo site that is used to make sure Nikola’s output does not have unexplained differences. The built site is available on the `v3.x` branch.

Usage instructions (for maintainers)
------------------------------------

1. Edit [BUILD-DATA in invariant-builds](https://github.com/getnikola/invariant-builds/blob/master/BUILD-DATA) (you can even do it on GitHub), explain what changed and why in the commit message
2. Wait for the action in this repo to build
3. Restart the failing builds
