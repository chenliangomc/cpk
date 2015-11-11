#!/usr/bin/env python
##
#  Liang Chen (C) Copyright 2013, 2014, 2015
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
#  This Source Code Form is "Incompatible With Secondary Licenses", as
#  defined by the Mozilla Public License, v. 2.0.
##
# cpk-gt$   lsf -cog;lsf -gou;lsf -Ugo
# total 52
# -rw-r--r-- 1   914 2015-11-09 17:04:17.065284951 -0500 command.conf.sample
# -rw-r--r-- 1  2123 2015-11-09 16:31:46.981161183 -0500 conf.py
# -rw-r--r-- 1  1855 2015-11-09 17:00:11.729189844 -0500 conf.pyc
# -rw-r--r-- 1     0 2015-11-10 14:25:37.456628618 -0500 demoapp.py
# -rw-r--r-- 1 16726 2015-11-09 13:03:44.515895727 -0500 MPL-2.0
# -rw-r--r-- 1  2386 2015-11-09 18:36:40.036039419 -0500 pathconf.py
# -rw-r--r-- 1   385 2015-11-09 16:56:09.492651285 -0500 paths.conf.sample
# -rw-r--r-- 1   232 2015-11-09 16:54:50.143163787 -0500 readme.md
# -rw-r--r-- 1  2186 2015-11-09 18:36:57.460340552 -0500 runtool.py
# -rw-r--r-- 1  2638 2015-11-09 17:03:31.168519007 -0500 runtool.pyc
# total 52
# -rw-r--r-- 1   914 2015-11-09 17:04:50.041835400 -0500 command.conf.sample
# -rw-r--r-- 1  2123 2015-11-09 16:44:49.391888078 -0500 conf.py
# -rw-r--r-- 1  1855 2015-11-09 17:01:11.522192671 -0500 conf.pyc
# -rw-r--r-- 1     0 2015-11-10 14:25:37.456628618 -0500 demoapp.py
# -rw-r--r-- 1 16726 2015-11-09 13:04:18.608498894 -0500 MPL-2.0
# -rw-r--r-- 1  2386 2015-11-09 16:44:49.391888078 -0500 pathconf.py
# -rw-r--r-- 1   385 2015-11-09 16:56:41.901259688 -0500 paths.conf.sample
# -rw-r--r-- 1   232 2015-11-09 16:56:41.901259688 -0500 readme.md
# -rw-r--r-- 1  2186 2015-11-09 17:03:31.168519007 -0500 runtool.py
# -rw-r--r-- 1  2638 2015-11-09 17:03:31.168519007 -0500 runtool.pyc
# total 52
# -rw-r--r-- 1  2638 2015-11-09 17:03:31.168519007 -0500 runtool.pyc
# -rw-r--r-- 1  2186 2015-11-09 18:36:57.460340552 -0500 runtool.py
# -rw-r--r-- 1 16726 2015-11-09 13:02:12.682268862 -0500 MPL-2.0
# -rw-r--r-- 1  2123 2015-11-09 16:31:46.929160200 -0500 conf.py
# -rw-r--r-- 1   232 2015-11-09 16:54:50.091162814 -0500 readme.md
# -rw-r--r-- 1   914 2015-11-09 12:15:50.027873283 -0500 command.conf.sample
# -rw-r--r-- 1   385 2015-11-09 16:56:09.444650386 -0500 paths.conf.sample
# -rw-r--r-- 1  1855 2015-11-09 17:00:11.729189844 -0500 conf.pyc
# -rw-r--r-- 1  2386 2015-11-09 18:36:40.036039419 -0500 pathconf.py
# -rw-r--r-- 1     0 2015-11-10 14:25:37.456628618 -0500 demoapp.py
##

import sys, os
import conf,pathconf,runtool

dap = {
    # default app launch name
    "java"   : ( "java", "-jar", ),
    "python" : ( "python", "", ),
}

def work():
    for ln in pathconf.PATHS:
        #print "%s=%s"%( ln, pathconf.PATHS[ ln ] )
        pass
    ##
    pc = pathconf.PathConf()
    print "default path:", pc.getDefaultFilename()
    up = pc.getUserFilename("command.conf")
    print "user path:", up
    uc = pc.readPaths( up )
    #print uc

    # build cmdln string list
    cmdln = list()
    dc = pathconf.PATHS
    app = "jabref"
    apptype = dc[ app ]["type"]
    app_launch_cfg = uc[ apptype ]
    #print app_launch_cfg

    if( apptype == "native" ):
        # skip the interpretor/runtime selecting
        pass
    else:
        if( app_launch_cfg["use"] == "sys" ):
            cmdln.append(  dap[ apptype ][0]  )
            pass
        elif( app_launch_cfg["use"] == "user" ):
            cmdln.append( app_launch_cfg["path"] )
            pass
        else:
            raise ValueError, "'use' key should be either 'sys' or 'user'."
        pass

    # additional option
    cmdln.append( app_launch_cfg["option"] )

    # app image file
    appfile = os.path.join( dc[ app ]["path"], dc[ app ]["fname"] )
    appfileparam = dap[ apptype ][1]
    cmdln.append( appfileparam )
    cmdln.append( appfile )

    # eliminate empty string
    #print cmdln
    cmdln = [ item for item in cmdln if( len(item) > 0 ) ]

    cmd_string = " ".join( cmdln )
    print "'%s'"%( cmd_string )

    try:
        res =  os.system( cmd_string )
        pass
    except:
        print "Error raises when running external program."
        pass
    ##
    return res

def main( args ):
    res = 0
    ##
    res = work()
    ##
    return res
##
if( __name__ == "__main__" ):
    ret = main( sys.argv )
    sys.exit( ret )
    pass
#-eof-#