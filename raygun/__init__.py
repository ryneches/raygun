import os
import shutil

"""
A simple BLAST wrapper. Use raygun to zap things.
"""

DEFAULT_E = 0.001

FIELDS = [ 'query', 'subject', 'percent_id', 'length', 'missmatches',
'gaps', 'qstart', 'qend', 'sstart', 'send', 'e', 'bit' ]

INTFIELDS = [ 'length', 'missmatches', 'gaps', 'qstart', 'qend',
'sstart', 'send' ]

FLOATFIELDS = [ 'percent_id', 'e', 'bit' ]

class RayGun :

    def __init__( self, infile ) :
        path = os.path.abspath( infile )
        self.DIR = '/tmp/raygun-' + str(int(os.times()[4]))
        os.mkdir( self.DIR )
        cmd = 'cd ' + self.DIR + '; formatdb -p F -i ' + path + ' -n raygun'
        assert os.system( cmd ) == 0

    def blastfile( self, infile, e = DEFAULT_E ) :
        """
        Run a BLAST search using an input file for the query sequence(s).  
        Set your own e-value if you want. Returns a list of dictionaries 
        for each hit.  
        """
        path = os.path.abspath( infile )
        cmd = 'cd ' + self.DIR + '; blastall -p blastn -d raygun -i ' + path + ' -m 8 -e ' + str(e)
        m = os.popen( cmd )
        hits = []
        for hit in m.read().strip().split('\n') :
            h = dict(zip( FIELDS, hit.split() ))
            for field in INTFIELDS :
                h[ field ] = int( h[ field ] )
            for field in FLOATFIELDS :
                h[ field ] = float( h[ field ] )
            hits.append( h )
        return hits

    def blastseq( self, seq, queryname = 'query', e = DEFAULT_E ) :
        """
        Run a BLAST search using a string for the query sequence (i.e., 
        only one sequence). Set your own e-value if you want. Returns
        a list of dictionaries for each hit. The query sequence
        identifier will be 'query' unless you set queryname.
        """
        q = self.DIR + '/query.fa'
        open( q, 'w' ).write( '>' + queryname +'\n' + str(seq) )
        return self.blastfile( q, e )
            
    def __del__( self ) :
        shutil.rmtree( self.DIR )
        
