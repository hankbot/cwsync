cwsync is a tool that was built to help keep a remote server in sync with a local dev environment.

While the tool is running the specified local source path is monitored for Mac OS X fsevents. When a change is detected rsync is used to synchronize the source to the supplied destination.

The tool can also be used to refresh the local copy in the case that the server has changes that need to be brought to the local copy.

In all cases the destination is made to match the source.

The bin script relies on the included autosync Python package.

rsync parameters such as exclusion patterns may be modified in the RSYNC_OPTIONS value set in config.py file in the autosync package.
