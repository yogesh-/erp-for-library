frappe.listview_settings['Transaction']={
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