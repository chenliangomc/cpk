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

@author: Liang Chen
@copyright: 2014, 2015

@since: 2015-1109-1202.52est on lcpc
"""

import os
import conf


class DefaultSetting:
    """
    default program launch setting
    """

    def __init__( self, obj ):
        """
        @raise ValueError: if I{obj} is not a dictionary object.
        """
        if( isinstance( obj, dict ) ):
            self.__user_app = obj
            pass
        else:
            raise ValueError, "obj must be a dictionary."
        pass

    def get( self, apptype ):
        """
        @return:

        the default setting for the given apptype.

        None if error occurs.
        """
        res = None
        ##
        dSet = {
            "native" : ("",""), # do NOT change this line
            # "app_type" : ( "program", "--app-file" )
            "java"   : ( "java", "-jar", ),
            "python" : ( "python", "", ),
            }
        ##
        if( isinstance( apptype, str ) ):
            try:
                res = dSet[ apptype ]
                pass
            except KeyError:
                raise ValueError, "incorrect apptype."
                pass
            pass
        else:
            raise ValueError, "apptype must be a string."
        ##
        return res

    def getUser( self ):
        """
        @return: user overrided program settings
        """
        res = self.__user_app
        return res
##
class Caller:
    """
    external program caller.
    """

    def __init__( self, obj ):
        self.__flags__ = {
            "debug": True,
            "dryrun": False,
            }
        #
        self.__dset = obj
        self.__job = None
        #
        self.__ready = False
        ##
        pass

    def __assemble__( self ):
        cmdlst = self.__job.getCmd()
        res = " ".join( cmdlst )
        return res

    def load( self, obj ):
        """
        load actual job settings.

        @raise RuntimeError: if setting has been loaded.
        @raise ValueError: if setting validation fails.
        """
        if( self.__ready ):
            raise RuntimeError, "job already loaded."
        else:
            if( isinstance( obj, Setter ) ):
                # validate the settings
                if( obj.validate( self.__dset ) ):
                    self.__job = obj
                    # job validated, ready to run
                    self.__ready = True
                    ##
                    pass
                else:
                    raise ValueError, "job setting validation failed."
                pass
            else:
                raise ValueError, "obj must be an instance of Setter class."
            pass
        ##
        pass

    def run( self ):
        """
        run the job.

        @return: the exit value of the called external program.
        """
        res = 0
        ##
        if( self.__ready ):
            # assemble the command line string
            cmdline = self.__assemble__()
            #
            if( self.__flags__["debug"] ):
                print cmdline
                pass
            # run the command
            if( not(self.__flags__["dryrun"]) ):
                try:
                    res = os.system( cmdline )
                    pass
                except:
                    print "Error raises when running external program."
                    pass
                pass
            else:
                pass
            pass
        else:
            res = -1
            raise RuntimeError, "job not loaded yet."
        ##
        return res
    pass
##
class Setter:
    """
    external program parameter helper class
    """

    def __init__( self, obj ):
        self.__basic = obj
        self.__dset = None
        self.__job = None
        pass

    def set( self, job ):
        """
        set the parameters of the actual job.

        @raise ValueError: if I{job} is not a dictionary object.
        """
        if( isinstance( job, dict ) ):
            self.__job = job
            pass
        else:
            raise ValueError, "job must be a dictionary."
        pass

    def __getType__( self ):
        res = ""
        try:
            res = self.__basic[ self.__job["appname"] ]["type"]
            pass
        except:
            #res = "native"
            pass
        ##
        return res
    def essentialKey( self ):
        """
        @return: the essential key names that the job dictionary must have.
        """
        res = ( "appname", "param", )
        return res

    def getCmd( self ):
        """
        generate the complete command line string

        @return: a list of command line tokens
        @since: 2015-1111-1310.29est on dhn
        """
        res = list()
        ##
        appname = self.__job["appname"]
        apptype = self.__getType__()

        appcfg = self.__dset.get( apptype )

        userapp = ( self.__dset.getUser() )[ apptype ]

        sysbin = ( "sys" == userapp["use"] )

        progfile = os.path.join( self.__basic[ appname ]["path"], self.__basic[ appname ]["fname"] )

        # runtime prefix
        if( sysbin ):
            res.append( appcfg[0] )
            pass
        else:
            res.append( userapp["path"] )
            pass

        # additional option
        res.append( userapp["option"] )

        # program file
        res.append( appcfg[1] )
        res.append( progfile )

        # job param
        res.append( self.__job["param"] )

        # eliminate empty string
        res = [ s for s in res if( len(s) > 0 ) ]
        ##
        return res

    def validate( self, dset=None ):
        """
        validate the settings of the job.

        @return:

        True if the setting is valid.

        False otherwise.

        @raise ValueError: if errors were found in the setting.
        """
        res = False
        ##
        if( ( self.__job is None )or( dset is None )or(self.__basic is None) ):
            # no data loaded.
            res = False
            pass
        else:
            # inject defaults
            self.__dset = dset

            # essential element check
            essential = self.essentialKey()
            for item in essential:
                if( self.__job.has_key(item) ):
                    res = True
                    pass
                else:
                    res = False
                    break
                pass

            # type check
            if( res ):
                # get user override
                userapp = self.__dset.getUser()
                avail_types = set( userapp["command"]["type"].split(",") )
                atype = self.__getType__()
                # check type mask
                if( atype in avail_types ):
                    override_label = userapp[ atype ]["use"]
                    # check override label
                    if( override_label in ( "sys","user" ) ):
                        pass
                    else:
                        res = False
                        raise ValueError, "'use' key should be either 'sys' or 'user'."
                    pass
                else:
                    res = False
                    raise ValueError, "external program type '%s' is disabled."%(atype)
                pass
            ##
            pass
        ##
        return res
    pass
##
class Dispatcher:
    """
    Caller provider class.
    """

    def __init__( self ):
        pass

    def new( self, obj ):
        """
        @return: a Caller object.
        """
        res = Caller( obj )
        ##
        return res
    pass
#--eof--#
