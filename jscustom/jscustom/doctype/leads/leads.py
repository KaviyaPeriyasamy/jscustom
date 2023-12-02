import frappe
from frappe import _
from frappe.desk.form import assign_to

# def create_todo_for_next_followup(doc, method):
#     """
#     Server-side method to create a TODO for the next follow-up
#     """
#     if not doc.next_follow_up_date:
#         # If the next follow-up date is not specified, we won't create a TODO
#         return

#     todo = frappe.new_doc('ToDo')
#     todo.description = doc.follow_up_description or _("Follow-up for Lead: {0}").format(doc.name)
#     todo.reference_type = 'Lead'
#     todo.reference_name = doc.name
#     todo.assigned_by = frappe.session.user
#     todo.assigned_to = frappe.session.user
#     todo.status = 'Open'
#     todo.priority = 'Medium'
#     todo.date = doc.next_follow_up_date
#     todo.save(ignore_permissions=True)
#     frappe.msgprint(_("TODO created"))

# def get_hooks():
#     return {
#         "before_save": {
#             "Lead": "jscustom.jscustom.doctype.leads.leads.create_todo_for_next_followup"
#         }
#     }

@frappe.whitelist(allow_guest = True)
def create_todo(ref_type, ref_name, assigned_to, status, priority, description, date):
    try:
        todo = frappe.new_doc('ToDo')
        todo.description = description
        todo.reference_type = ref_type
        todo.reference_name = ref_name
        todo.assigned_by = frappe.session.user
        todo.allocated_to = assigned_to
        todo.status = status
        todo.priority = priority
        todo.date = date
        todo.save(ignore_permissions=True)
        return True
    except:
        frappe.throw(title="Error", msg=_("Todo not Created"))