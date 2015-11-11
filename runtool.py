##
#  Liang Chen (C) Copyright 2008--2015
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
#  This Source Code Form is "Incompatible With Secondary Licenses", as
#  defined by the Mozilla Public License, v. 2.0.
##

"""
Run external program

Author: Liang Chen (C) Copyright 2008--2015

Changelog:

2015-1109-1202.52est on lcpc, module created by Liang
"""

import os
import conf
##
defaultProgramSetting = {
    # default program launch setting
    # "app_type" : ( "program", "--app-file" )
    "java"   : ( "java", "-jar", ),
    "python" : ( "python", "", ),
}
##
class Caller:
    """
    a external program caller.
    """
    def __init__( self, obj ):
        self.__flags__ = {
            "debug": True,
            }
        ##
        pass
    def __assemble__( self ):
        cmdlst = list()
        ##

        # eliminate empty string
        cmdlst = [ s for s in cmdlst if( len(s) > 0 ) ]
        ##
        res = " ".join( cmdlst )
        return res
    def load( self, obj ):
        """
        load actual job settings.
        """
        pass
    def run( self ):
        """
        run the job.
        """
        res = 0
        ##
        # assemble the command line string
        cmdline = self.__assemble__()
        if( self.__flags__["debug"] ):
            print cmdline
            pass
        # run the command
        try:
            res = os.system( cmdline )
            pass
        except:
            print ""
            pass
        ##
        return res
    pass
##
class Setter:
    """
    external program parameter helper class
    """
    def __init__( self ):
        pass
    def set( self, obj ):
        """
        set the parameters of the instance.
        """
        pass
    def get( self ):
        res = None
        return res
    def validate( self ):
        """
        validate the settings of the instance.
        """
        res = False
        ##
        return res
    pass
##
class Dispatcher:
    """
    a Caller provider class.
    """
    def __init__( self ):
        pass
    def new( self, obj ):
        """
        return a Caller object.
        """
        res = None
        ##
        ar = Caller()
        ar.set( obj )
        # validate the settings
        if( ar.validate() ):
            res = ar
            pass
        ##
        return re
    pass
#--eof--#
