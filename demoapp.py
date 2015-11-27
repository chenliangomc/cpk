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
"""
@author: Liang Chen
@license: Mozilla Public License Version 2.0
@since: 2015-11-10 14:25:37est

@summary: sample program.
@require: conf, pathconf, runtool
"""

import sys, os
import conf, pathconf, runtool


def dowork():
    pc = pathconf.PathConf()
    userapp = pc.readPaths( pc.getUserFilename("command.conf", "") )

    P = runtool.Dispatcher()
    ds = runtool.DefaultSetting( userapp )
    ac = P.new( ds )
    ss = runtool.Setter( pc.readPaths() )
    ss.set( { "appname":"jacat", "param":"/tmp" } )
    ac.load( ss )
    ac.run()

    try:
        ad = P.new( ds )
        st = runtool.Setter( pathconf.PATHS )
        st.set( { "appname":"ls", "param":" -la /" } )
        ad.load( st )
        ad.run()
        pass
    except:
        print "[II] arbitrary command execution is banned."
        pass
    ##
    pass

def main( args ):
    res = 0
    ##
    res = dowork()
    ##
    return res
##
if( __name__ == "__main__" ):
    ret = main( sys.argv )
    sys.exit( ret )
    pass
#-eof-#
