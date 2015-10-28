# -*- coding: utf-8 -*-
# Copyright (c) 2015, frappe tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Patron(Document):
	def prevent_duplicate(self):
		pass
		
	

#access the db
#call the current fields from web page
#compare it with db
# if match then throw error
# if no match then proceed to save it.