frappe.listview_settings['Transactions']={
    add_fields:["transaction_type"],
    get_indicator: function(doc){
        if (doc.transaction_type=="Issue") {
            return[__("Issue"),"red","status,=,Issue"];
            //return[__("Red","status,=,Issue")];
        }
        else if (doc.transaction_type=="Return"){
            return[__("Return"),"green","status,=,Return"];
        }    
    }
};
/*frappe.ui.form.on("Transactions","transaction_date",
                  function (frm) {
                    frappe.call({
                        args: {
                            doctype:"Transactions",
                            date: frm.doc.transaction_date
                        },
                    })
                  });
*/
function datevalidation() {
    var x = document.forms["Transactions"]["transaction_date"].value;
    if (x > Date()) {
        alert("Date cannot greater then today's date");
        return false;
    }
}