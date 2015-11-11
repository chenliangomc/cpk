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
    2015-1102-1712.06est on lcpc, create module

    2015-1109-1836.06est on lcpc, add getUserFilename()

    2015-1110-1857.18est on lcpc, add optional param for readPaths()

    2015-1110-1901.34est on lcpc, depreciate a private method
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

    def getDefaultBasename( self ):
        """
        return the default config filename.
        """
        res = "paths.conf"
        return res

    def getDefaultFilename( self ):
        """
        return the path of default config file.
        =2015-1110-1858.49est on lcpc
        """
        res = os.path.join(
            self.__getModPath__(),
            self.getDefaultBasename()
            )
        return res

    def readPaths( self, path="" ):
        """
        read the default config file and return a Conf object.

        return None if error occurs.

        =2015-1110-1853.52est on lcpc, add path support.
        """
        res = None
        ##
        aPath = self.getDefaultFilename() #self.__getDefaultConf__()
        if( isinstance( path, str ) ):
            if( len(path) > 1 ):
                aPath = path
                pass
            pass
        ##
        if( os.path.exists( aPath ) ):
            cc = conf.Conf()
            res = cc.read( aPath )
            pass
        else:
            raise IOError, "[EE] cannot open default config file at %s"%( aPath )
        ##
        return res
    def getUserFilename( self, fname="", path="" ):
        """
        =2015-1109-1830.22est on lcpc
        write initial version
        =2015-1109-1832.54est on lcpc

        =2015-1110-1848.40est on lcpc, add userpath support
        """
        uwdir = os.getcwd()
        uhome = os.path.expanduser("~")
        ##
        ufname = ".paths.conf"
        if( isinstance( fname, str ) ):
            if( len(fname) > 1 ):
                ufname = fname
                pass
            pass
        ##
        udir = uwdir
        if( isinstance( path, str ) ):
            if( len( path ) > 0 ):
                udir = path
                pass
            pass
        ##
        res = os.path.join( udir, ufname )
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
