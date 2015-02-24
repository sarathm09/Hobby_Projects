from selenium import webdriver
import os

path = raw_input("Path to folder: ")
br = webdriver.Firefox()
br.get("http://csebeta.x10.mx?login")
page = br.get("http://csebeta.x10.mx/admin.php")
files = os.listdir(path)
for i in files:
	br.get("http://csebeta.x10.mx/admin.php")
	title = br.find_element_by_name("filetitle")
	title.send_keys(i.split(".")[0])
	subs_short = ["AI", "SIC", "MC", "NN", "HPC", "AM", "ANT", "OT", "ECOM", "MT", "NLP"]
	subs_big = ["Artifi", "Secur", "Mobile", "Neur", "High", "Advanced M", "Advanced Ne", "Opti", "E Co", "Multi", "Natur"]
	subval = ""
	for j in subs_short:
		if j in i:
			print i, j
			subval = subs_big[subs_short.index(j)]
	if subval == "":
		subval = raw_input("Enter sub for " + i)
	sub = br.find_element_by_name("filesub")
	sub.send_keys(subval)
	f = br.find_element_by_name("filename")
	f.send_keys(path + "\\" + i)
	br.find_element_by_id("fileupload").click()
