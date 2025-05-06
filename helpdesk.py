from frappe import _

def get_data():
    return [
        {
            "label": _("Helpdesk"),
            "items": [
                {
                    "type": "doctype",
                    "name": "HD Ticket",
                    "label": _("HD Ticket"),
                },
                {
                    "type": "doctype",
                    "name": "HD Notification",
                    "label": _("HD Notification"),
                }
            ],
        }
    ]
