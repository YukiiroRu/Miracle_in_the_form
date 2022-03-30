# Png, для моргания персонажа.
При желании можно настроить самостоятельно, как персонаж будет моргать.
Можно настроить медленное закрытие глаз с помощью команды (slow) или сделать быстрое моргание изменив время.

image unblink:
    contains:
        "anim blink_up"
        xalign 0 yalign 0
          ease 1.0 pos (0,-1080)
        contains:
            "anim blink_down"
            xalign 0 yalign 0
            ease 1.0 pos (0,1080)
