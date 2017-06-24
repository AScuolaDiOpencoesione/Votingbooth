import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

import requests
import json

import types
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def showitem(request, section_id, field=0):

	key = request.get_full_path()
	#kk = r.get(key)
	#if kk:
	#	return HttpResponse(kk)
	itms = json.load(open("votingstructure1617.json"))
	structure = itms.get("structure")
	db = itms.get("db")
	db_long = itms.get("db_meta")
	db_repeater = itms.get("db_repeater")
	dim = itms.get("dimension")
	dimv = request.GET.get(dim)
	print dim, dimv
	sh = itms.get("shared")
	pimp(sh, db, db_long, db_repeater, dim, dimv)

	for s in structure:
		if s["screen_id"] == section_id:
			fields = s["fields"]
			field = fields[int(field)]
			pimp(field, db, db_long, db_repeater, dim, dimv)
			t = loader.get_template('render_view.html')
			c = {"field":field, "section":s, "context":sh}
			r.set(key, t.render(c, request))
			kk = r.get(key)
			return HttpResponse(kk)
			#return render(request, "render_view_%s.html" % section_id, {"field":field, "section":s, "context":sh})

def pimp(items, db, db_long, db_repeater, dim, dimv):
	to_get = [f.get("field") for f in items if (f.get("field") != "" and not f.get("table"))]
	to_get_T = [f.get("type") for f in items if (f.get("field") != ""  and not f.get("table"))]
	print db, dim, dimv,",".join(to_get), ",".join(to_get_T)
	#url = db+"filter_field="+dim+"&filter_value="+dimv+"&field="+",".join(to_get)+"&ft="+",".join(to_get_T)
	url = db+"filter_field="+dim+"&filter_value="+dimv+"&field="+",".join(to_get)+"&ft="+",".join(to_get_T)
	print url
	if len(to_get) > 0:
		ret_raw = requests.get(url)
		rr = ret_raw.text
		rr = rr.replace("`", "")
		ret = json.loads(rr)
	else:
		ret = []

	for f in items:
		if f.get("field") != "":
			for r in ret:
				if r.get("field") == f.get("field"):
					f["field"] = r["value"]
		#f f["type"] == "oembed" or f["type"]== "oembed_nullable":
		#	try:
		#		print f["field"]
		#		f["field"] = f["field"].replace("http:// ", "")
		#		f["field"] = consumer.embed(f["field"])["html"]
		#	except:
		#		f["type"] = "iframe_url"
		if f["type"]== "date":
			f["field"] = f["field"][6:8]+"/"+f["field"][4:6]+"/"+f["field"][0:4]
		if f["type"] == "long_text":
			f["type"] = "text"
			#nurl = db_long+"filter_field="+dim+"&filter_value="+dimv+"&field="+f["field"]+"&table="+f["table"]
			#print nurl
			#ret_raw = requests.get(nurl)
			#ret_raw = ret_raw.json()
			#if len(ret_raw) == 1:
			#	f["field"] = ret_raw[0].get("value")
			#else:
			#	f["field"] = None
		#if f["type"] == "repeater":
		#	nurl = db_repeater+"filter_field="+dim+"&filter_value="+dimv+"&field="+f["field"]+"&table="+f["table"]+"&parent="+f["acf_parent"]+"&child="+f["acf_child"]
		#	print nurl
		#	ret_raw = requests.get(nurl)
		#	ret_raw = ret_raw.json()
		#	if len(ret_raw) == 1:
		#		f["field"] = ret_raw[0].get("value")
		#	else:
		#		f["field"] = None
		#if f["type"] == "twitter":
		#	for t in twitter_handles:
		#		print type(f), type(dimv), type(t)
		#		if str(t["ID_ASOC"]) == dimv:
		#			print ">>>>", dimv, t
		#			f["field"] = "https://twitter.com/"+t["twitter"]
		#		print f

def flatten(l):
	for el in l:
		if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
			for sub in flatten(el):
				yield sub
		else:
			yield el