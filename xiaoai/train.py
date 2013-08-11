# -*- coding: utf-8 -*- 
from xml.dom import minidom
import Utils
import os
import codecs
#from Utils import chineseSplit
from LangSupport import UnicodeSupport

def createcategory(pattern, template):
	xmldoc = minidom.Document()
	root = xmldoc.appendChild(xmldoc.createElement('aiml'))
	cg = xmldoc.createElement('category')
	pt = xmldoc.createElement('pattern')
	pt.appendChild(xmldoc.createTextNode(UnicodeSupport().input(Utils.toUpperCase(pattern))))
	tp = xmldoc.createElement('template')
	tp.appendChild(xmldoc.createTextNode(template))
	cg.appendChild(pt)
	cg.appendChild(tp)
	root.appendChild(cg)
	return xmldoc

def addcategory(xmldoc, cgdom):
	root = xmldoc.getElementsByTagName('aiml')[0]
	cg = cgdom.getElementsByTagName('category')[0]
	root.appendChild(cg)
	return xmldoc

def addtobrain(kernel, filename, xmldoc):
	if not os.path.exists(filename):
		file = codecs.open(filename, 'w', encoding='utf-8')
		xmldoc.writexml(file, encoding='utf-8')
		file.close()
	else:
		xmldom = minidom.parse(filename)
		addcategory(xmldom, xmldoc)
		file = codecs.open(filename, 'w', encoding='utf-8')
		xmldom.writexml(file, encoding='utf-8')
		file.close()
	kernel.learn(filename)

def test_systemresponse(kernel):
	kernel.systemresponse = "success"

globals()['createcategory'] = createcategory
globals()['addtobrain'] = addtobrain
globals()['addcategory'] = addcategory
globals()['test_systemresponse'] = test_systemresponse
		
