#!/usr/bin/python
import pickle

import happybase
import json
from datetime import datetime
import os

host = "192.168.0.20"
namespace = "hep_4116W_tag"
table_name = "tag_padding_4"

connection = happybase.Connection(host = host, timeout = 1800000, table_prefix = namespace, table_prefix_separator = ":")
connection.open()

table = connection.table(table_name)

query_opt_list = json.load(open("./opt.json"))
query_num_list = json.load(open("./num.json"))

def BechThisOpt(query_opt_str):
	
	row_start = query_opt_str+"#"
	row_stop = query_opt_str+"#a"

	start_datetime = datetime.now()
	this_query = table.scan(row_start = row_start.encode('utf-8'), row_stop = row_stop.encode('utf-8'))
	
	num_ret_data = 0
	for key, data in this_query:
		num_ret_data += 1

	end_datetime = datetime.now()

	duration = end_datetime - start_datetime
	return duration, num_ret_data

result_list = []

f = open('query_with_row_start.plk','wb')
for i in range(len(query_opt_list)):
	this_duration, this_num_ret_data = BechThisOpt(query_opt_list[i])
	print this_duration, this_num_ret_data

	result_list.append({'duration':this_duration, 'got_num':this_num_ret_data})

pickle.dump(result_list, f)
f.close()
connection.close()