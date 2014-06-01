cwsync is a tool that was built to help keep a remote server in sync with a local dev environment.

While the tool is running, the supplied source destination is monitored for Mac OS X fsevents. When a change is detected rsync is used to synchronize the source to the destination.

The bin script relies on the included autosync Python package.
