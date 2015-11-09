##
#  Liang Chen (C) Copyright 2014, 2015
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
#  This Source Code Form is "Incompatible With Secondary Licenses", as
#  defined by the Mozilla Public License, v. 2.0.
##

"""
Liang Chen (C) Copyright 2014, 2015

Path config module.

Usage:  import this module and read pathconf.PATHS object.

Changelog:
    2015-1102-1712.06est on lcpc
"""

import os
import conf

class PathConf:
    """
    Path Config reader.

    This class may raise IOError exception.
    """
    def __init__( self ):
        pass

    def __getModPath__( self ):
        mod_file_path = os.path.realpath( __file__ )
        mod_path = os.path.dirname( mod_file_path )
        return mod_path

    def __getDefaultConf__( self ):
        default_conf = os.path.join(
            self.__getModPath__(),
            self.getDefaultFilename()
            )
        return default_conf

    def getDefaultFilename( self ):
        """
        return the default config filename.
        """
        res = "paths.conf"
        return res

    def readPaths( self ):
        """
        read the default config file and return a Conf object.

        return None if error occurs.
        """
        res = None
        ##
        aPath = self.__getDefaultConf__()
        if( os.path.exists( aPath ) ):
            cc = conf.Conf()
            res = cc.read( aPath )
            pass
        else:
            raise IOError, "[EE] cannot open default config file at %s"%( aPath )
        ##
        return res
    pass
##
PATHS = None

if( __name__ == "__main__" ):
    pass
else:
    if( PATHS is None ):
        __pc__ = PathConf()
        PATHS = __pc__.readPaths()
        pass
    else:
        pass
    pass
#--eof--#
