label Miracle_day4:

    $ backdrop = "un"
    $ new_chapter(4, u"Чудо в форме. День 4.")
    $ prolog_time()

    window show
    mt "Семён! {w}Семён! Вставай!"
    window hide

    show blinking_m

    play ambience ambience_camp_center_day fadein 2

    $ inside1(True)

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day
    with pixellate

    # play music music_list[""] fadein 3

    window show
    show mt normal pioneer at center with dissolve
    me "А, что?.."
    me "Да встаю я, встаю."
    "Я присел на кровати и сразу почувствовал, что сильно болит голова."
    show mt shocked pioneer at center with dspr
    mt "Что с тобой Семён?"
    me "Да у меня голова болит. У вас случайно нет анальгина?"
    mt "Надо посмотреть в аптечке, на сколько я помню были."
    hide mt
    with diss
    "…"
    "Вожатая какое-то время суетилась возле тумбочки, громыхая её содержимым."
    show mt normal pioneer at center with diss
    mt "Нет, видимо кончились. Тебе нужно зайти в медпункт."
    show mt shocked pioneer at center with dspr
    mt "С тобой, что-то ещё?"
    me "Что, что-то ещё? Я вас не понимаю."
    mt "Ты во сне стонал и дёргался, как будто у тебя был припадок."
    me "Я не чего не помню, честно."
    "Что мне снилось или нет? Я этого не помнил. Было лишь ощющение опустошонности и усталости. Как будто меня выжали, как лимон."
    show mt normal pioneer at center with dspr
    mt "Что ж, если вспомнишь поговорим, а пока иди в медпункт."
    mt "А уж потом пойдёшь на завтрак. {w}Да и после завтрака зайди в главный корпус."
    me "А зачем?"
    ht "Интересно, почему зайти в админисрацию именно сегодня, а не допустим в первый же день?"
    mt "Не чего серьёзного, там что-то с твоим личным делом."
    me "Личное дело?"
    mt "Да ты не волнуйся, это так формальность."
    hide mt
    with dissolve

    play sound sfx_close_door_campus_1

    "И вожатая вышла из домика."
    "Я же остался один с моими мыслями и болью, которую хотелось унять."
    me "Надо пойти умыться, может легче станет."
    ht "Ох блин башка трещит…"
    window hide

    # play ambience ambience_camp_center_day fadein 2

    $ day_time()

    $ outside1()

    scene bg ext_house_of_mt_day
    with dissolve

    window show
    "Я взял умывальные принадлежности и пошёл умываться. Долго умываться я был не в силах, голова раскалывалась."

    scene bg ext_washstand_day
    with dspr

    play sound sfx_open_water_sink

    $ renpy.pause(1)

    play sound_loop sfx_water_sink_stream

    "Боль была не постоянная, она пульсировала, было то хуже, то лучше."

    stop sound_loop

    play sound sfx_close_water_sink

    window hide

    play sound sfx_open_dooor_campus_1

    $ prolog_time()

    $ inside1(True)

    scene bg int_house_of_mt_day
    with diss

    window show
    "Я зашёл в домик чтобы положить умывальные принадлежности."
    "Мне показалось, что в домике кто-то побывал, но это была не наша вожатая. Ну и конечно же, не кто-то из нашего отряда."
    "Это был чужак и он явно что-то искал. Вот только, что, было не понятно…"
    "Из-за не стихающей боли, мне было не до выяснения обстоятельств дела и я поспешил в медпункт."
    window hide

    $ day_time()

    $ outside1()

    scene bg ext_aidpost_day
    with fade

    window show
    "Подойдя ближе к медпункту, я остановился."
    "В ближних кустах я заметил мелькнувший уже знакомый мне кошачий хвост."
    th "О Юля, средь бело дня? Куда это она?"
    th "Чёртова боль…"
    window hide

    stop ambience fadeout 2

    play sound sfx_open_door_1

    $ prolog_time()

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day
    with dissolve

    play ambience ambience_medstation_inside_day fadein 3

    window show
    show cs normal at center with dissolve
    cs "Здравствуй Семён. Что-то случилось?"
    me "Здравствуйте Виола, да голова болит. У вас не найдётся анальгина?"
    cs "Конечно. Присядь."
    hide cs
    with dspr
    "Я сел на кушетку в ожидании спасительного лекарства."
    "Виола полезла в тумбочку с лекарствами, их запах меня уже не сильно донимал."
    show cs normal at center with dspr
    cs "Вот держи."
    "Медичка протянула мне таблетку и стакан с водой. Закинув таблетку в рот, я сделал жадный глоток воды и стал ждать."
    "Виола же тем временем была занята какой-то писаниной сидя за своим столом."
    hide cs
    with dspr
    "Прошло несколько минут и боль стала утихать, принося чувство облегчения, но это было лиш облегчение телесное, а в душе всё оставалось также."
    show cs normal at center with dspr
    cs "Как себя чувствуешь Семён?"
    "Её взгляд слегка холодный был взглядом сурового медика, который чувствует себя удовлетворительно лишь тогда, когда его работа даёт нужные ему плоды."
    me "Да вроде хорошо."
    cs "Ты уверен?"
    me "Да, а что? Что-то не так?"
    "Она как-то испытующе посмотрела на меня."
    cs "У меня есть разговор к тебе. Серьёзный."
    me "А можно отложить его, на чуть позже?"
    cs "Прости но нет, это важно и не терпит отлогательства."
    me "Тогда ладно. И о чём разговор?"
    "По её виду было понятно, что то, о чём она хочет говорить и в самом деле серьёзно."
    cs "Я хочу поговорить с тобой, о Юле."
    me "А что Юля? Хотя понимаю, она проговорилась?"
    me "Хорошо давайте поговорим, хоть мне и не легко это именно сейчас."
    cs "Ты с ней разговаривал и даже купался…"
    "Разговор "
    window hide





















    stop music fadeout 3

    scene bg black
    with fade3

    show credits my_credits4:
        xalign 0.5
        ypos 1.3
        linear 52.0 ypos -4.0

    $ renpy.pause(20, hard=True)

    return

    # jump Miracle_day5

# день, число/месяц/2022., время PM/AM., Закончен.
