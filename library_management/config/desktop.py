# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"Library Management": {
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Library Management")
		},
	
		
		"Circulation": {
			"color": "purple",
			"icon": "octicon octicon-mirror",
			"type": "module",
			"label": _("Circulation")
		},
		
		"Procurement": {
			"color": "green",
			"icon": "octicon octicon-repo-clone",
			"type": "module",
			"label": _("Procurement")
		},
	}