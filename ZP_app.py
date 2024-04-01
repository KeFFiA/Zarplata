from buttons import browse
from config import root
from labeles import info
from classes import Button_Pos

info.pack(expand=True)
browse.place(x=Button_Pos.x, y=Button_Pos.y)

root.mainloop()
