# -*- coding: utf-8 -*-
# Copyright (c) 2015, frappe tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import nowdate,getdate

class Transaction(Document):
    def validate(self):
        self.validate_date()
        last_transaction = frappe.get_list("Transaction",
            fields=["transaction_type", "transaction_date"],
            filters = {
                "article": self.article,
                "transaction_date": ("<=", self.transaction_date),
                "name": ("!=", self.name)
            })
        if self.transaction_type=="Issue":
            msg = ("Article {0} has not been recorded as returned since {2}")
            if last_transaction and last_transaction[0].transaction_type=="Issue":
                frappe.throw(msg.format(self.article, self.article_name,
                    last_transaction[0].transaction_date))
        else:
            if not last_transaction or last_transaction[0].transaction_type!="Issue":
                #frappe.throw(_("Cannot return article not issued"))
                #we should not use _ or __ in between (( else it throws error.
                frappe.throw(("Cannot return article not issued"))
        
    def validate_date(self):
        print nowdate()
        print self.transaction_date
        if getdate(self.transaction_date) > getdate(nowdate()):
            frappe.throw("Date cannot be greater than today's date")
        
        if getdate(self.transaction_date) < getdate(nowdate()):
            frappe.throw("Date cannot be less than today's date")
        