#!/usr/bin/python

## start thrift ./bin/hbase-daemon.sh start thrift
## netstat -apn | grep 9090
import happybase

def create_mytable(conn,table_name):
	# To list the available tables
	tables = conn.tables()

	if table_name in tables:
		print 'table name already in use'
	else:
		conn.create_table(table_name,{'cf':dict()})
		print "create",table_name,"successfully"

host = "192.168.1.148"
conn = happybase.Connection(host)
conn.open()
table_name = 'mytableoldschema'
create_mytable(conn,table_name)
conn.close()