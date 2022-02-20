# -*- coding: utf-8 -*-
import os
import telebot
from telebot import types

token = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in [
        'ОРВИ/ОРЗ🤧',
        'ГВ🤱',
        'Витамин Д💊',
        'Паразитоз🐛',
        'Анемия👽',
        'Аптечка🩹',
        'Ожог🔥',
        'Ушная боль🦻🏻',
        'Зубная боль🦷',
        'Запор💩',
        'НЕ ДАВАТЬ!❌',
        'Диарея/Рвота🤮',
        'Падение🤕',
        'Прикорм🥦',
        'Онлайн консультация',
    ]])
    bot.send_message(m.chat.id, 'Выберите жалобу:', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def message(message):
    if message.text == 'ОРВИ/ОРЗ🤧':
        keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in [
            'Сопли',
            'Красное горло',
            'Кашель',
            'Температура'
        ]])
        bot.send_message(message.chat.id, 'Выберите жалобу ниже или вернитесь на главное меню (/start)', reply_markup=keyboardgostart)
    elif message.text == 'Сопли':
        bot.send_message(message.chat.id, '''
🍀 обеспечте прохладный 23°, влажный 60% воздух в комнате где находится малыш.
🍀 уделите ему больше внимания носите на ручках.
🍀 промывайте носки водичкой (морской ⚓ или аптечной) не увлекайтесь и не перестарайтесь.
🍀 не капайте никакие масляные капли 💦 и масла в нос типа пиносола, хлорфилипта,сопелок.
🍀 кормите пупсиков по желанию, нет аппетита ненужно настаивать.
🍀 предлагайте напитки любые, какие считаете нужным и на какие нет аллергии (соки, воды, морсы, компоты, настои, чаи).
🍀 купать малышей можно, особенно с добавлением пачки соли на ванну.
🍀 гулять по погоде нужно.
🍀 чаще мойте руки и умывайтесь.
🍀 не приглашайте и не ходите в гости.
🍀 обратитесь к доктору, сдайте анализ (риноцитограмму), это поможет определить какой насморк аллергический, бактериальный...
🍀 не использовать без острой необходимости устройства аспирационные, не делать "кукушку "
🍀 не заливать в носики полаптеки.
🍀 не спешите непременно вставить в попу свечку.
🍀 ну раз уж заболел дайте поболеть спокойно, не подвергайте стрессу.
🍀 будьте в меру бдительны, я вам всегда готова помочь, назначить лекарства, и направить к лору при необходимости.
🍀 будьте счастливы и здоровы.

Для возврата на главное меню, нажмите /start.''')
    elif message.text == 'Красное горло':
        bot.send_message(message.chat.id, '''
💚Красное горло и что с ним делать?
Для начала красное горло -это нормальная реакция слизистой в ответ на попадание вирусов или бактерий, это воспалительная реакция организма,то есть красное горло это не диагноз это симптом.
💜 При ОРВИ красное горло лечить бесполезно! Не придумали такого средства которое убило бы вирусы сидящие в клетках, поэтому единственное что нам остается-облегчить жизнь больному и убрать дискомфорт.
💜 Боль в горле 💜
Здесь поможет холод который приводит к сужению сосудов , что в свою очередь уменьшает отек тем самым уменьшая боль.холод не увеличивает сроки болезни и риски тяжелого течения и осложнений. Подойдет рассасывание кусочка льда или замороженного сока, мороженое, йогурт, для грудных детишек охлажденное грудное молоко. отофаг/фагодент прямо из холодильника.
💙Парацетамол и ибупрофен  обезболевают, снимают жар ( не увлекаться).
💙Более старшим детям можно использовать лизобакт, стрепсилс, граммидин и подобные но их нет в международных протоколах.
💙у детей до 6 лет спреи в горло не разрешены так как они могут синхронизировать вдох и выдох, есть риск ларингоспазма /вспомнили мирамистин / леденцы опасны удушьем.В любом случае обильное питье для увлажнения слизистых.

Для возврата на главное меню, нажмите /start.''')
    elif message.text == 'Кашель':
        bot.send_message(message.chat.id, '''
Если у вашего ребенка кашель из-за соплей, то в первую очередь вылечить сопли.
Обратиться к педиатру, чтобы послушала какой кашель у ребенка (влажный или сухой).
В рацион добавить жиры и масла богатые витамином А.

Для возврата на главное меню, нажмите /start.''')
    elif message.text == 'ГВ🤱':
        keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in [
            'Мало молока',
            'Лактостаз',
            'Правильное прикладывание',
            'Питание на ГВ',
            'Завершение ГВ',
            'Прибавки',
        ]])
        bot.send_message(message.chat.id, 'Выберите жалобу ниже или вернитесь на главное меню (/start)', reply_markup=keyboardgostart)
    elif message.text == 'Мало молока':
        bot.send_message(message.chat.id, '''
Алгоритм действий в ситуации мало молока:

1) Коррекция прикладывания к груди:
 Правильное прикладывание к груди- это залог эффективного опорожнения груди. Если малыш неправильно приложен к груди, то он может сосать грудь часто и долго, но при этом не получать достаточное количество молока. 

2) Частое прикладывание малыша к груди, каждые 1-1,5 часа.
Смотрим по малышу, если ребенок не готов прикладываться к груди так часто, протестует, тогда:
- корректируйте прикладывание
- чаще меняйте грудь в одно кормление

3) Частая смена груди- в одно кормление вы предлагаете 2-4 и более груди.
Как это делать?
приложите малыша к груди правильно
малыш начинает активно глотать, через 5-7 минут активных глотков, начинайте использовать метод сдавления груди. С методом сдавления малыш глотает ещё 2-4 минут. После чего вы забираете грудь и перекладываете кроху снова к первой груди (там все тоже самое- активные глотки 5-7 минут, потом 2-4 минут с методом сдавления). За одно кормление можно дать 2-6 груди, в зависимости от потребностей малыша, его готовности сосать и глотать.

4) Кормление малыша ночью:
Пролактин- гормон, который отвечает за количество молока. Наибольшая выработка гормона Пролактина приходится на ночной период, с 3 до 8 утра  для того, что молока вырабатывалось больше, важна стимуляция груди в этот промежуток времени. Без ущерба для сна мамы и ближайших родственников, помогает реализовать ночные кормления совместный сон с малышом 
Желательно покормить малыша с 3 до 8 утра минимум 2 раза

5) Кормящей маме нужен отдых!
Выделение молока из груди связано с гормоном окситоцином. Когда мама находится в состоянии тревоги, гормоны стресса подавляют окситоциновую реакцию молоко плохо выделяется из груди.⠀

Если у малыша прибавки веса за 4,5,6 месяц 200-300 грамм, то можно ввести:
6) Дополнительные сцеживания.
Сцеживание - это дополнительная стимуляция груди + сцеженное молоко является приоритетным докорм для ребенка
Как правильно сцеживать молоко ?
Сцеживать нужно обе груди 30 минут, по 15 минут на каждую, если нет такой возможности, то сцеживайте грудь столько, сколько получается
1-3 сцеживания, плюс коррекция прикладывания и организации ГВ - будет достаточно.

Для возврата на главное меню, нажмите /start.''')
    elif message.text == 'Прибавки':
        bot.send_message(message.chat.id, '''
💝Самое первое и самое важное, что необходимо знать, что единственный достоверный признак достаточности питания для малыша, - это прибавки.
💖Если они менее 500гр/мес или менее 140гр/нед, то ребёнок не получает достаточно питания, или, проще говоря, у вас мало молока.
💗Так же, если ребёнок набирает указанный минимальный вес, то никакие ваши подозрения, истерики, плач ребёнка не могут говорить о том, что у вас мало молока, и в данном случае докорм вводить не нужно! Отбросьте все сомнения и кормите в удовольствие!
💜Возьмите в аренду весы на авито, это недорого. Нельзя взвешивать ребёнка ежедневно, несколько раз в сутки, до, во время или после еды, это все ни о чем не говорит, вы только сами себя запутаете, будете безосновательно нервничать, заработаете себе высокий кортизол, а на таком фоне молока не только не прибавится, а может знатно уменьшиться, поэтому наберитесь терпения и взвешивайте не чаще раза в неделю без одежды примерно в одно и то же время суток.
💙Если прибавки меньше минимальных, ребёнку нужен докорм! Это может быть донорское грудное молоко, смесь.
💚Параллельно рекомендуется заняться увеличением количества молока с помощью квалифицированного консультанта по грудному вскармливанию. Хотя бы через онлайн консультации.
💛Если даже такой возможности нет, то начните работать по схеме, приведённой под кнопкой *мало молока*. Схема рабочая и помогла очень многим женщинам.
‼️🧡‼️ВАЖНО!‼🧡‼️ ️ Пока вы увеличиваете количество молока, докорм смесью убирается ПОСТЕПЕННО, при этом вы постоянно отслеживаете прибавки ребёнка, чтобы они были не ниже минимальных! Чтобы не запутаться, сколько вводить докорм, на сколько грамм уменьшать, сколько раз давать, чувствовать себя уверенно, все же лучше обратиться к консультанту по гв. Поверьте, это в десятки раз дешевле, чем потом в течение более полутора лет покупать ребёнку смесь.
❤️Успешного грудного вскармливания!

Для возврата на главное меню, нажмите /start.''')
    elif message.text == 'Лактостаз':
        bot.send_message(message.chat.id, '''
🤍Лактостаз - это застой молока, который возникает, если в какой-то части груди нет движения молока.
🤍Симптомы:
    ●Уплотнение в груди
    ●Болезненность в груди
    ●Покраснение участка груди на месте уплотнения
    ●Повышение температуры тела
    ●Ломота в теле, головная боль
    ●Малыш беспокоится у груди, из которой затруднен отток молока
🤍Причины:
    ●Неправильное прикладывание, из-за чего малыш плохо опорожняет грудь
    ●Регулярные сцеживания
    ●Пропустили очередное кормление
    ●Гиперлактация - много молока
    ●Закупорка протока - молочная пробка/мозолька на соске
    ●Тесное неудобное белье
    ●Травма груди
    ●Инфекция
    ●Усталость и стресс - гормоны стресса препятствуют свободному вытеканию молока из груди
🤍Алгоритм действий:
    ●Как можно чаще прикладывать ребёнка к груди. Если ребёнок отказывается сосать эту грудь, то мягко сцеживайте, ни в коем случае не разминайте руками шишки, вы можете порвать проток, что приведёт к образованию молочной кисты.
    ●Перед кормлением делать лимфодренажный массаж на больную грудь, мягкие плавные нежные движения от соска к лимфоузлам у ключицы и в подмышечной впадине
    ●Перед кормлением после массажа делать 5-минутный холодный компресс, приложив холод через пеленку. Можно налить воды в чистый подгузник и заморозить его для этих целей.
    ●Холод и лимфодренажный массаж хорошо снимают отёк, после чего облегчается выход молока из груди.
    ●Между кормлениями прикладывать на грудь прохладный капустный лист, предварительно поскоблив вилкой, либо намазать Траумель гелем.
    ●Продолжайте все действия до полного выздоровления.
🤍Признаки того, что вы справились с лактостазом:
    ●Снижение температуры тела (если не принимали жаропонижающее)
    ●Проходит болезненность в зоне уплотнения либо значительно уменьшается
    ●Размер уплотнения значительно уменьшается либо оно больше не пальпируется
    ●Самочувствие улучшается
🤍Если в течение 3 суток уплотнение сохраняется либо температура повышена более суток, в обязательном порядке пройдите узи молочных желез и покажите результаты маммологу.


Для возврата на главное меню, нажмите /start.''')
    elif message.text == 'Правильное прикладывание':
        bot.send_message(message.chat.id, '''
Признаки правильного прикладывания к груди:
1️⃣ Мама не испытывает неприятных ощущений в области соска и ареолы (даже в первые минуты кормления);⠀
2️⃣ Рот широко открыт, губы не напряжены;⠀
3️⃣ Не слышно посторонних звуков (причмокивания, цоканья);⠀
4️⃣ Подбородок «утоплен» в грудь;⠀
5️⃣ Носик может касаться, может не касаться груди, но не утопает в
груди;⠀
6️⃣ Над нижней губой может быть виден язычок;⠀
7️⃣ Во время сосания ребенок захватывает снизу больше груди, чем
сверху (примерно 3-4 см снизу и 2-3 см сверху);⠀
8️⃣ После сосания сосок ровный, круглый, иногда может быть
удлинен. Не скошен, не сплющен;⠀
9️⃣ Ушко - плечико - бедро находятся на одной линии.

Для возврата на главное меню, нажмите /start.''')
    elif message.text == 'Витамин Д💊':
        bot.send_message(message.chat.id, '''
    💜ВИТАМИН Д💜
    - Дозировка для новорожденного до 6месяцев жизни на гв (при том что у мамы хороший уровень витамин Д и она профилактически продолжает принимать) - 1000ме.
    - С 6месяцев до 1,6 это 1600ме.
    - Ближе к 2м годика это 2000ме, без анализа!!!! с анализами другие подсчеты.
    Аквадетримы,детримаксы,эвалары дети приходят с рахитом, перевозбужденные, не спящие.
    Дело Ваше, Вам виднее что и как и когда давать.''')
    elif message.text == 'Паразитоз🐛':
        bot.send_message(message.chat.id, '''
💜Подготовка к  исследованию на паразитоз.💜
1) Пьете желчегонные - фламин, артишок,хофитол, шиповник, по инструкции, за полчаса до еды три раза в день около месяца.
2) Примерно каждые  5-7-10 дней сдаете кал методами - парасеп, либо двойная седиментация, либо расширенное информативное копрологическое исследование Фарм-т(Казань).
💜 Чтобы повысить вероятность нахождения сдавать в период угасающей луны, в этот период паразиты выходят.💜
Ну а если нашли:
💚оак с лейкоформулой
💚оам
💚копрограмма
💚узи органов брюшной полости
👣Если есть атопия, то эозинофильнокатионный белок, с-реактивный белок, ig E иммуноглобулин, чтобы отличить аллергию от паразитоза.
💜Найдем причину и устраним вместе , обращайтесь на личную консультацию.''')
    elif message.text == 'Анемия👽':
        bot.send_message(message.chat.id, '''
Диагностика причин анемии :
🍀 Общий анализ крови +Соэ, L формула.
🍀 Общий анализ мочи
🍀 Ретикулоциты
🍀 Гематокрит
🍀 Витамин В12
🍀 Фолиевая кислота.
🍀 Железо (сыворотка крови) +ОЖСС.
🍀 Ферритин.
🍀 УЗИ брюшной полости.
Всем мамулечкам на гв обязательно дважды в год как минимум.''')
    elif message.text == 'Аптечка🩹':
        bot.send_message(message.chat.id, '''
Летняя аптечка нужна для:
1️⃣экстренных ситуаций (ночью, оказания первой помощи)
2️⃣случаев, когда можно обойтись без помощи врача.
❌Любые другие препараты назначаются только врачом.
🚨Поэтому при выезде заграницу-ОБЯЗАТЕЛЬНО оформить мед.страховку!
🤔Не берите лекарства с недоказанной эффективностью и много лекарств (можно вынуть из пачки один блистер.
🚨ПРИМЕРНЫЙ СПИСОК:
✅Жаропонижающее и обезболивающее (на основе парацетамола-Панадол,Цефекон Д, Эффералган и ибупрофена-Ибуфен, Нурофен и др)- свечи или сироп, строго по инструкции!)
❗Анальгин/аспирин/димедрол-запрещены у детей! Не протирать уксусом/водкой!
✅Антигистаминные препараты (супрастин/фенистил/зиртек/зодак эриус)
✅Электролитный раствор (Хумана Электролит, Гидровит, Регидрон Био, адиарин регидро,биогая орс)
✅Антибактериальная мазь (бактробан/агросульфан/левомеколь/банеоцин и др)
✅Перевязочный материал: пластыри, самоклеющийся бинт, марлевые салфетки (на небольшие ссадины можно нанести клей БФ или его аналоги)
✅Местные стероиды (гидрокортизон крем, Локоид)
✅Эластичный бинт
✅Пипетка, пинцет, ножницы
✅Противовоспалительные глазные капли (Тобрекс, левомицетиновые глазные капли).
✅Устройство для изъятия клещей
✅Гемостатическая губка или аналоги (порошок или бинт Целокс Celox, на основе хитозана или спрей на основе окисленной целлюлозы СМАРТ и аналоги (маркирован m-doc)
✅Криопакет (Холодок,Снежок)
✅Противоожоговый гель с антисептиком и анестетиком (например, «Аполло»), но первая помощь охлаждаете водой!
✅Антисептики (Мирамистин, Хлоргексидин)
✅Сорбенты (Активированный уголь, Смекта , полисорб,энтеросгель)
🚨Если в семье были случаи анафилаксии, в международных протоколах рекомендовано носить с собой авто-инъектор с адреналином (Epipen, Jext, Adrenaclick). Но в РФ удобной формы препарата нет.
👩🏼‍⚕В аптечке нет ушных капель, тк эти препараты назначаются после осмотра врачом и зависят от вида отита (для обезболивания при боли в ухе применяется жаропонижающее).
Но анауран можно даже при перфоративном отите.
🌊Также я не стала включать в аптечку солевой раствор в нос:думаю, это не срочная мед.помощь, спокойно успеете его купить или на крайний случай сделать самостоятельно.
Ну и как же без соленых ванн то.
❗Важно знать о ближайших мед пунктах!
🤓Корректируйте аптечку под себя!
❗Всегда следуйте инструкции!''')
    elif message.text == 'Ожог🔥':
        bot.send_message(message.chat.id, '''
Первая помощь при ожоге и единственная - это холодная вода и точка, не пантенол, не ещё что-то.
Даже если уже волдырь, даже если солнечный.
Цель-охладить и увлажнить, как можно быстрее, чтобы не усугубить. Долго, пока не перестанет жечь.
Только на стадии заживления можно ранозаживляющие никак не в момент.
В момент только вода. Запомнить ожог - вода.
Берегите себя. В аптечке держите маленький пузырек масла чёрного тмина. На стадии заживления прекрасно справляется,без шрамов.''')
    elif message.text == 'Ушная боль🦻🏻':
        bot.send_message(message.chat.id, '''
При прорезывании зубов бывает ушная боль, даже если не красно там нигде.
Оталгия при синдроме прорезывания зубов.
Помогает вибрукол, парацетамол если очень больно, анауран всё таки, и капельки камелия.''')
    elif message.text == 'Зубная боль🦷':
        bot.send_message(message.chat.id, '''
Что касается прорезывания зубов. Это одно из первых испытаний болевого порога малыша.
🌷 Почему же у некоторых детишек синдром прорезывания зубов проходит незаметно, а у некоторых с зудом, болью, слюнотечением, порой даже насморком и диареей?!
Да всё по причине разного восприятия боли, всему виной особенности нервной системы.
И у взрослых также, зуб мудрости кто-то даже не замечает, а кто то страдает.
Если вы на ГВ, то при прорезывании обычно всегда помогает успокоение грудью.
Если сильно переживаете, ребенку больно и нет ГВ, то должны помочь Дантинорм Бэби или Камилия(iherb).''')
    elif message.text == 'Температура':
        bot.send_message(message.chat.id, '''
У ребенка появилась температура, и у родителей сразу же паника.
На этом этапе появляется масса вопросов. Ответим на них.

💚До каких цифр можно терпеть? При каких цифрах сбивать?
Всех интересует точная цифра. И очень хочется сбивать.
Почему-то считается, что если не загасить температуру 39, то вскоре она будет 40, потом 45, 49, и далее.
Но ведь ребенок не механизм, не циферблат.
Посмотрите ему в глазки, если он видит Вас, способен улыбнуться, говорит, пьет водичку – все нормально, продолжаем питье.
Температура – это правильная, хорошая реакция организма на инфекцию. Ваше дело – помочь ребенку справиться, а не разрушить его защиту.
Вот он, первый закон: не сбиваем температуру без особой нужды. Да вы правильно поняли, даже высокую.

💚Если ребенок плохо переносит высокую температуру, не смотря на все ваши действия (так
бывает, очень редко) - даем жаропонижающее!
Половину возрастной дозировки!
Пусть температура снизится не до нормы, а на 1 градус, И продолжаем поить.
 Если кожа вашего ребенка, несмотря на высокую температуру, розовая и влажная на ощупь, вы можете быть, относительно спокойны- баланс между теплопродукцией и теплоотдачей не нарушен.
Но если кожа бледная, руки ноги холодные, а ребенка бьет озноб, то это белая или бледная лихорадка, при которой возникает спазм сосудов. Причиной могут быть поражение центральной нервной системы, нехватка жидкости, снижение давления и другие причины.
Все это говорит о серьезности болезни, необходимости оказания первой помощи и срочного обращения к врачу.
Все остальное неэффективно или небезопасно. Не тратьте деньги и берегите организм ребенка (все препараты проходят через печень).
Не подвергайте ребенка лишним рискам, в том числе риску аллергической реакции или еще опаснее аутоиммунным заболеваниям.


Для возврата на главное меню, нажмите /start.''')
    elif message.text == 'Запор💩':
        bot.send_message(message.chat.id, '''
Если ваш ребенок на ГВ с 1,5 месяца до начала прикорма, то ребенок может не испражняться до 7-10 дней. Это считается нормой.
После начала прикорма запор чаще всего связан нехваткой жиров в рационе.
0-1,5 мес ребёнок должен ходить ежедневно. Если не ходит, то чаще всего причина в питании мамы (если на ГВ), надо разбираться индивидуально.
Если на ИВ или СВ, то надо разбираться со смесью.''')
    elif message.text == 'Диарея/Рвота🤮':
        bot.send_message(message.chat.id, '''
При диареи или рвоте отпаивайте водой (30мл на кг).
При рвоте: электролитный раствор (Хумана Электролит, Гидровит, Регидрон Био, адиарин регидро,биогая орс).
При диареи: сорбенты (Активированный уголь, Смекта , полисорб, энтеросгель).
    ''')
    elif message.text == 'НЕ ДАВАТЬ!❌':
        keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in [
            'Муколитики',
            'Мирамистин',
            'Хлорфилипт',
            'Фероны'
        ]])
        bot.send_message(message.chat.id, 'Выберите жалобу ниже или вернитесь на главное меню (/start)', reply_markup=keyboardgostart)
    elif message.text == 'Муколитики':
        bot.send_message(message.chat.id, '''
Лекарства, которые не следует давать малышам:

💜Во всем мире муколитики применяются с 2-6 лет с великой осторожностью , а до двух лет вообще крайне редко, только если под рукой аспиратор для дыхательных путей  и рядом есть реанимация и анестезиолог, то есть в стационаре и то не соматическом.
А все потому что у ребенка слабый кашлевой толчок из-за физиологически узких бронхов, слабых мышц диафрагмы, недоразвитых ресничек эпителия дыхательных путей.
💜Педиатры в нашей стране назначают препараты типа лазолвана с рождения, что категорически неправильно, так как есть вероятность , что ребенок захлебнется в мокроте.
Откашлять он ее не может до конца, риск удушья и заболачивания.
💜Когда его можно применять: острый и хронический бронхит, бронхиальная астма, пневмония, хроническая обструктивная болезнь легких (ХОБЛ)чаще у взрослых, бронхоэктатическая болезнь.
💜Ни в коем случае не применять при сухом кашле , в возрасте до 2 лет, а желательно до 6 лет, применять вместе с препаратами подавляющими кашель.
💜При приеме лазолвана рекомендуется больше пить, и использовать его не позже 18:00 вечера.
💜Родственники лазолвана - амбробене, флуимуцил, ацц, бромгексин, бронхолитин и дугие.
''')
    elif message.text == 'Мирамистин':
        bot.send_message(message.chat.id, '''
💟Мирамистин
💬 Производитель заявляет его , как бактерицидное(убивает бактерии), противогрибковое, противовирусное (с оговоркой /действует только на сложные вирусы вич и герпес, орви вызывается простыми вирусами).
💬Хорошо его применять как наружное средство при ранах, ожогах, для обработки рук, когда нет возможности их помыть водой с мылом.
💯 Детям до трех лет запрещено использовать, есть риск ларингоспазма и отравления (бензилдиметил3миристоиламино пропил аммония хлорида моногидрат).
Ну и что , что он ничем не пахнет и без вкуса это не вода все же, бензин не пьем ведь сами, а ребенок до трех лет не умеет выплюнуть его.
💬Следующий момент: От боли в горле не поможет и от его покраснения тоже, так как не всасывается в слизистые оболочки.
Да, вы скажете,что вам помогает. Он ли? А может обильное питье? А может леденцы от боли в горле? Или антибиотик, который назначил врач пр ангине?
💬 По хорошему, нельзя назначать для профилактики. Убьете нормальную микрофлору (я знаю мамы садиковых детей часто балуются из разряда хоть что-то нужно ведь делать!).
На месте нормальной флоры будет патогенная тут как тут и будет вам болезнь.
Более того у многих к нему уже есть устойчивость, то есть в некоторых случаях он вообще не поможет, а в некоторых подкормит мутирующие микробы.
💣Нельзя применять в виде ингаляций он для этого не предназначен, сломаете небулайзер, риск удушья, неэффективен в конце концов!
💥Качественных исследований нет, на людях исследований тоже нет, а стоит он не дешево.💟''')
    elif message.text == 'Хлорфилипт':
        bot.send_message(message.chat.id, '''
Эфирные масла очень часто вызывают ларингоспазм (стеноз гортани).
И в инструкции к препарату нет порказаний как красное горло.
Хлорфилипт препарат против стафиллококка.
Если у вас там не стафиллококк, а другие микробы вирусы или тем более грибы, то это просто неэффективно.
''')
    elif message.text == 'Фероны':
        bot.send_message(message.chat.id, '''
Дано:
У ребенка нормальный иммунитет он борется прекрасно с 38.4, зачем виферон?
Чтобы был пирогенный эффект и было 41? Зачем? У ребенка уже вырабатываются эндогенные настоящее фероны свои, зачем вставлять фероны?
Чтобы потом сбивать нурофеном? Для чего эти качели? Просто, чтобы самоутвердиться, что Вы что-то делаете?
А об аутоиммунным процессах кто то думает, а об отдаленных последствиях безконтрольных приемов интерферонов?
Сколько подростков страдают от аутоиммунных заболеваний разнообразных.
Да да!!!! им в детстве всем вставляли фероны в анамнезе, и сколько реактивных панкреатитов вы знаете???
Я вижу это каждый день!!!!!
Так что не нужно в чатах рекомендовать фероны.
Я их сама назначу если есть показания, а повод убедительный для них очень редок!!!!
''')
    elif message.text == 'Падение🤕':
        bot.send_message(message.chat.id, '''
Если ребенок упал с высоты, то:
1) Понаблюдайте за состоянием, поведением (беспокойство, вялость).
2) Посмотрите зрачки (одинаковый ли размер).
3) Есть ли тошнота, рвота.
4) Идет ли кровь и есть ли рана.

Если все хорошо, то нет повода для беспокойства.
Если есть какой-то из пунктов, то лучше сразу же обратиться к врачу.''')
    elif message.text == 'Прикорм🥦':
        bot.send_message(message.chat.id, '''
С чего начать прикорм?
Однозначно с выявления готовности ребенка к прикорму - с пищевого интереса🤗
И в зависимости от исходнных данных, так скажем, если были проблемы (например, ЛН, аллергии, АД, дисбиоз и тд), то рекомендуем залечить и подготовить кишечник - начать с гапс бульона, если всё хорошо - то сезон свежих овощей - отличное время для введения прикорма с кабачков, тыковки, брокколи и тд.
Обязательно с добавлением масла ГХИ или растительных прямого отжима.

Кто в самом начале введения прикорма, сделайте лучше так:
- потушите на масле гхи овощи,
- попробуйте дать кусочком, некоторые дети сразу начинают маковать.
Можно запечь и после заправить маслом. И вместе с малышом самим вкусно поесть, чуть  посолив, например. Это будет лучший пример.
Чем дать пару ложек из банки пюре, которое сама мама не ест, потому что "бяка"))''')
    elif message.text == 'Завершение ГВ':
        bot.send_message(message.chat.id, '''
Определение готовности малыша к завершению ГВ
Пройдите тест, который вам поможет определить готовность малыша к завершению ГВ!

Будьте предельно честны, проходя тест, свои ответы, пишите на листе бумаги или специально приготовленной тетради.
И помните, что это нужно в первую очередь вам, чтобы начать работу по завершению ГВ вовремя и провести ее максимально мягко 🙏
Автор теста: команда консультантов АКЕВ

1) У малыша нет необходимости прикладываться к груди для того, чтобы уснуть на ночь и/или на дневной сон
2) Ночью малыш прикладывается к груди несколько раз.
3) Малыш перестал прикладываться при пробуждении после дневного сна.
4) В течение дня малыш может запивать из маминой груди свои завтраки, обеды или ужины.
5) Дневных прикладываний у малыша стало значительно меньше, чем прежде.
6) Малыш прикладывается к груди, когда ему необходимо утешение по какому-либо поводу (больно, страшно, устал).
7) Утром, при пробуждении, ребенка часто можно отвлечь от мысли о сосании.
8) Ребенок может приложиться к груди, если хочет пить.
9) Если днем ребенок просит грудь, а мама предлагает подождать и отвлекает его каким-то занятием, он долго не вспоминает о своем желании пососать.
10) Малыш просит приложить его к груди, если мама входит в дом после долгого отсутствия.
11) В течение ночи малыш прикладывается редко или не прикладывается совсем.
12) Он часто прикладывается, когда ему скучно и нечем заняться или когда мама принимает неподвижную позу, например, садится разговаривать по телефону.
13) Днем в отсутствие мамы ребенок может уснуть с другим человеком.
14) Если у малыша появляется потребность приложится, его бывает сложно от этой идеи отвлечь.
15) Ребенок почти не нуждается в утешении у груди при решении каких-то своих проблем.
16) Если на ночь в отсутствие мамы малыша попробует уложить спать другой человек, он вряд ли сумеет заснуть.
17) В течение суток у ребенка осталось всего 1-3 прикладывания.

Подсчет результатов.

Добавьте себе по 1 баллу за каждый отрицательный ответ на вопросы: 1, 3, 5, 7, 9, 11, 13, 15, 17.
Добавьте себе по 1 баллу за каждый положительный ответ на вопросы: 2, 6, 8, 12, 14, 16.
Добавьте себе по 2 балла за каждый положительный ответ на вопросы: 4, 10.

Результаты теста.

Если Вашему малышу больше 2-2,5 лет и на последний (№17) вопрос теста Вы ответили «Да», значит Вам с ним осталось сделать последний, завершающий шаг.
А сделать его уже сегодня или несколько месяцев спустя – решать только вам двоим. В любом случае вы оба – большие молодцы. А Вашему малышу очень повезло с мамой!
0-6 баллов:
Возможно, Ваш малыш уже действительно почти готов к завершению грудного вскармливания.
Однако если теперь кроха начнет посасывать свой пальчик, нижнюю губку или что-нибудь еще, не игнорируйте эти симптомы. Они говорят о том, что с отлучением Вы немного торопитесь. И если не отнестись с пониманием к потребностям Вашего маленького человечка, это может серьезно отразиться на его нервной системе в будущем.

Помните, что процедура завершения ГВ  с самого начала и до самого конца должна проходить плавно, постепенно, по принципу «шаг вперед – два назад». И если через неделю результаты теста окажутся иными – не удивляйтесь, это нормально. Просто наберитесь терпения.
В конце концов, волнуясь в день своей свадьбы, ваше чадо точно не полезет к Вам за пазуху!

7-12 баллов:
Кое-что в ваших взаимоотношениях с малышом уже изменилось. Но не стоит торопить события. Все-таки на этом этапе заменить малышу мамино молочко невозможно ничем. Что уж говорить о минутах блаженства, проведенных малышом у мамы под грудью!
Да и самой маме проще успокоить расстроенного малыша, приложив его к груди, чем пытаться объяснить ему, что разбитая коленка скоро заживет, а молочка у мамы все-равно уже нет (в такие минуты малыши не желают понимать ни того, ни другого).

13-19 баллов:
Если по результатам теста Вы набрали баллы в этом интервале, знайте, что малыш, ведущий себя подобным образом, к завершению ГВ  пока еще не готов.

Для возврата на главное меню, нажмите /start.''')
    elif message.text == 'Питание на ГВ':
        bot.send_message(message.chat.id, '''
Ребёночек толерантен к Вашей пище ещё с утроба матери.
Диета вообще непонятное слово, тем более на ней" сидеть".
Есть особенности, традиции, вкусы, предпочтения, непереносимости.
Старайтесь убрать пищевой мусор, массмаркет, консерванты, красители,и питайтесь разнообразно.

Завтрак кормящей мамы должен быть сытный белковый и жировой!
Исключить глютен и сахар.
Яйцо,красная рыба,или икра или мясо или птица, сливочное масло ,авокадо, безглютеновый хлеб,  и зелень, огурчики ,гапс бульон или холодец,квашеная капуста и так далее.
Сырые овощи и зелень ешьте, это же защелачивание.
Каши - это  фитин, что препятствует всасыванию минералов из еды, можно,но вымоченные желательно безглютеновые, эта еда уж не яд)))
Сами делайте молочко кедровое, кокосовое, миндальное, кешью фундучное с предварительным замачиванием прекрасно.
Молоко и кисломолочное магазинное убираете, только если деревенское фермерское типа творога катык можно.
Утром всегда обычная вода до завтрака. После такой еды не захочется перекусов.
Чай желательно травяной и ягодный, обычный черный как можно реже, кофе натуральный изредка можно,но в идеале исключить.
Супы можно, котлетки из мяса, рыбы птицы.
Масла  в  рацион, сливочное можно козье или коровье. И растительные нерафинированные, кедроврго ореха горчичное, оливковое, виноград косточки, тыквенных семечек, 🥑, кокосовое,гхи, жиры животные.
Антиоксиданты в виде ягод, овощи приготовленные и сырые плюс листовая зелень нужна.
Печенье пеките безглютеновую, блинчики, сырники, пряники, что угодно.
Из сладкого можно мед и  финики.
Питание продуманное  питательное должно быть и жирное.
Никода не видела чтобы мед плесневел, поэтому я мед разрешаю.
Фрукты кислые можно ,а бананы нет.
Ягод побольше любых.
Принцип такой: сытно кушать, но без батонов, печенек магазинных.
Картофель можно изредка,но паслёновые могут вызывать воспаление в кишечнике, как можно реже.

Для возврата на главное меню, нажмите /start.''')
    elif message.text == 'Онлайн консультация':
        bot.send_message(message.chat.id, '''
Вы можете обратиться за личной консультацией к Айгуль Фаридовне.
Для этого напишите ей личное сообщение по логину (@aigulfaridovna) с пометкой НУЖНА ОНЛАЙН КОНСУЛЬТАЦИЯ и сразу приложите ответы на вопросы ниже в этом же сообщении.
Стоимость консультации от 1000 рублей, в зависимости от сложности вопроса.

Вопросы:
💙Ваше имя и малыша
🧡Откуда Вы
💜Рост вес ребёнка
💛Возраст
🤍Какие по счёту роды
💚Способ родовспоможения
🧡Перенесенное заболевание во время беременности
💛Наблюдался ли во время беременности токсикоз головные боли запоры расстройство стула симптомы неблагополучия на коже ногтях волосах  сыпь зуд сухость выпадения волос
🧡Какие лекарственные средства принимала мама во время беременности в каком триместре
💜Был ли приложен к груди
🤎Антибиотики в роддоме или в первые месяцы жизни
🖤Симптомы которые беспокоят настоящий момент
💓Стул сколько раз в день и какой аппетит сколько раз включая перекусы
💚Сколько и как спит
💜Есть ли бледность, желтушность, потливость, родинки, пигментные, пятна, гемангиомы
❤️Имеется ли аллергия какая и на что
💜Имеется ли отягощенный наследственный анамнез
❤️Хронические заболевания и патология
💛Было ли грудное вскармливание в первые 6 месяцев жизни ребёнка если смесь то какая смесь сейчас присутствует смесь? какая?
🤍Перенёс ли ротавирус норовирус коронавирус аденовирус кишечная инфекция
🧡Укачивает ли в автомобиле
💙Бывает ли рвота и как часто
💚Употребляет ли молочные продукты хлебобулочные изделия макароны крупы сладости полуфабрикаты соки и другие сладкие напитки
🥬Опишите подробнее Ваше традиционное питание
💛Посещает ли детский сад
❤️Все ли прививки по возрасту
🧡Если хоть какой-нибудь диагноз поставленный врачом
💙Когда и чем болел
💜Антибиотики были ли? когда ?гормоны и другие сильнодействующие препараты ?
💛Какой у вас запрос на консультацию?''')


bot.polling()
