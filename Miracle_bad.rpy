label Miracle_bad:

    $ prolog_time()

    $ volume (0.25, "sound_loop2")
    play sound_loop2 sfx_Tictak

    scene bg int_semen_room_1

    window show
    show dv angry pioneer at center with dissolve
    dv "Как я тут оказалась?!"
    dv "Анука отвечай!"
    my "А ты, кто вообще?! И что делаешь в моей квартире?"
    show dv rage pioneer at center with dspr
    dv "Сейчас узнаешь!.."

    play sound sfx_face_slap

    with flash_red

    stop ambience

    scene bg black
    with dspr

    play sound sfx_face_slap

    th "Меня побила девчонка, какая ирония. Ха, ха…"
    window hide

    stop sound_loop2 fadeout 2

    $ renpy.pause(1, hard=True)

    show credits my_credits6:
        xalign 0.5
        ypos 1.3
        linear 52.0 ypos -4.0

    $ renpy.pause(20, hard=True)

    return

# вс, 23/января/2022., 05:40 PM., Закончен.
