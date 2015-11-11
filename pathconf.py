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
Path config module.

Author: Liang Chen (C) Copyright 2014, 2015

Usage:  import this module and read pathconf.PATHS object.

Changelog:

2015-1102-1712.06est on lcpc, create module

2015-1109-1836.06est on lcpc, add getUserFilename()

2015-1110-1857.18est on lcpc, add optional param for readPaths()

2015-1110-1901.34est on lcpc, depreciate a private method

2015-1111-1227.13est on dhn, bugfix in docstring
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

    def getDefaultBasename( self ):
        """
        return the default config filename.

        Changelog:

        2015-1110-1901.34est on lcpc, add this function.
        """
        res = "paths.conf"
        return res

    def getDefaultFilename( self ):
        """
        return the path of default config file.
        
        Changelog:

        2015-1110-1858.49est on lcpc, return the full path.
        """
        res = os.path.join(
            self.__getModPath__(),
            self.getDefaultBasename()
            )
        return res

    def readPaths( self, path="" ):
        """
        read the config file specified by 'path' and return the contents read by Conf object.

        return None if error occurs.

        Changelog:

        2015-1110-1853.52est on lcpc, add path support.
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
        build a path string to user config file.

        if 'path' is omitted or empty string, the current working dir is used as the path.

        Changelog:

        write initial version between 2015-1109-1830.22est and 2015-1109-1832.54est on lcpc

        2015-1110-1848.40est on lcpc, add userpath support
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
