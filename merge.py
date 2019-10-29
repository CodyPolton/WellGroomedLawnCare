
from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

template = "InvoiceTemplate2df.docx"
document = MailMerge(template)
print(document.get_merge_fields())

# jobs_history = [{

#     'Qty': 
# }]


document.merge(
    Qty = 'Cody Polton',
    Total = "6969"
)


document.write('test-output.docx')