#========================================= ## (∆ Файл настройки модификации. ∆) ## =========================================#
    #AUTHOR: Автор модификации Максим Райс.

init python:

    #AUTHOR: Пишем название первого "label" и название мода.
        # *|На мобильном первый (label) "Mi", а на компьютере "inform".|*
        # *|Если при создании мода, первым пишется (init python:), то ставить знак { $ } перед mods не нужно.|*

    mods["inform"] = u"{font=Miracle_in_the_form/fonts/JetBrainsMono-Regular.ttf}{color=#008000}{size=35}∆ Чудо в форме. ∆{/size}{/color}{/font} | v. 5.22"

# init:

    # $ promise = "Miracle_in_the_form/music/a_promise_from_distant_days_v2.ogg" # Музыка в мобильном меню. На компьютере закомментировать.

init:

    # Переменные.

    $ mir_dv = 1
    $ mir_us = 1
    $ score_m = 1

    # Инструменты.

    $ config.developer = False # *| Включать (True) ли инструменты разработчика? Здесь нужно поставить (False) перед выпуском игры, чтобы игрок не смог мошенничать, используя эти инструменты. Перезагрузка без выхода из игры 'SHIFT + r' в английской раскладке.|*

# init:

    # transform mi_transform:
        # xcenter 0.5 ycenter 0.5

#===========================================================================================================================#


    #AUTHOR: Различные настройки, - эффектов, - переходов и смены сцен.

    $ slow = Dissolve (1.0)
    $ diss = Dissolve(0.3) # Своя настройка функции [Dissolve].
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff') # Своя настройка вспышки.
    define circle_in = ImageDissolve("Miracle_in_the_form/gui/additionally/im_diss_circle.png", 1.0, 8, reverse=True)
    define circle_out = ImageDissolve("Miracle_in_the_form/gui/additionally/im_diss_circle.png", 1.0, 8)
    define teleport = ImageDissolve("Miracle_in_the_form/gui/additionally/im_diss_teleport.png", 1.0, 0)

    image unblink_m: # Своя настройка (Моргания персонажа).
        contains:
            "anim blink_up1"
            xalign 0 yalign 0
            ease 1.0 pos (0,-1080) # На мобильном значение 720, на ПК 1080.
        contains:
            "anim blink_down1"
            xalign 0 yalign 0
            ease 1.0 pos (0,1080)

    image blink_m:
        contains:
            "anim blink_up1"
            pos (0,-1080)
            ease 1.0 xalign 0 yalign 0
        contains:
            "anim blink_down1"
            pos (0,1080)
            ease 1.0 xalign 0 yalign 0

    image blinking_m:
        contains:
            "anim blink_up1"
            pos (0,-1080)
            ease 1.0 xalign 0 yalign 0
        contains:
            "anim blink_down1"
            pos (0,1080)
            ease 1.0 xalign 0 yalign 0
        pause 0.5
        contains:
            "anim blink_up1"
            xalign 0 yalign 0
            ease 1.0 pos (0,-1080)
        contains:
            "anim blink_down1"
            xalign 0 yalign 0
            ease 1.0 pos (0,1080)

    #AUTHOR: Своя функция для громкости (ambience) снаружи и внутри, применять непостоянно, а по мере необходимости.
        # *|Функция написана не мной, а слегка изминённая взята из мода (Roadtoglory --> Путь к успеху).|*

    python:


        def inside(suneven):
            global inside_volume


            volume(inside_volume,'ambience')


        def outside():
            global outside_volume


            volume(outside_volume,'ambience')

    python: # *|Настройка громкости для вечера-ночи.|*
        inside_volume = 0.2
        outside_volume = 0.8


    python:


        def inside1(day):
            global inside1_volume


            volume(inside1_volume,'ambience')


        def outside1():
            global outside1_volume


            volume(outside1_volume,'ambience')

    python: # *|Настройка громкости для дня.|*
        inside1_volume = 0.1
        outside1_volume = 0.9

#===========================================================================================================================#


label inform:

    #AUTHOR: Запуск собственного меню в версии, для ПК.
        # *|На мобильном за комментировать, а на компьютере наоборот.|*

    call screen new_main_menu

    jump inform

#===========================================================================================================================#


# label Mi:

    #AUTHOR: Запуск собственного меню в версии, для мобильного.
        # *|На компьютере за комментировать, а на мобильном наоборот.|*

    # play music promise fadein 1

    # call screen menu_mi

    # screen menu_mi:

        # tag menu_mi
        # modal True

        # imagemap:

            # ground "Miracle_in_the_form/bg_img/ext_island_1night.jpg"
            # idle "Miracle_in_the_form/gui/Main_menu/mobile_menu/start_push_idle.png"
            # hover "Miracle_in_the_form/gui/Main_menu/mobile_menu/start_push_hover.png"
            ## hotspot(134, 479, 1085, 589) action (Hide("menu_mi"), Jump("Miracle")) # Это удалить, потом.
            # hotspot(134, 479, 1050, 530) action (Hide("menu_mi"), Jump("Miracle"))

#===========================================================================================================================#


## Добавление титров, персонажей, музыки и звуков, может не работать с помощью знака { $ }. По этому лучше добавлять с помощью { define }. ##

    #AUTHOR: Добавление титров. В конце дня будут выводиться титры, из соответствующего (my_credits).
        # *|Эту информацию можно и не выводить, это по желанию.|*

    define my_credits = "{font=Miracle_in_the_form/fonts/UbuntuMonoR.ttf}Спасибо, за внимание к моему моду.\n\nНе забудьте поставить Like, на странице мода.\n\nИ советуйте друзьям поиграть, в „Бесконечное лето“. НАШУ - ЛЮБИМУЮ - ИГРУ.{/font}"
    define my_credits1 = "{font=Miracle_in_the_form/fonts/UbuntuMonoR.ttf}Первый день прожит, идём дальше.{/font}"
    define my_credits2 = "{font=Miracle_in_the_form/fonts/UbuntuMonoR.ttf}Ура! Вы пережили и второй день, поздравляю.{/font}"
    define my_credits3 = "{font=Miracle_in_the_form/fonts/UbuntuMonoR.ttf}Вы осилили и третий день. XD Так держать!{/font}"
    define my_credits4 = "{font=Miracle_in_the_form/fonts/UbuntuMonoR.ttf}The end?..{/font}"
    define my_credits5 = "{font=Miracle_in_the_form/fonts/UbuntuMonoR.ttf}В моде были использованы материалы, как из оригинальной „БЛ“ так и из других источников.{/font}"
    define my_credits6 = "{font=Miracle_in_the_form/fonts/UbuntuMonoR.ttf}Алиса: Ты, да, ты - который сейчас это читает! Я приду к тебе ночью и отшлёпаю! \n\nАвтор: Очень злая Алиса отпинала Семёна и тебя может тоже отпинать. \n\nМожет нужно было сделать другой выбор?{/font}"

#===========================================================================================================================#


    #AUTHOR: Добавление (своих) персонажей.
        # *|Новым персонажам можно присвоить свои переменные, например (testpers), но не обязательно писать (testpers), или (testpers1, testpers2, и т.д.), можно написать любое другое имя, например (new_person). Кроме зарезервированных имён.|*
        # *|Так же новым персонажам, можно настроить свои цветовые стили, имени и текста. Для этого нужны, коды цветовых схем.|*
        # *|Коды цветовых схем, есть в папке (dev_files -> color_theme).|*

    define alx = Character(u"Алекс", color="#59d80c", what_color="E2C778", font="Miracle_in_the_form/fonts/anime.ttf")
    define sy = Character(u"Злой незнакомец", color="#696969", what_color="#2F4F4F")
    define ds = Character(u"Дядя Саня", color="E2C778", what_color="E2C778")
    define nio = Character(u"Пионер…", color="E2C778", what_color="E2C778")
    define pe = Character(u"Пионерка А", color="696969", what_color="E2C778")
    define an = Character(u"Аня", color="#ec8312", what_color="#f1d076", font="Miracle_in_the_form/fonts/anime.ttf")
    define anp = Character(u"Пионерка Б", color="#FFFF00", what_color="E2C778") # Пионерка „Б“ до того, как назвали её имя, потом она становится Аней.
    define so = Character(u"Соня", color="#ec8312", what_color="#f1d076", font="Miracle_in_the_form/fonts/anime.ttf")
    define nek = Character(u"Ник", color="E2C778", what_color="E2C778")
    define nekp = Character(u"Пионер А", color="E2C778", what_color="E2C778")
    define mg = Character(u"Продавщица", color="E2C778", what_color="E2C778")

#===========================================================================================================================#


    #AUTHOR: Добавление bg, cg и anim.
        # *|В папке мода, делается папка для bg, например (bg_img) из неё они будут, подгружаться в игру.|*
        # *|Так же делается папка для cg, например (cg_img) из неё они будут, подгружаться в игру.|*
        # *|Так же делается папка для anim, например (anim_pic).|*

    ## __BG__ ##

    image bg black1 = "Miracle_in_the_form/bg_img/black1.jpg" # Моя работа.
    image bg monitor = "Miracle_in_the_form/bg_img/monitor.jpg" # Моя переделка.
    image bg monitor1 = "Miracle_in_the_form/bg_img/monitor1.jpg" # Моя переделка.
    image bg new_map = "Miracle_in_the_form/gui/maps/new_map.jpg" # Моя переделка.
    image bg new_active_map = "Miracle_in_the_form/gui/maps/new_active_map.jpg" # Моя переделка.
    image bg int_mine_backdoor = "Miracle_in_the_form/bg_img/int_mine_backdoor.jpg"
    image bg int_semen_kitchen = "Miracle_in_the_form/bg_img/int_semen_kitchen.jpg"
    image bg int_bathhouse_night1 = "Miracle_in_the_form/bg_img/int_bathhouse_night1.jpg"
    image bg int_bathhouse_night = "Miracle_in_the_form/bg_img/int_bathhouse_night.jpg"
    image bg int_office_day = "Miracle_in_the_form/bg_img/int_office_day.jpg"
    image bg int_stairwell = "Miracle_in_the_form/bg_img/int_stairwell.jpg"
    image bg int_semen_room_1 = "Miracle_in_the_form/bg_img/int_semen_room_1.jpg" # Моя переделка.
    image bg int_semen_room_2 = "Miracle_in_the_form/bg_img/int_semen_room_2.jpg" # Моя переделка.
    image bg int_semen_room_3 = "Miracle_in_the_form/bg_img/int_semen_room_3.jpg" # Моя переделка.
    image bg int_semen_room_4 = "Miracle_in_the_form/bg_img/int_semen_room_4.jpg" # Моя переделка.
    image bg int_liaz_bus_night = "Miracle_in_the_form/bg_img/int_liaz_bus_night.jpg"
    image bg int_bus_window_day = "Miracle_in_the_form/bg_img/int_bus_window_day.jpg" # Моя переделка.
    image bg int_aidpost_sunset = "Miracle_in_the_form/bg_img/int_aidpost_sunset.jpg"
    image bg int_shop_night = "Miracle_in_the_form/bg_img/int_shop_night.jpg"
    image bg int_catacombs_entrance_light = "Miracle_in_the_form/bg_img/int_catacombs_entrance_light.jpg"
    image bg int_catacombs_door_no_light = "Miracle_in_the_form/bg_img/int_catacombs_door_no_light.jpg"
    image bg int_mine_halt_dynamite = "Miracle_in_the_form/bg_img/int_mine_halt_dynamite.jpg" # Моя переделка.
    image bg int_musclub_day1 = "Miracle_in_the_form/bg_img/int_musclub_day1.jpg" # Моя переделка.
    image bg int_musclub_sunset = "Miracle_in_the_form/bg_img/int_musclub_sunset.jpg"
    image bg int_clubs_night_light = "Miracle_in_the_form/bg_img/int_clubs_night_light.jpg"
    image bg int_admin_day = "Miracle_in_the_form/bg_img/int_admin_day.jpg"
    image bg int_art_clas_day = "Miracle_in_the_form/bg_img/int_art_clas_day.jpg"
    image bg ext_musclub_close_day = "Miracle_in_the_form/bg_img/ext_musclub_close_day.jpg"
    image bg ext_new_year = "Miracle_in_the_form/bg_img/ext_new_year.jpg"
    image bg ext_storage_day = "Miracle_in_the_form/bg_img/ext_storage_day.jpg"
    image bg ext_storage_night = "Miracle_in_the_form/bg_img/ext_storage_night.jpg"
    image bg ext_night_camp_entrance = "Miracle_in_the_form/bg_img/ext_night_camp_entrance.jpg" # Моя переделка.
    image bg ext_night_camp_entrance_1 = "Miracle_in_the_form/bg_img/ext_night_camp_entrance_1.jpg" # Моя переделка.
    image bg ext_aidpost_sunset = "Miracle_in_the_form/bg_img/ext_aidpost_sunset.jpg"
    image bg ext_clubs_sunset = "Miracle_in_the_form/bg_img/ext_clubs_sunset.jpg"
    image bg ext_washstand_sunset = "Miracle_in_the_form/bg_img/ext_washstand_sunset.jpg"
    image bg ext_island_revers_day = "Miracle_in_the_form/bg_img/ext_island_revers_day.jpg"
    image bg ext_island_1night = "Miracle_in_the_form/bg_img/ext_island_1night.jpg"
    image bg ext_glade_day = "Miracle_in_the_form/bg_img/ext_glade_day.jpg"
    image bg ext_winter_park_night_light = "Miracle_in_the_form/bg_img/ext_winter_park_night_light.jpg"
    image bg ext_square_day_blur = "Miracle_in_the_form/bg_img/ext_square_day_blur.jpg"
    image bg ext_square_color_day = "Miracle_in_the_form/bg_img/ext_square_color_day.jpg" # Моя переделка.
    image bg ext_square_color_day1 = "Miracle_in_the_form/bg_img/ext_square_color_day1.jpg" # Моя переделка.
    image bg ext_square_day_flag = "Miracle_in_the_form/bg_img/ext_square_day_flag.jpg" # Моя переделка.
    image bg ext_square_day_flag1 = "Miracle_in_the_form/bg_img/ext_square_day_flag1.jpg" # Моя переделка.
    image bg ext_bus_close_day = "Miracle_in_the_form/bg_img/ext_bus_close_day.jpg" # Моя переделка.
    image bg ext_bus_open_day = "Miracle_in_the_form/bg_img/ext_bus_open_day.jpg" # Моя переделка.
    image bg ext_bus_close_night = "Miracle_in_the_form/bg_img/ext_bus_close_night.jpg" # Моя переделка.
    image bg ext_bus_open_night = "Miracle_in_the_form/bg_img/ext_bus_open_night.jpg" # Моя переделка.
    image bg ext_square_night1 = "Miracle_in_the_form/bg_img/ext_square_night1.jpg" # Моя переделка.
    image bg ext_square_night_party1 = "Miracle_in_the_form/bg_img/ext_square_night_party1.jpg" # Моя переделка.
    image bg ext_square_night_party_2 = "Miracle_in_the_form/bg_img/ext_square_night_party_2.jpg" # Моя переделка.
    image bg ext_square_night_party_00 = "Miracle_in_the_form/bg_img/ext_square_night_party_00.jpg" # Моя переделка.
    image bg ext_square_night_party_01 = "Miracle_in_the_form/bg_img/ext_square_night_party_01.jpg" # Моя переделка.
    image bg ext_square_night_party_02 = "Miracle_in_the_form/bg_img/ext_square_night_party_02.jpg" # Моя переделка.
    image bg ext_square_night_party_03 = "Miracle_in_the_form/bg_img/ext_square_night_party_03.jpg" # Моя переделка.
    image bg ext_houses_night = "Miracle_in_the_form/bg_img/ext_houses_night.jpg"
    image bg ext_avto_sunset = "Miracle_in_the_form/bg_img/ext_aidpost_sunset.jpg"
    image bg ext_new_camp_entrance_day = "Miracle_in_the_form/bg_img/ext_new_camp_entrance_day.jpg" # Моя переделка.
    image bg ext_power_line = "Miracle_in_the_form/bg_img/ext_power_line.jpg" # Моя переделка.
    image bg ext_old_building_day = "Miracle_in_the_form/bg_img/ext_old_building_day.jpg"
    image bg ext_beach1_day = "Miracle_in_the_form/bg_img/ext_beach1_day.jpg" # Моя переделка.
    image bg int_dining_hall_evening = "Miracle_in_the_form/bg_img/int_dining_hall_evening.jpg"
    image bg ext_beach1_sunset = "Miracle_in_the_form/bg_img/ext_beach1_sunset.jpg" # Моя переделка.
    image bg ext_beach_night_moon = "Miracle_in_the_form/bg_img/ext_beach_night_moon.jpg" # Моя переделка.
    image bg ext_beach_night_moon1 = "Miracle_in_the_form/bg_img/ext_beach_night_moon1.jpg" # Моя переделка.
    image bg ext_house_of_dv_night1 = "Miracle_in_the_form/bg_img/ext_house_of_dv_night1.jpg" # Моя переделка.
    image bg ext_house_of_dv_day1 = "Miracle_in_the_form/bg_img/ext_house_of_dv_day1.jpg" # Моя переделка.
    image bg ext_house_of_dv_night3 = "Miracle_in_the_form/bg_img/ext_house_of_dv_night3.jpg"
    image bg ext_house_of_dv_night2 = "Miracle_in_the_form/bg_img/ext_house_of_dv_night2.jpg"
    image bg ext_forest_day = "Miracle_in_the_form/bg_img/ext_forest_day.jpg"
    image bg ext_forest_day1 = "Miracle_in_the_form/bg_img/ext_forest_day1.jpg"
    image bg ext_forest_day2 = "Miracle_in_the_form/bg_img/ext_forest_day2.jpg"
    image bg ext_forest_night_rain = "Miracle_in_the_form/bg_img/ext_forest_night_rain.jpg"
    image bg ext_forest_vecher = "Miracle_in_the_form/bg_img/ext_forest_vecher.jpg"
    image bg ext_forest_vecher_rain = "Miracle_in_the_form/bg_img/ext_forest_vecher_rain.jpg"
    image bg ext_house1_of_mt_day = "Miracle_in_the_form/bg_img/ext_house1_of_mt_day.jpg" # Моя переделка.
    image bg ext_house1_of_mt_night = "Miracle_in_the_form/bg_img/ext_house1_of_mt_night.jpg" # Моя переделка.
    image bg ext_house1_of_mt_sunset = "Miracle_in_the_form/bg_img/ext_house1_of_mt_sunset.jpg" # Моя переделка.
    image bg ext_house2_of_mt_night = "Miracle_in_the_form/bg_img/ext_house2_of_mt_night.jpg" # Моя переделка.
    image bg ext_library1_day = "Miracle_in_the_form/bg_img/ext_library1_day.jpg" # Моя переделка.
    image bg ext_library1_night = "Miracle_in_the_form/bg_img/ext_library1_night.jpg" # Моя переделка.
    image bg ext_house_of_sl_day1 = "Miracle_in_the_form/bg_img/ext_house_of_sl_day1.jpg" # Моя переделка.
    image bg ext_house_of_un_day1 = "Miracle_in_the_form/bg_img/ext_house_of_un_day1.jpg" # Моя переделка.
    image bg monitor1_chat = "Miracle_in_the_form/bg_img/monitor1_chat.jpg" # Моя переделка.
    image bg monitor2_chat = "Miracle_in_the_form/bg_img/monitor2_chat.jpg" # Моя переделка.
    image bg monitor3_chat = "Miracle_in_the_form/bg_img/monitor3_chat.jpg" # Моя переделка.
    image bg monitor4_chat = "Miracle_in_the_form/bg_img/monitor4_chat.jpg" # Моя переделка.
    image bg int_clubs_pantry = "Miracle_in_the_form/bg_img/int_clubs_pantry.jpg"

    ## __CG__ ##

    image cg all_final = "Miracle_in_the_form/cg_img/all_final.jpg"
    image cg d2_mz_library = "Miracle_in_the_form/cg_img/d2_mz_library.jpg" # Моя переделка.
    image cg d2_mz1_library = "Miracle_in_the_form/cg_img/d2_mz1_library.jpg" # Моя переделка.
    image cg d2_mz2_library = "Miracle_in_the_form/cg_img/d2_mz2_library.jpg" # Моя переделка.
    image cg d3_dining_hall_day = "Miracle_in_the_form/cg_img/d3_dining_hall_day.jpg" # Моя переделка.
    image cg d3_dining_hall_day1 = "Miracle_in_the_form/cg_img/d3_dining_hall_day1.jpg" # Моя переделка.
    image cg d3_dv_me_dance = "Miracle_in_the_form/cg_img/d3_dv_me_dance.jpg"
    image cg d3_dv_me_sliep = "Miracle_in_the_form/cg_img/d3_dv_me_sliep.jpg"
    image cg d3_dv_night = "Miracle_in_the_form/cg_img/d3_dv_night.jpg"
    image cg d4_dining_hall_sunset_rain = "Miracle_in_the_form/cg_img/d4_dining_hall_sunset_rain.jpg"
    image cg d4_dv_me = "Miracle_in_the_form/cg_img/d4_dv_me.jpg"
    image cg dv_me_boat = "Miracle_in_the_form/cg_img/dv_me_boat.jpg"
    image cg min_later = "Miracle_in_the_form/cg_img/min_later.jpg"
    image cg mt_clubs_sunset = "Miracle_in_the_form/cg_img/mt_clubs_sunset.jpg" # Моя переделка.
    image cg the_end_dv_good = "Miracle_in_the_form/cg_img/the_end_dv_good.jpg"
    image cg d2_square_day1 = "Miracle_in_the_form/cg_img/d2_square_day1.jpg" # Моя переделка.
    image cg d2_square_day2 = "Miracle_in_the_form/cg_img/d2_square_day2.jpg" # Моя переделка.

    ## __ANIM__ ##

    image anim blink_down1 = "Miracle_in_the_form/anim_pic/blink_down1.png"
    image anim blink_up1 = "Miracle_in_the_form/anim_pic/blink_up1.png"

#===========================================================================================================================#


    #AUTHOR: Добавление сцен, которые могут быть удалены из игры.
        # *|Сцены удалённые из мобильной версии.|*

    ## __CGS__ ##

    image cgs d2_miku_piano = "Miracle_in_the_form/cgs_img/d2_miku_piano.jpg"
    image cgs d2_miku_piano2 = "Miracle_in_the_form/cgs_img/d2_miku_piano2.jpg"
    image cgs d2_miku_piano3 = "Miracle_in_the_form/cgs_img/d2_miku_piano3.jpg" # Моя переделка.
    image cgs d2_mt_undressed_2 = "Miracle_in_the_form/cgs_img/d2_mt_undressed_2.jpg"
    image cgs d2_mt_undressed = "Miracle_in_the_form/cgs_img/d2_mt_undressed.jpg"
    image cgs d3_dv_banya = "Miracle_in_the_form/cgs_img/d3_dv_banya.jpg"
    image cgs d3_el_wash = "Miracle_in_the_form/cgs_img/d4_el_wash.jpg" # Моя переделка.
    image cgs d4_un_glade = "Miracle_in_the_form/cg_img/d3_un_glade.jpg" # Моя переделка.
    image cgs d2_cs = "Miracle_in_the_form/cgs_img/d2_cs.jpg"
    image cgs d2_cs1 = "Miracle_in_the_form/cgs_img/d2_cs1.jpg"
    image cgs dv_final = "Miracle_in_the_form/cgs_img/dv_final.jpg"
    image cgs monitor_02 = "Miracle_in_the_form/cgs_img/monitor_02.jpg" # Моя переделка.
    image cgs d4_slavya_undressed = "Miracle_in_the_form/cgs_img/d4_slavya_undressed.jpg"

#===========================================================================================================================#


    #AUTHOR: Добавление спрайтов - персонажей.
        # *|В папке мода, делается папка, например (sprites) из неё они будут, подгружаться в игру. Для всех спрайтов лучше делать отдельные папки по именам. Если спрайт один, то отдельную папку можно не делать.|*

    image mt sad2 = "Miracle_in_the_form/sprites/normal/mt/mt sad2.png" # Моя переделка.

    image cs new body = "Miracle_in_the_form/sprites/normal/cs/cs new body.png"
    image cs new body smile = "Miracle_in_the_form/sprites/normal/cs/cs new body smile.png"

    image dv heart figure = "Miracle_in_the_form/sprites/normal/dv/dv heart figure.png"
    image dv lisenok = "Miracle_in_the_form/sprites/normal/dv/dv lisenok.png" # Моя переделка.
    image dv lisenok1 = "Miracle_in_the_form/sprites/normal/dv/dv lisenok1.png" # Моя переделка.
    image dv lisenok2 = "Miracle_in_the_form/sprites/normal/dv/dv lisenok2.png" # Моя переделка.
    image dv bra1 = "Miracle_in_the_form/sprites/normal/dv/dv bra1.png"
    image dv bra2 = "Miracle_in_the_form/sprites/normal/dv/dv bra2.png"
    image dv bra3 = "Miracle_in_the_form/sprites/normal/dv/dv bra3.png"
    image dv bra4 = "Miracle_in_the_form/sprites/normal/dv/dv bra4.png"
    image dv behind1 = "Miracle_in_the_form/sprites/normal/dv/dv behind1.png" # Моя переделка.

    image us heart figure = "Miracle_in_the_form/sprites/normal/us/us heart figure.png"

#===========================================================================================================================#


    #AUTHOR: Другой вариант добавления спрайтов.
        # *|Сборка спрайтов, по частям. Из именной папки, в данном случае папка (pe). При отображении писать (show pe normal body).|*
        # *|В мобильной версии размер в (im.Composite) не (900х1080), а (600х720) пикселей.|*

    ## Пионерка А. ##

    image pe dontlike body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_dontlike.png"))

    image pe grin body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_grin.png"))

    image pe guilty body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_guilty.png"))

    image pe normal body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_normal.png"))

    image pe serious body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_serious.png"))

    image pe smile body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_smile.png"))

    image pe sorrow body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_sorrow.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_sorrow.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_1_sorrow.png"))

    image pe dull body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_2_dull.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_2_dull.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_2_dull.png"))

    image pe grin2 body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_2_grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_2_grin2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_2_grin2.png"))

    image pe angry body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_3_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_3_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_3_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_3_angry.png"))

    image pe sad body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_3_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_3_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_3_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/pe/pe_3_sad.png"))

    ## Племянница Жени, Аня. ##

    image an normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/an/an normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/an/an normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/an/an normal.png"))

    image an dontlike = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/an/an dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/an/an dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/an/an dontlike.png"))

    image an smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/an/an smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/an/an smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/an/an smile.png"))

    image an surprise = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/an/an surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/an/an surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/an/an surprise.png"))

    ## Ник. ##
        # *|При отображении писать (show nek normal body).|*

    image nek angry body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_angry.png"))

    image nek normal body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_normal.png"))

    image nek happy body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_happy.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_happy.png"))

    image nek smile body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_smile.png"))

    image nek laugh body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_1_laugh.png"))

    image nek serious2 body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_serious.png"))

    image nek surprise body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_2_surprise.png"))

    image nek angry3 body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_3_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_3_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_3_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_3_serious.png"))

    image nek serious3 body = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_3_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_3_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_3_body.png", (0, 0), "Miracle_in_the_form/sprites/normal/nek/nek_3_serious.png"))

    ## Дядя Саня. ##
        # *|Спрайт дяди Сани был создан специально для данного мода, художника можно найти по ссылке [@deadybetz] в телеграмм.|*
        # *|Использование данного спрайта в других проектах с обязательным указанием (мода - источника и автора спрайта).|*

    image ds smile hand = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/ds/ds smile hand.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/ds/ds smile hand.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/ds/ds smile hand.png"))

    image ds smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/ds/ds smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/ds/ds smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/ds/ds smile.png"))

    ## Алексей - Алекс. ##
        # *|Данный спрайт, моя переделка.|*

    image alx normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/alx/alx normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/alx/alx normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/alx/alx normal.png"))

    image alx smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/alx/alx smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/alx/alx smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/alx/alx smile.png"))

    image alx serious = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/alx/alx serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/alx/alx serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/alx/alx serious.png"))

    image alx sad = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/alx/alx sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/alx/alx sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/alx/alx sad.png"))

    ## Соня. ##

    image so head = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so head.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so head.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so head.png"))

    image so normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so normal.png"))

    image so sad = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so sad.png"))

    image so sad1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so sad1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so sad1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so sad1.png"))

    image so smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so smile.png"))

    image so smile1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so smile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so smile1.png"))

    image so surprise = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so surprise.png"))

    image so surprise1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so surprise1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so surprise1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so surprise1.png"))

    image so angry = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so angry.png"))

    image so angry1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so angry1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so angry1.png"))

    image so blush = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so blush.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so blush.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so blush.png"))

    image so blush1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so blush1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so blush1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so blush1.png"))

    image so laugh = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so laugh.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so laugh.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so laugh.png"))

    image so laugh1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so laugh1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so laugh1.png"))

    image so kiss = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so kiss.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so kiss.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so/so kiss.png"))

    image so tn normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_tn/so tn normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_tn/so tn normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_tn/so tn normal.png"))

    image so tn normal1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_tn/so tn normal1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_tn/so tn normal1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_tn/so tn normal1.png"))

    image so tn surprise = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_tn/so tn surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_tn/so tn surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_tn/so tn surprise.png"))

    image so tn smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_tn/so tn smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_tn/so tn smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_tn/so tn smile.png"))

    image so n normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_n/so n normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_n/so n normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_n/so n normal.png"))

    image so n kiss = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_n/so n kiss.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_n/so n kiss.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/so_n/so n kiss.png"))

    ## Ещё пионер. ##

    image nio normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio normal.png"))

    image nio angry = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio angry.png"))

    image nio smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio smile.png"))

    image nio surprise = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio surprise.png"))

    image nio think = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio think.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio think.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio think.png"))

    image nio angry1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio angry1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio angry1.png"))

    image nio smile1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio smile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio smile1.png"))

    image nio smile2 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio smile2.png"))

    image nio surprise1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio surprise1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio surprise1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/nio/nio surprise1.png"))

    ## Алиса. ##

    image dv body n = ConditionSwitch(
        "persistent.sprite_time == 'sunset' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/dv/dv body n.png", (0, 0), "Miracle_in_the_form/sprites/normal/dv/dv normal n.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night' ", im.MatrixColor(im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/dv/dv body n.png", (0, 0), "Miracle_in_the_form/sprites/normal/dv/dv normal n.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "Miracle_in_the_form/sprites/normal/dv/dv body n.png", (0, 0), "Miracle_in_the_form/sprites/normal/dv/dv normal n.png"))

#===========================================================================================================================#


    #AUTHOR: Добавление музыки и звуков.
        # *|В папке мода, делается папка, например (music) из неё они будут, подгружаться в игру.|*
        # *|Так же в папке мода делаем папку, например (sfx) из неё они будут, подгружаться в игру.|*

    define 410_short = "Miracle_in_the_form/music/410_short.mp3" # Моя обрезка.
    define fear = "Miracle_in_the_form/music/fear.mp3"
    define sfx_Tictak = "Miracle_in_the_form/sfx/Tictak.mp3"
    define moment_of_decision_short = "Miracle_in_the_form/music/moment_of_decision_short.mp3" # Моя обрезка.
    define sfx_steps_in_snow = "Miracle_in_the_form/sfx/steps_in_snow.mp3" # Взял с сайта (freesound.org).
    define sfx_punch = "Miracle_in_the_form/sfx/punch.ogg"
    define sfx_alarm_clock_short = "Miracle_in_the_form/sfx/alarm_clock_short.ogg"
    define reflection_short = "Miracle_in_the_form/music/reflection_short.mp3" # Моя обрезка.
    define sfx_bomb_explosion = "Miracle_in_the_form/sfx/bomb_explosion.ogg"
    define sfx_far_steps_fast = "Miracle_in_the_form/sfx/far_steps_fast.ogg"
    define sfx_rain_loop = "Miracle_in_the_form/sfx/rain_loop.ogg"
    define sfx_jingle_normal = "Miracle_in_the_form/sfx/jingle_normal.ogg"
    define sfx_jingle1 = "Miracle_in_the_form/sfx/jingle1.ogg"
    define sfx_jingle_speaker2 = "Miracle_in_the_form/sfx/jingle_speaker2.ogg"
    define sfx_sex1 = "Miracle_in_the_form/gui/sound/sex1.mp3"
    define sfx_sex2 = "Miracle_in_the_form/gui/sound/sex2.mp3"
    define sfx_orgasm = "Miracle_in_the_form/gui/sound/orgasm.mp3"
    define sfx_Purr = "Miracle_in_the_form/sfx/Purr.ogg"

#===========================================================================================================================#


    #AUTHOR: Создание звукового канала.
        # *|Дополнительный канал создать не сложно, главное правильно указать, что за звук (ambience или sfx) и зациклен он (True) или нет (False).|*

    $ renpy.music.register_channel("sound_loop2", "sfx", True)
    $ renpy.music.register_channel("sound_loop3", "sfx", True)
    $ renpy.music.register_channel("sound2", "sfx", False)
    $ renpy.music.register_channel("sound3", "sfx", False)

#===========================================================================================================================#


    #AUTHOR: Добавление видео.
        # *|В папке мода, делается папка, например (movie, video и т.д.) из неё они будут, подгружаться в игру.|*
        # *|Добавление видео, по желанию. Пример того, как это делается; $ renpy.movie_cutscene("Miracle_in_the_form/resources/movie/kryto.ogv"). Ваше видео должно быть в формате ogv или webm, mp4 не подходит.|*
