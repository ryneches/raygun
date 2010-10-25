import raygun
import os.path

try :
    import Bio.SeqRecord
    import Bio.Seq
    BIOPYTHON = True
except ImportError :
    BIOPYTHON = False

try :
    import pygr.sequence
    PYGR = True
except ImportError :
    PYGR = False


"""
Tests for raygun. 

NOTE : I gave up trying to avoid hardcoding the paths to the test
data files. As a result, you have to invoke nosetests from the module
folder (i.e., the one that has raygun's setup.py).
"""

QUERYFILE = os.path.join( os.getcwd(), 'raygun/tests/query.fa' )
TESTDB = os.path.join( os.getcwd(), 'raygun/tests/stap_16S.fa' )

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

def test_no_hit() :
    rg = raygun.RayGun( TESTDB )
    assert rg.blastseq( 'atatgaacatgcatagatcccta' ) == []

def test_query_seq_biopython() :
    if BIOPYTHON :
        rg = raygun.RayGun( TESTDB )
        seqr = Bio.SeqRecord.SeqRecord( 'GTGGGCAAGTTCTGGTGTCAGCCGCCGCG' )
        hits = rg.blastseq( seqr, e=0.1 )
        assert hits[0]['length'] == 29
        seq = Bio.Seq.Seq( 'GTGGGCAAGTTCTGGTGTCAGCCGCCGCG' )
        hits = rg.blastseq( seq, e=0.1 )
        assert hits[0]['length'] == 29

def test_query_seq_pygr() :
    if PYGR :
        rg = raygun.RayGun( TESTDB )
        seq = pygr.sequence.Sequence( 'GTGGGCAAGTTCTGGTGTCAGCCGCCGCG', 'pygrseq' )
        hits = rg.blastseq( seq, e=0.1 )
        assert hits[0]['length'] == 29
