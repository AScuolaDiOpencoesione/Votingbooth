import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

import requests
import json

import oembed
import types
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

twitter_handles = [
	{"ID_ASOC":1,   "twitter":"@ASOC_Bovalino"},
	{"ID_ASOC":2,   "twitter":"@Cittadinanza_EC"},
	{"ID_ASOC":4,   "twitter":"@OPENRIGHI16"},
	{"ID_ASOC":5,   "twitter":"@FASANELLIMARIA1"},
	{"ID_ASOC":9,   "twitter":"@Einaudi2g"},
	{"ID_ASOC":10,  "twitter":"@ASOC4C"},
	{"ID_ASOC":14,  "twitter":"@OpencoesioneVd"},
	{"ID_ASOC":15,  "twitter":"@TERZAFDA"},
	{"ID_ASOC":16,  "twitter":"@3ALC_GTGIORDANI"},
	{"ID_ASOC":18,  "twitter":""},
	{"ID_ASOC":23,  "twitter":"@QUARTAE201516"},
	{"ID_ASOC":24,  "twitter":"@DREAMWARRIORS4F"},
	{"ID_ASOC":30,  "twitter":"@ITASPERTINI"},
	{"ID_ASOC":31,  "twitter":"@IISBOCCARDIASOC"},
	{"ID_ASOC":35,  "twitter":"@OPENCOESIONETER"},
	{"ID_ASOC":36,  "twitter":"@OKriptal"},
	{"ID_ASOC":37,  "twitter":"@Letsflytogethe1"},
	{"ID_ASOC":38,  "twitter":"@IRDTEP"},
	{"ID_ASOC":42,  "twitter":"@belvedereasoc"},
	{"ID_ASOC":43,  "twitter":"@3LBACHELET"},
	{"ID_ASOC":44,  "twitter":"@4OPENYOURMIND"},
	{"ID_ASOC":45,  "twitter":"@4H_CASTELNUOVO"},
	{"ID_ASOC":50,  "twitter":"@4CPIN_FORMA"},
	{"ID_ASOC":54,  "twitter":"@LIFEAVERSA"},
	{"ID_ASOC":56,  "twitter":"@opencoesioneme1"},
	{"ID_ASOC":62,  "twitter":"@OPENCOESIONE4AT"},
	{"ID_ASOC":63,  "twitter":"@DR5EAMTEAM"},
	{"ID_ASOC":65,  "twitter":"@ASOC4AC"},
	{"ID_ASOC":66,  "twitter":"@PIRIAROSARNO1"},
	{"ID_ASOC":67,  "twitter":"@LOPENCOESIONE"},
	{"ID_ASOC":68,  "twitter":"@REVIVAL4SOUTH"},
	{"ID_ASOC":69,  "twitter":"@EUROPECOHESION"},
	{"ID_ASOC":70,  "twitter":"@OPENCASTIGLIANO"},
	{"ID_ASOC":71,  "twitter":"@ISAMEDEODAOSTA"},
	{"ID_ASOC":75,  "twitter":"@MISIGROUP"},
	{"ID_ASOC":78,  "twitter":"@BERTI3H"},
	{"ID_ASOC":83,  "twitter":""},
	{"ID_ASOC":84,  "twitter":""},
	{"ID_ASOC":86,  "twitter":"@IPECOSISTEMA"},
	{"ID_ASOC":87,  "twitter":"@GREENGUARDIANA1"},
	{"ID_ASOC":88,  "twitter":"@Itet_MarcoPolo_"},
	{"ID_ASOC":91,  "twitter":"@PACINOTTI_TEAM"},
	{"ID_ASOC":92,  "twitter":"@CLASSE3I"},
	{"ID_ASOC":94,  "twitter":"@LAVINAENERGY15"},
	{"ID_ASOC":95,  "twitter":"@BOYSWATERSTABIA"},
	{"ID_ASOC":97,  "twitter":"@ASOCSEARANGERS"},
	{"ID_ASOC":103, "twitter":"@ITIPRIMOLEVI"},
	{"ID_ASOC":105, "twitter":"@LUMIMEZZOGIORNO"},
	{"ID_ASOC":110, "twitter":"@ASOC_LAC3D"},
	{"ID_ASOC":111, "twitter":"@OPENWOODTEAM"},
	{"ID_ASOC":113, "twitter":"@ARENA_OPEN"},
	{"ID_ASOC":116, "twitter":"@lll_bu"},
	{"ID_ASOC":118, "twitter":"@BOULEVARDGUYS"},
	{"ID_ASOC":119, "twitter":"@FICCANASOA"},
	{"ID_ASOC":130, "twitter":"@RICCIAGREENTEAM"},
	{"ID_ASOC":133, "twitter":"@opencoesione5xF"},
	{"ID_ASOC":135, "twitter":"@IPIADEVIVO1"},
	{"ID_ASOC":136, "twitter":"@CALAIMANU2015"},
	{"ID_ASOC":137, "twitter":"@diffondoenonaff"},
	{"ID_ASOC":140, "twitter":"@CULTURE_SAVERS"},
	{"ID_ASOC":141, "twitter":"@DREPANON_"},
	{"ID_ASOC":144, "twitter":"@ASOC3MGRAMSCI"},
	{"ID_ASOC":149, "twitter":"@3BOPENCOESIONE"},
	{"ID_ASOC":152, "twitter":"@timetosdream"},
	{"ID_ASOC":156, "twitter":"@IVACOESE"},
	{"ID_ASOC":160, "twitter":"@3asavecchi"},
	{"ID_ASOC":164, "twitter":"@ASOC4A"},
	{"ID_ASOC":168, "twitter":""},
	{"ID_ASOC":169, "twitter":"@OPENMASCI"}
]


def showitem(request, section_id, field=0):

	key = request.get_full_path()
	kk = r.get(key)
	if kk:
		return HttpResponse(kk)
	itms = json.load(open("votingstructure.json"))
	structure = itms.get("structure")
	db = itms.get("db")
	db_long = itms.get("db_meta")
	db_repeater = itms.get("db_repeater")
	dim = itms.get("dimension")
	dimv = request.GET.get(dim)
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
			return render(request, "render_view.html", {"field":field, "section":s, "context":sh})

def pimp(items, db, db_long, db_repeater, dim, dimv):
	#consumer = oembed.OEmbedConsumer()
	#consumer.addEndpoint(oembed.OEmbedEndpoint("http://www.youtube.com/oembed",["http://youtu.be/*"]))
	#consumer.addEndpoint(oembed.OEmbedEndpoint("http://live.amcharts.com/oembed",["http://live.amcharts.com/*"]))
	#consumer.addEndpoint(oembed.OEmbedEndpoint("https://vimeo.com/api/oembed.json",["http://vimeo.com/*","http://vimeo.com/groups/*/videos/*", "https://vimeo.com/*", "https://vimeo.com/groups/*/videos/*"]))
	#consumer.addEndpoint(oembed.OEmbedEndpoint("http://www.screenr.com/api/oembed.{format}",["http://www.screenr.com/*/"]))
	#consumer.addEndpoint(oembed.OEmbedEndpoint("http://prezi.com/",["http://prezi.com/*/*"]))
	
	
	to_get = [f.get("field") for f in items if (f.get("field") != "" and not f.get("table"))]
	to_get_T = [f.get("type") for f in items if (f.get("field") != ""  and not f.get("table"))]
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
		#if f["type"] == "oembed" or f["type"]== "oembed_nullable":
		#	try:
		#		print f["field"]
		#		#f["field"] = f["field"].replace("http:// ", "")
		#		#f["field"] = consumer.embed(f["field"])["html"]
		#	except:
		#		f["type"] = "iframe_url"
		if f["type"]== "date":
			f["field"] = f["field"][6:8]+"/"+f["field"][4:6]+"/"+f["field"][0:4]
		if f["type"] == "long_text":
			f["type"] = "text"
			nurl = db_long+"filter_field="+dim+"&filter_value="+dimv+"&field="+f["field"]+"&table="+f["table"]
			print nurl
			ret_raw = requests.get(nurl)
			ret_raw = ret_raw.json()
			if len(ret_raw) == 1:
				f["field"] = ret_raw[0].get("value")
			else:
				f["field"] = None
		if f["type"] == "repeater":
			nurl = db_repeater+"filter_field="+dim+"&filter_value="+dimv+"&field="+f["field"]+"&table="+f["table"]+"&parent="+f["acf_parent"]+"&child="+f["acf_child"]
			print nurl
			ret_raw = requests.get(nurl)
			ret_raw = ret_raw.json()
			if len(ret_raw) == 1:
				f["field"] = ret_raw[0].get("value")
			else:
				f["field"] = None
		if f["type"] == "twitter":
			for t in twitter_handles:
				print type(f), type(dimv), type(t)
				if str(t["ID_ASOC"]) == dimv:
					print ">>>>", dimv, t
					f["field"] = "https://twitter.com/"+t["twitter"]
				print f

def flatten(l):
	for el in l:
		if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
			for sub in flatten(el):
				yield sub
		else:
			yield el