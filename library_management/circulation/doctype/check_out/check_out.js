frappe.ui.form.on("Check Out", {
	onload: function(frm) {
		cur_frm.set_value("date",frappe.datetime.get_today())
	}
})