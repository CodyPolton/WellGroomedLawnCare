
from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

template = "C:\\Users\\tso2080\\Documents\\Python Scripts\\WellGroomedLawnCare\\InvoiceTemplate.docx"
document = MailMerge(template)
print(document.get_merge_fields())

jobs_history = [{

    'Qty': "1",
    'JobAddress': '810 Cambridge Dr.',
    'Description': "Mowing",
    'UPrice': '70.00',
    'LinePrice': '70.00'
},{
    'Qty': "12",
    'JobAddress': '810 Cambridge Dr.',
    'Description': "Mowing x2asdfas df f asd fasd f asd f asdf asd f asdf asdf das f sdaf sd",
    'UPrice': '70.00',
    'LinePrice': '140.00'
}
]

document.merge(BillingName = "Cody Polton")
document.merge_rows('Qty', jobs_history)


document.write('test-output.docx')