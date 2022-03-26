init python:

    style.new_save_load_button = Style(style.button)
    style.new_save_load_button.background = "Miracle_in_the_form/gui/Save_Load/Return_Save_Load_Buttonl_idle.png"
    style.new_save_load_button.hover_background = "Miracle_in_the_form/gui/Save_Load/Return_Save_Load_Buttonl_hover.png"
    style.new_save_load_button.selected_background = "Miracle_in_the_form/gui/Save_Load/Return_Save_Load_Buttonl_selected.png"
    style.new_save_load_button.selected_hover_background = "Miracle_in_the_form/gui/Save_Load/Return_Save_Load_Buttonl_selected.png"
    style.new_save_load_button.selected_idle_background = "Miracle_in_the_form/gui/Save_Load/Return_Save_Load_Buttonl_selected.png"

    renpy.music.register_channel("test", "sfx", False)
    renpy.music.register_channel("Rlaugh", "sfx", False)
    renpy.music.register_channel("menu_gate", "sfx", False)


screen new_main_menu:

    python:
        # renpy.music.queue("Miracle_in_the_form/gui/music/forest_maiden.ogg", channel = "music", fadein = 1)
        renpy.music.queue("Miracle_in_the_form/gui/music/a_promise_from_distant_days_v2.ogg", channel = "music", fadein = 1)

    tag menu
    modal True
    add "Miracle_in_the_form/gui/Main_menu/main_menu.jpg"

    imagebutton:
        auto "Miracle_in_the_form/gui/Main_menu/1_%s.png"
        pos (66, 251)
        action Jump('Miracle')

    imagebutton:
        auto "Miracle_in_the_form/gui/Main_menu/2_%s.png"
        pos (66, 331)
        action ShowMenu('new_Load')

    imagebutton:
        auto "Miracle_in_the_form/gui/Main_menu/3_%s.png"
        pos (66, 411)
        action ShowMenu('new_preferences')

    imagebutton:
        auto "Miracle_in_the_form/gui/Main_menu/4_%s.png"
        pos (66, 500)
        action ShowMenu('new_quit') hovered Play("test", "Miracle_in_the_form/gui/sound/test.ogg")

    imagebutton:
        auto "Miracle_in_the_form/gui/misc/5_%s.png"
        pos (66, 800) # pos (0.89,0.85)
        action OpenURL("https://vk.com/yukiiro") hovered Play("menu_gate", "Miracle_in_the_form/gui/sound/menu_gate.ogg")


screen new_Load:

    modal True

    window background "Miracle_in_the_form/gui/Save_Load/load bg.png":
        textbutton "Назад, юхуу!.." style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()
        textbutton "Играть сохранение?" style "log_button" text_style "settings_link" yalign 0.92 xalign 0.45 action (FunctionCallback(on_load_callback,selected_slot), FileLoad(selected_slot))
        textbutton "{size=-12}{b}x{/b}{/size}"+"Удалить нафиг!" style "log_button" text_style "settings_link" yalign 0.92 xalign 0.97 action FileDelete(selected_slot)

        vbox xalign 0.023 yalign 0.5:
            grid 1 10:
                for i in range(0, 10):
                    if i == 0:
                        textbutton "Авто." text_size 50 style "log_button" text_style "settings_link" action (FilePage("avto"), SetVariable("selected_slot", False))
                    else:
                        textbutton str(i) text_size 50 right_padding 50 style "log_button" text_style "settings_link" action (FilePage(i), SetVariable("selected_slot", False))

        grid 4 3 xpos 0.13 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i) xpos 10 ypos 10
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "new_save_load_button"
                        has fixed
                        text ("%s." % i + FileTime(i, format="%d.%m.%y, %H:%M", empty=" " + translation["Empty_slot"][_preferences.language]) + "\n" + FileSaveName(i)) style "file_picker_text" xpos 15 ypos 15


screen new_quit:

    modal True

    add "Miracle_in_the_form/gui/Main_menu/screen_quit2.jpg"

    imagebutton:
        auto "Miracle_in_the_form/gui/Main_menu/6_%s.png"
        pos (1250, 108)
    textbutton "У меня булки горят, ухожу..." text_size 70 style "log_button" text_style "settings_link" xalign 0.07 yalign 0.65 text_color "#ffffff" text_hover_color "#e3a11d" action Quit(confirm=False) hovered Play("Rlaugh", "Miracle_in_the_form/gui/sound/Rlaugh.mp3")
    textbutton "Окай, остаюсь." text_size 70 style "log_button" text_style "settings_link" xalign 0.95 yalign 0.65 text_color "#ffffff" text_hover_color "#e3a11d" action Return()


screen new_preferences:

    modal True

    $ bar_null = Frame(get_image("gui/Settings/bar_null.png"),36,36)
    $ bar_full = Frame(get_image("gui/Settings/bar_full.png"),36,36)

    window background "Miracle_in_the_form/gui/Settings/preferences_bg.jpg":

        hbox xalign 0.5 yalign 0.08:
            add "Miracle_in_the_form/gui/Settings/dv_body1.png" yalign 0.65
            text " "+"Настройка игры."+" " style "settings_link" yalign 0.5 color "#ffffff"
            add "Miracle_in_the_form/gui/Settings/dv_body1.png" yalign 0.65
        textbutton "Ой.., страшно!" style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport id "preferences":
                mousewheel True
                scrollbars None

                has grid 1 18 xfill True spacing 15
                text "Режим экрана и прочее." style "settings_header" xalign 0.5 color "#ffffff"
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.fullscreen:
                            add "Miracle_in_the_form/gui/Settings/el_body1.png" ypos 0.12
                        else:
                            null width 22
                        textbutton "На весь экран." style "log_button" text_style "settings_text" text_color "#ffffff" action Preference("display", "fullscreen")

                    hbox xalign 0.5:
                        if not _preferences.fullscreen:
                            add "Miracle_in_the_form/gui/Settings/el_body1.png" ypos 0.12
                        else:
                            null width 22
                        textbutton "В окне." style "log_button" text_style "settings_text" text_color "#ffffff" action Preference("display", "window")

                text "Пропуск сюжета." style "settings_header" xalign 0.5 color "#ffffff"
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.skip_unseen:
                            add "Miracle_in_the_form/gui/Settings/mt_body1.png" ypos 0.12
                        else:
                            null width 22
                        textbutton "Пропустить всё." style "log_button" text_style "settings_text" text_color "#ffffff" action Preference("skip", "all")

                    hbox xalign 0.5:
                        if not _preferences.skip_unseen:
                            add "Miracle_in_the_form/gui/Settings/mt_body1.png" ypos 0.12
                        else:
                            null width 22
                        textbutton "Пропустить прочтённое." style "log_button" text_style "settings_text" text_color "#ffffff" action Preference("skip", "seen")

                text "Громкость." style "settings_header" xalign 0.5 color "#ffffff"

                grid 2 1 xfill True:
                    textbutton "Музыка." style "log_button" text_style "settings_text" text_color "#ffffff" action Play("sound", "Miracle_in_the_form/gui/sound/test.ogg") xpos 0.1
                    bar value Preference("music volume") left_bar bar_full right_bar bar_null thumb "Miracle_in_the_form/gui/Settings/htumb1.png" hover_thumb "Miracle_in_the_form/gui/Settings/htumb1.png" xmaximum 1.35 ymaximum 36 xpos -0.55

                grid 2 1 xfill True:
                    textbutton "Звуки." style "log_button" text_style "settings_text" text_color "#ffffff" action Play("sound", "Miracle_in_the_form/gui/sound/test.ogg") xpos 0.1
                    bar value Preference("sound volume") left_bar bar_full right_bar bar_null thumb "Miracle_in_the_form/gui/Settings/htumb1.png" hover_thumb "Miracle_in_the_form/gui/Settings/htumb1.png" xmaximum 1.35 ymaximum 36 xpos -0.55

                grid 2 1 xfill True:
                    textbutton "Эмбиент." style "log_button" text_style "settings_text" text_color "#ffffff" action Play("sound", "Miracle_in_the_form/gui/sound/test.ogg") xpos 0.1
                    bar value Preference("voice volume") left_bar bar_full right_bar bar_null thumb "Miracle_in_the_form/gui/Settings/htumb1.png" hover_thumb "Miracle_in_the_form/gui/Settings/htumb1.png" xmaximum 1.35 ymaximum 36 xpos -0.55

                text "Скорость текста." style "settings_header" xalign 0.5 color "#ffffff"
                bar value Preference("text speed") left_bar bar_full right_bar bar_null thumb "Miracle_in_the_form/gui/Settings/htumb1.png" hover_thumb "Miracle_in_the_form/gui/Settings/htumb1.png" xalign 0.5 xmaximum 0.8 ymaximum 36

                text "Автопереход." style "settings_header" xalign 0.5 color "#ffffff"
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.afm_time != 0:
                            add "Miracle_in_the_form/gui/Settings/sh_body1.png" ypos 0.12
                        else:
                            null width 22
                        textbutton "Врубить!" style "log_button" text_style "settings_text" text_color "#ffffff" action Preference("auto-forward after click", "enable")

                    hbox xalign 0.5:
                        if _preferences.afm_time == 0:
                            add "Miracle_in_the_form/gui/Settings/sh_body1.png" ypos 0.12
                        else:
                            null width 22
                        textbutton "Вырубить!" style "log_button" text_style "settings_text" text_color "#ffffff" action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))

                text "Время автоперехода." style "settings_header" xalign 0.5 color "#ffffff"
                bar value Preference("auto-forward time") left_bar bar_full right_bar bar_null thumb "Miracle_in_the_form/gui/Settings/htumb1.png" hover_thumb "Miracle_in_the_form/gui/Settings/htumb1.png" xalign 0.5 xmaximum 0.8 ymaximum 36

                text "Размер шрифта." style "settings_header" xalign 0.5 color "#ffffff"
                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.font_size == "small":
                            add "Miracle_in_the_form/gui/Settings/sl_body1.png" ypos 0.12
                        else:
                            null width 22
                        textbutton "Нормальный." style "log_button" text_style "settings_text" text_color "#ffffff" action SetField(persistent, "font_size", "small")

                    hbox xalign 0.5:
                        if not persistent.font_size == "small":
                            add "Miracle_in_the_form/gui/Settings/sl_ody1.png" ypos 0.12
                        else:
                            null width 22
                        textbutton "Большой." style "log_button" text_style "settings_text" text_color "#ffffff" action SetField(persistent, "font_size", "large")

                null
                null

            bar value XScrollValue("preferences") left_bar "Miracle_in_the_form/gui/Settings/none.png" right_bar "Miracle_in_the_form/gui/Settings/none.png" thumb "Miracle_in_the_form/gui/Settings/none.png" hover_thumb "Miracle_in_the_form/gui/Settings/none.png"
            vbar value YScrollValue("preferences") bottom_bar "Miracle_in_the_form/gui/Settings/none.png" top_bar "Miracle_in_the_form/gui/Settings/none.png" thumb "Miracle_in_the_form/gui/Settings/un_body1.png" thumb_offset -12
