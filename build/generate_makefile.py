#!/usr/bin/env python

import sys

sys.argv.pop( 0 )
for i in sys.argv:
    stem = i.split( '.' )[ 0 ]
    print ( stem + ".blogpost: " + stem + ".adoc" )
    print ( stem + ": " + stem + ".blogpost" ) 


