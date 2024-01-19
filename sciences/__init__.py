"""File-file serta folder yang sejajar dengan init akan dibantu oleh file init
untuk dihubungkan dengan folder diatasnya jika diperlukan import statement
ke file program lain.
"""


from . import physics #artinya : tolong hubungkan file physics dengan folder di atasnya.

"bisa juga nulis seperti ini langsung"
from .physics import hukum_2_newton #gaperlu nulis namespace physics lagi, kalau ditulis juga gapapa
from .physics import work #sama, yang ini juga.

import math
from . math import basic,scientific
from .math.basic import add
from .math.basic import times
from .math.scientific import exponen





