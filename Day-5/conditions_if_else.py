# 2 Conditions

import sys

vm_type = sys.argv[1]

if vm_type == "t2.micro":
    print("VM creation in process...and its t2.micro")
else:
    print("VM type has to be t2.micro")
