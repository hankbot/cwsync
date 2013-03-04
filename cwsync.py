#!/usr/bin/env python
import sys

print "Initializing: please wait"
sync = None

try:
    import optparse
    import autosync.util
    import time
    import termios
    import fcntl
    import os
    import autosync.constant as AC

    def main():
        try:
            
            options = parse_options()
        
            fd = sys.stdin.fileno()
            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)
            oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
            
            sync = autosync.util.fsevent_sync()
            sync.set_sync_source(options[1][0])
            sync.set_sync_destination(options[1][1])
        
            #is_started = sync.start_sync()
            #
            #if not is_started:
            #    print "Error starting sync"
            #    exit(1)
            print "Ready: you may (s)tart, (p)ause, or (q)uit"
            while 1:
                try:
                    c = sys.stdin.read(1)
                    s = str(c)
                    
                    if s == 'p':
                        is_paused = sync.pause_sync()
                        
                        if is_paused:
                            print "Paused"
                        else:
                            print "Could not pause"
                        print sync.sync_status
                    elif s == 's':
                        if sync.sync_status == AC.STATUS_IDLE:
                            is_started = sync.start_sync()
                            
                            if not is_started:
                                print "Error starting sync"
                                exit(1)
                            
                            print "Started"
                        else:
                            print "Cannot start, already running"
                    elif s == 't':
                        print sync.sync_status
                    elif s == 'q':
                        sync.pause_sync(True)
                        print 'Quit: goodbye'
                        exit()
                    elif s == 'r':
                        print "Reverse sync"
                        is_reverse = sync.reverse_sync()
                        if not is_reverse:
                            print "Reverse sync cannot start"
                    else:
                        pass
                    
                except IOError:
                    pass
                
                time.sleep(.2)
                
        except KeyboardInterrupt:
            if sync:
                sync.pause_sync()
            print 'Cancelled: goodbye'
            exit()
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        
    def parse_options():
        parser = optparse.OptionParser()
        o, a   = parser.parse_args()
        
        return [o, a]
    
    if __name__ == '__main__':
        main()
        
except KeyboardInterrupt:
    if not sync == None:
        sync.pause_sync()
    exit()
