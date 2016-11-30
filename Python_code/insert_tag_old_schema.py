#!/usr/bin/python

import csv
import happybase
from datetime import datetime

batch_size = 1000
host = "localhost"
file_path= "TagFile.csv"
# namespace = "hep"
row_count = 0
table_name = "tag_oldschema"

start_time = datetime.now()

def connect_to_hbase():
	conn = happybase.Connection(host = host)
	conn.open()
	table = conn.table(table_name)
	batch = table.batch(batch_size = batch_size)
	return conn, batch

def insert_row(rowkey,batch,row):
	batch.put(row[1] + "#" + "totalCharged" + "#" + row[3].zfill(3) + "#" + row[2], {"data:key":row[1]+"-"+row[2]} )
	batch.put(row[1] + "#" + "totalNeutral" + "#" + row[4].zfill(3) + "#" + row[2], {"data:key":row[1]+"-"+row[2]})
	batch.put(row[1] + "#" + "totalTrks" + "#" + row[5].zfill(3) + "#" + row[2], {"data:key":row[1]+"-"+row[2]})

def read_csv():
	csvfile = open(file_path, "r")
	csvreader = csv.reader(csvfile)
	return csvreader,csvfile

conn, batch = connect_to_hbase()
print "Connect to HBase. table name: %s, batch_size: %i" %(table_name,batch_size)
csvreader, csvfile = read_csv()
print "Connected to file. name: %s" % (file_path)

try:
	for row in csvreader:
		row_count += 1
		insert_row(row_count,batch, row)
		print row_count
	batch.send()
finally:
	csvfile.close()
	conn.close()

end_time = datetime.now()
duration = datetime.now() - start_time
print "Done. Row count: %i" % (row_count)
print "Duration: ", duration