cwsync is a tool that was built to help keep a remote server in sync with a local dev environment.

The main goal of this project is to make working with large codebases on a remote dev server easier when using an editor or IDE that works better with a local file access e.g. Sublime Text, TextMate, Eclipse.

While the tool is running the specified local source path is monitored for Mac OS X fsevents. When a change is detected rsync is used to synchronize the source to the supplied destination.

The tool can also be used to refresh the local copy in the case that the server has changes that need to be brought to the local copy. This action is refered to as a "reverse sync".

In all sync cases the destination is made to match the source, changes in the destination will be overwritten.

The bin script relies on the included autosync Python package.

rsync parameters such as exclusion patterns may be modified in the RSYNC_OPTIONS value set in config.py file in the autosync package.

Only one action may be performed at a time. If the program is monitoring the local source path it must be paused prior to initiating a reverse sync.
