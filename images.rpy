init python hide: #배경이미지
    for file in renpy.list_files():
        if file.startswith('images/bg'): 
            if file.endswith('.png'):
                name = file.replace('images/bg/','').replace('/bg_', '_').replace('.png','')
                name='bg_'+name
                renpy.image(name, Image(file))
                continue
            continue


init python hide: #캐릭터이미지
    for file in renpy.list_files():
        if file.startswith('images/character'): 
            if file.endswith('.png'):
                name = file.replace('images/character/','').replace('/', ' ').replace('.png','')
                renpy.image(name, Image(file))
                continue
            continue