﻿define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene hotel room
    play music "hotel.ogg"

    "Вы создали новую игру Ren'Py."

    "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
