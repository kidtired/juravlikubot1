import random

anekdot = [
        'Чтобы хоть как—то отвлечь внимание от дырки в носке, '
        'мальчик Петя ударил именинницу табуреткой.',

        '— А по—нормальному ты умеешь говорить?\n'
        '— Ответ, к сожалению, не да.',

        'Однажды я спросил маму: “Сколько будет 2х2?”.\n'
        '“Много будешь знать, скоро состаришься”, — ответила она.\n'
        '“Четыре”, — сказал дедушка и заплакал.',

        '— Вы греховны, дети?\n'
        '— Да, патриарх!\n'
        '— Я не слышу!\n'
        '— Так точно, патриарх!\n'
        '— Оооооооооооооооо! Ну тогда скидываемся по 600 рублей на очищение.',

        '— Вы готовы дети?\n'
        '— Да, капитан!\n'
        '— Я не слыыышуууу!\n'
        '— ТАК ТОЧНО, капитан!\n'
        '— Кто проживает на дне океана?\n'
        '— Экономика нашей великой страны.\n'
        '— Ооооооооооо…',

        '— Пап, что такое отсутствие логики?\n'
        '— Глобус тебе в зад. — Ну пааап? — Борщ.',

        '— А Саша выйдет?\n'
        '— Саша умер…\n'
        '— А скиньте мяч!',

        '4 февраля в Польше - день больных эпилепсией. Что-то в этом есть…',

        'Бегающие за машинами собаки - это души умерших гаишников.',

        'Заходит тёмный мужчина , в чёрном капюшоне , с попугаем на плече в Бар.\n'
        'Бармен спрашивает: Где ты его купил? В Африке отвечает попугай!',

        'Новинка! Надувная кукла Вуду! Теперь вы можете воткнуть в своего врага не только иголку.',

        '— Эти оборотни прожили вместе 25 лет.\n'
        '— Что же их убило?\n'
        '— Серебряная свадьба.',

        '— От чего умер Ваш супруг?\n'
        '— Чистил ружье и случайно застрелился.\n'
        '— А откуда столько синяков?\n'
        '— Не хотел чистить.',

        '— Почему в Африке так много болезней?\n'
        '— Потому что таблетки нужно запивать водой.',

        'Курить по 3 пачки в день — это трудный путь, но разве нам нужны легкие?',

        'Среди детей-антипрививочников самое популярное имя — Любовь, потому что любовь живет три года.',

        'У долгожителя так долго пролетала перед глазами его жизнь, что он прожил еще три года.',

        'Пьяный мужик приходит домой и встречается на пороге с маленькой смертью.\n'
        'Он падает на колени и начинает долго и отчаянно просить пощадить его.\n'
        'Смерть отвечает:\n'
        '— Отъе6ись, я за хомяком.',

        'Мое финансовое положение:\n'
        '— Тараканы в доме есть?\n'
        '— Нет, их пауки съели.\n'
        '— У Вас пауки есть?\n'
        '— Нет, их крысы съели.\n'
        '— У Вас крысы есть?!\n'
        '— Нет, их Гена Афанасьев съел.\n'
        '— А кто это?\n'
        '— Забыл представиться.',

        'ЦРУ никогда не удастся выкрасть Эдварда Сноудена из России, ведь он навеки прикреплен к районной поликлинике.',

        'Террорист-смертник в зоомагазине кричит:\n'
        '— У вас есть 30 секунд, чтобы выйти из помещения, прежде чем я его взорву!\n'
        'Черепаха:\n'
        '— Вот сволочь!',

        'Подходит зебра к гаишнику и, поглядывая на жезл, смущенно говорит:\n'
        '— Простите, а где вы это взяли?',

        '— Как ты избавился от тараканов?\n'
        '— Да я китайский карандаш купил.\n'
        '— И как результат?\n'
        '— Вон, сидят тихонько в уголке, рисуют.',

        'В океане обнаружен гибрид акулы с золотой рыбкой\n'
        '— исполняет три последних желания!',

        '«Разрывная», — подумал Штирлиц, раскинув мозгами.',

        'Штирлиц долго смотрел сначала в одну точку, потом в другую…\n'
        '«Двоеточие», — подумал Штирлиц.',

        'Штирлиц приготовился к бою, а пришла гёрл…',

        '— Что общего между барабанщиком и философом?\n'
        '— Оба рассматривают время как абстрактное понятие.',

        'Почему каждую новую зубную пасту всегда рекомендуют только девять из десяти стоматологов?\n'
        'Кто этот десятый, которому постоянно всё не нравится?',
        
        'Однажды царь собрал всех бояр придворных и задал вопрос:\n'
        '—Почему налогов всё больше и больше, а в казне денег всё меньше и меньше?\n'
        'Тогда придворный шут взял кусок льда и пустил по кругу через все руки, до царя дошла капля!\n'
        'Тогда по кругу пустили самого шута, ибо нех*й тут умничать.',

        '— А ёжик выйдет? — с надеждой спросил Олег.\n'
        '— Даже не знаю… Случай-то уникальный, — ответил проктолог.',

        '— Блин, ручка кончилась.\n'
        '— Как мило вы называете ампутацию.',

        'По домофону очень легко угрожать. Просто звонишь в любую квартиру:\n'
        '— Откройте дверь.\n'
        '— Не открою.\n'
        '— Я знаю, где ты живёшь.',

        '— Это психолог? Меня постоянно преследуют мысли о суициде! Я хотел бы записаться на консультацию\n'
        '— Есть окошко на завтра.',

        'Две вещи не стареют: черный юмор и невакцинированные дети.',

        'Мазохиста Андрея укусил комар: мелочь, а приятно.',

        'Проезжая мимо церквей, многие люди крестятся. Это называется «православный чекпойнт».',
]

print(random.choice(anekdot))