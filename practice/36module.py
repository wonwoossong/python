#만약에 사고나서 타이어나 범퍼가 고장났으면 그것만 고치면 유지보수가 쉽다
#모듈도 똑같아
# teather module 사용하자 
import teather_module
teather_module.price(3)
teather_module.price_morning(4)
teather_module.price_soldier(5)

import teather_module as mv#별명으로 줄일수도 있다
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from teather_module import *
price(3)
price_morning(4)
price_soldier(5)

from teather_module import price,price_morning
price(5)
price_morning(6)

from teather_module import price_soldier as soldier
soldier(7)