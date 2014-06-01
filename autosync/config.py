import logging

LOG_LEVEL = logging.WARNING

FSEVENT_LATENCY = 1
FSEVENT_SINCE   = -1

RSYNC_OPTIONS = ['-v', '--delete', '-rltu', '--exclude=.svn/', '--exclude=data/']