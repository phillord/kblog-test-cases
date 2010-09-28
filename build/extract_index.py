#!/usr/bin/env python

import sys
import pickle
import os

## all nicked from blogpost...
class Namespace(object):
    """
    Ad-hoc namespace.
    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    # This is here so unpickling <0.9.1 cache files still works.
    def __setstate__(self, state):
        self.categories = []        # Attribute added at version 0.9.1
        self.__dict__.update(state)
        self.__class__ = Cache      # Cache class name change in 0.9.1


class Cache(Namespace):
    pass

class Media(object):

    def __init__(self, filename):
        self.filename = filename # Client file name.
        self.checksum = None     # Client file MD5 checksum.
        self.url = None          # WordPress media file URL.

    def upload(self, blog):
        """
        Upload media file to WordPress server if it is new or has changed.
        """
        checksum = md5.new(open(self.filename).read()).hexdigest()
        if not (blog.options.force
                or self.checksum is None
                or self.checksum != checksum):
            infomsg('skipping unmodified: %s' % self.filename)
        else:
            infomsg('uploading: %s...' % self.filename)
            if not blog.options.dry_run:
                self.url =  blog.server.newMediaObject(self.filename)
                print 'url: %s' % self.url
            else:
                self.url = self.filename  # Dummy value for debugging.
            self.checksum = checksum


sys.argv.pop( 0 )
for i in os.walk( '.' ):
    directory = i[0]
    files = i[2]

    for j in files:
        if( j.endswith( ".blogpost" ) ):
            file = directory + "/" + j
            cache = pickle.load(open( file  ))
            print( cache.title  + "\n\t\t" + cache.url + "\n\t\t" + file ) 

