import pyautogui as pg  
import math  

pg.sleep(5)  # 5 saniye beklemeyi sağla

r = 300  # dairenin yarıçapını tanımla
(x, y) = (985, 539)  # başlangıç koordinatlarını tanımla

pg.moveTo(x + r, y)  # fareyi belirtilen noktaya taşı

pg.mouseDown()  # fareyi basılı tut

for i in range(0, 361, 6):  # 0 ile 360 derece aralığında 6'şar derecelik adımlarla dön
    pg.moveTo(x + r * math.cos(math.radians(i)), y + r * math.sin(math.radians(i)), 0)  # yeni konumu hesapla ve fareyi taşı

pg.mouseUp()  # fareyi bırak