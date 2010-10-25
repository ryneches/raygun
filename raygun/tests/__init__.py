import raygun
import os.path

"""
Tests for raygun. 

NOTE : I gave up trying to avoid hardcoding the paths to the test
data files. As a result, you have to invoke nosetests from the module
folder (i.e., the one that has raygun's __init__.py).
"""

QUERYFILE = os.path.join( os.getcwd(), 'tests/query.fa' )
TESTDB = os.path.join( os.getcwd(), 'tests/stap_16S.fa' )

def test_load_raygun() :
    rg = raygun.RayGun( TESTDB )

def test_destroy() :
    rg = raygun.RayGun( TESTDB )
    DIR = rg.DIR
    del( rg )
    assert not os.path.exists( DIR )

def test_query_file() :
    rg = raygun.RayGun( TESTDB )
    hits = rg.blastfile( QUERYFILE, 0.0001 )
    lengths = []
    for hit in hits :
        lengths.append( hit[ 'length' ] )
    assert max( lengths ) == 895

def test_query_seq_biopython() :
    rg = raygun.RayGun( TESTDB )

def test_query_seq_pygr() :
    rg = raygun.RayGun( TESTDB )
