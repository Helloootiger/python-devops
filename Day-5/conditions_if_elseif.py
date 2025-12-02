# Multiple Conditions

import sys

vm_type = sys.argv[1]

if vm_type == "t2.micro":
    print("VM creation in process...and its t2.micro")
elif vm_type == "t2.medium":
    print("VM creation in process...and its t2.medium")
elif vm_type == "t2.xlarge":
    print("VM creation in process...and its t2.xlarge")
else:
    print("Provide valid VM type")