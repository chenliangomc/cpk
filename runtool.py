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
class DefaultSetting:
    """
    default program launch setting
    """
    def __init__( self ):
        pass
    def get( self, appname ):
        """
        return the default setting for the given app.

        return None if error occurs.
        """
        res = None
        ##
        dSet = {
            # "app_type" : ( "program", "--app-file" )
            "java"   : ( "java", "-jar", ),
            "python" : ( "python", "", ),
            }
        ##
        if( isinstance( appname, str ) ):
            try:
                res = dSet[ appname ]
                pass
            except KeyError:
                raise ValueError, "incorrect appname."
                pass
            pass
        else:
            raise ValueError, "appname must be a string."
        ##
        return res
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
        if( isinstance( obj, Setter ) ):
            # validate the settings
            if( obj.validate() ):
                pass
            else:
                raise ValueError, "job setting validation failed."
            pass
        else:
            raise ValueError, "obj must be an instance of Setter class."
        ##
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
            print "Error raises when running external program."
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
        res = Caller( obj )
        ##
        return re
    pass
#--eof--#
