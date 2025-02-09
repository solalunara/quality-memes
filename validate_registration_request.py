import sys
import json

if __name__ == "__main__":
    request_plaintext = sys.argv[ 1 ];
    request = json.loads( request_plaintext );
    users_file = open( "users.json", "r" );
    existing = json.loads( users_file.read() );
    users_file.close();
    for user in existing.users:
        if ( request.uname == user.uname ):
            exit( 1 );

    existing.users.append( request );
    users_file_write = open( "users.json.new", "rw" );
    users_file_write.write( json.dumps( existing ) );
    users_file_write.close();
