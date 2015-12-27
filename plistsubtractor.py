#!/usr/bin/env python
# Copyright (c) Joshua Wright 2015'ish

import sys
import os
try:
    import biplist
except ImportError:
    sys.stdout.write("You must install the biplist module: pip install biplist\n")
    sys.exit(1)

def extplist(plistfile):
    #print "Processing " + plistfile
    try:
        plistelements=biplist.readPlist(plistfile)
    except biplist.InvalidPlistException:
        print "Invalid plist file: " + plistfile
        return
    except OverflowError:
        print "Invalid plist data: " + plistfile
        return
    except IOError:
        print "Bad file name: " + plistfile
        return

    # Sometimes we get a list or string, not a dictionary
    if not isinstance(plistelements, dict):
        return

    for key in plistelements:
        if isinstance(plistelements[key], biplist.Data):
            # Try to extract plist
            try:
                newp=biplist.readPlistFromString(plistelements[key])
            except biplist.InvalidPlistException:
                # Not valid plist data
                continue

            newfilename=os.path.basename(plistfile[:-6]) + "-" + key + ".plist"
            i=1
            while True:
                if not os.path.exists(newfilename):
                    break
                else:
                    newfilename=os.path.basename(plistfile[:-6]) + "-" + key + "-" + str(i) + ".plist"
                    i+=1
            print "Writing " + newfilename
            try:
                biplist.writePlist(newp,newfilename)
            except:
                print "Could not write plist file " + newfilename
                print sys.exc_info()[0]
            extplist(newfilename)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Usage: %s [plist files]"%sys.argv[0]
        sys.exit(0)
    for pfile in sys.argv[1:]:
        if pfile[-6:] != ".plist":
            print "Skipping file '%s'. File names must end in '.plist'"%pfile
            continue
        extplist(pfile)
