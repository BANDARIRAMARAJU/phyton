# Q3. To create a sub directory in mysub directory:
"""cwd
|-mysub
|-mysub2"""

import os
os.mkdir("mysub/mysub2")
print("mysub2 created inside mysub")