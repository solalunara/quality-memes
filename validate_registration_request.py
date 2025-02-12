import sys
import json

class emptyclass:
    pass;    

class userdata:
    hash = 0;
    balances = emptyclass;

if __name__ == "__main__":
    request_plaintext = sys.argv[ 1 ];
    request = json.loads( request_plaintext );
    users_file = open( "users.json", "r" );
    users_file_str = users_file.read();
    existing = json.loads( users_file_str );
    users_file.close();
    print( existing );
    for user in existing:
        if ( request[ "uname" ] == user ):
            exit( 1 );

    existing[ request[ "uname" ] ] = { "hash": request[ "hash" ], "balances": {}};
    users_file_write = open( "users.json.new", "w" );
    users_file_write.write( json.dumps( existing, indent=2 ) );
    users_file_write.close();
