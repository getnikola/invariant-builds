Travis Invariant Builder for Nikola
===================================

Because Travis does crazy things, we prepare stuff for invariant building here.

Make sure to change the `BUILD-DATA` file on *every* rebuild!

The built site is available on the `output` branch.

Usage instructions
------------------

1. edit [BUILD-DATA in invariant-builds](https://github.com/getnikola/invariant-builds/blob/master/BUILD-DATA) (you can even do it on github)
2. wait for Travis to finish building
3. restart the build for Python 2.7 in the main Nikola repo, or make a new commit there
