import getpass
import oracledb


# pw = getpass.getpass("Enter password: ")
user="dba_gfor_rft"
pw = 'vbnfgh'

dsn ="varhins.madrid.org"
# connection = oracledb.connect(user=user, password=pw, dsn=dsn)
#  devuelve error: oracledb.exceptions.DatabaseError: DPY-4027: no configuration directory specified


# Segundo intento de conexión
host = "varhins.madrid.org"
port = 1521
service_name = "varhins"

dsn = f'{user}/{pw}@{host}:{port}/{service_name}'
# connection = oracledb.connect(dsn)
#  devuelve error: socket.gaierror: [Errno 11001] getaddrinfo failed



#  Tercer intento de conexión
params = oracledb.ConnectParams(host=host, port=port, service_name=service_name)
connection = oracledb.connect(user=user, password=pw, params=params)
#  devuelve error: socket.gaierror: [Errno 11001] getaddrinfo failed


print("Successfully connected to Oracle Database")



cursor = connection.cursor()

exit


# Create a table

cursor.execute("""
    begin
        execute immediate 'drop table todoitem';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")

cursor.execute("""
    create table todoitem (
        id number generated always as identity,
        description varchar2(4000),
        creation_ts timestamp with time zone default current_timestamp,
        done number(1,0),
        primary key (id))""")

# Insert some data

rows = [ ("Task 1", 0 ),
         ("Task 2", 0 ),
         ("Task 3", 1 ),
         ("Task 4", 0 ),
         ("Task 5", 1 ) ]

cursor.executemany("insert into todoitem (description, done) values(:1, :2)", rows)
print(cursor.rowcount, "Rows Inserted")

connection.commit()

# Now query the rows back
for row in cursor.execute('select description, done from todoitem'):
    if (row[1]):
        print(row[0], "is done")
    else:
        print(row[0], "is NOT done")