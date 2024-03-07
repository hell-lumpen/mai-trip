from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram.utils.media_group import MediaGroupBuilder

import config
from buttons import get_keyboard_all_audience, get_keyboard_contact, get_keyboard_main, get_keyboard_nav
from config import room

navigator = """
        Приветствую тебя! Я твой гид по IT-этажу Института №8. Давай я покажу тебе, что у нас есть. Выбери интересующую тебя локацию:

        1. 💼 <b>Коворкинг</b> - Уютное место для совместной работы и обмена идеями.
        2. 🕶️ <b>VR/XR лаборатория</b> - Погрузитесь в виртуальную реальность и экспериментируйте с расширенной реальностью.
        3. 🎓 <b>Лекториум</b> - Место для проведения лекций, семинаров и мастер-классов.
        4. 🤖 <b>Лаборатория ИИ</b> - Исследовательскя лаборатория студентов и сотрудников института.
        5. 🖼️ <b>ИИ картины</b> - Сборник совместного творчества нашего преподавателя и искусственного интеллекта.
        6. 🎒 <b>Студентческая лаборатория Лямбда</b> - Место, где студенты могут воплощать свои идеи и проекты в жизнь.
        7. 🏆 <b>Центр олимпиадного программирования</b> - Здесь готовятся будущие чемпионы программирования, шахмат, а также Яндекс Лицей.
        8. ☕ <b>Центральная зона</b> - руководство института и теннисный стол.
        9. 💻 <b>Партнеры</b> - Стенд партнеров.
        10. 🖥️ <b>Холл зоны Б</b> - Компьютерные классы, серверная, кафешка.
        """


async def navigation(call: CallbackQuery):
    answer = ''
    answer_photo = None
    answer_video = None
    answer_video_note = None
    mrkp = None
    is_edit = False
    it5 = False

    if call.data == 'audience-0':
        album_builder = MediaGroupBuilder()
        album_builder.add_photo(
            media='AgACAgIAAxkBAAIE32W0wqeU_04wyhgJfKHkFkM1MFZVAALx1jEbPkioSVGqeuFhRzzbAQADAgADeQADNAQ'
        )
        album_builder.add_photo(
            media='AgACAgIAAxkBAAIE4WW0wqz6DKgg4b0zHxExy69nJCQKAALy1jEbPkioSSRsQGZDXAxlAQADAgADeQADNAQ'
        )
        await call.message.answer_media_group(
            media=album_builder.build()
        )
        answer = """
<b>Коворкинг IT-0</b>

Линус Торвальдс - финский программист, известный своим вкладом в мир технологий, создав операционную систему Linux и систему контроля версий Git. Его творчество стало символом свободного и открытого исходного кода, вдохновляя множество разработчиков по всему миру. Помимо работы в сфере IT, Торвальдс также является страстным любителем адреналина и скорости, увлекаясь гонками на мотоциклах и пилотированием самолетов.

Познакомьтесь ближе с Линусом Торвальдсом на <a href="https://www.ted.com/talks/linus_torvalds_the_mind_behind_linux/transcript?language=ru">TED.com</a>.

Сотрудничество Института №8 МАИ с ведущими IT-компаниями, такими как Yandex, VK, SBER, IVI, МТС, билайн и Лаборатория Касперского открывает студентам широкие возможности для профессионального роста. Студенты получают доступ к стажировкам, совместным проектам и обучающим курсам, что дает им ценный опыт работы в индустрии информационных технологий. Онлайн магистратура, организованная совместно с Сбером, обеспечивает студентам высококачественное образование, соответствующее современным требованиям рынка, и способствует их профессиональному развитию.
        """
        mrkp = get_keyboard_nav(int(call.data.split('-')[1]))
        config.VIEW_DATA[call.from_user.username]['audience-0'] = True
        answer_video_note = 'DQACAgIAAxkBAAIDDGW0ZNonCHssUPdRX_NvWUK1mIL9AAK2OAACyJ-oSXD9a_q0NEhPNAQ'

    elif call.data == 'audience-1':
        album_builder = MediaGroupBuilder()
        album_builder.add_photo(
            media='AgACAgIAAxkBAAIE42W0wyMtj1rDEmsgNHV69OTkHPU4AAL01jEbPkioSbLsTuHDMWHHAQADAgADeQADNAQ'
        )
        album_builder.add_photo(
            media='AgACAgIAAxkBAAIE62W0w0BTLn276jCRRMNEAzseIlWtAAL11jEbPkioSU7GDsemCf6QAQADAgADeQADNAQ'
        )
        album_builder.add_photo(
            media='AgACAgIAAxkBAAIE7WW0w4zfKN4rqu9ogjZCNliH66sMAAL21jEbPkioSZFEkssFnrdxAQADAgADeQADNAQ'
        )
        await call.message.answer_media_group(
            media=album_builder.build()
        )
        answer = """
        <b>VR/XR лаборатория</b>

В лаборатории находится большое пространство-трансформер, которое служит идеальной средой для тестирования самых передовых технологий виртуальной и дополненной реальности, робототехники, планшетов, а также глубинных камер. Это место стало неотъемлемой частью образовательной программы, где наши студенты изучают основы работы с движками Unity и Unreal Engine. Здесь они приобретают практические навыки программирования VR-приложений и разработки интерактивных симуляций.

Лаборатория также является центром математического моделирования, где проводятся исследования в области физически информированных нейронных сетей. Эти интеллектуальные системы используются для решения сложных задач, таких как аэродинамика и другие проекты, требующие обширной работы с 3D-моделями и вычислениями.

Здесь студенты и исследователи имеют доступ к самым передовым инструментам и технологиям, что позволяет им глубоко погружаться в изучение и разработку новаторских решений в области визуализации, моделирования и виртуальной реальности. Это уникальное пространство способствует творческому подходу к решению сложных задач и стимулирует инновационное мышление, что делает лабораторию идеальным местом для подготовки карьеры в сфере IT и разработки игр.
        """
        mrkp = get_keyboard_nav(int(call.data.split('-')[1]))
        config.VIEW_DATA[call.from_user.username]['audience-1'] = True
        answer_video_note = 'DQACAgIAAxkBAAIE0mW0wX-HyyOMMZb-kcZ5cN5OH9TFAAI4QgACIWigSfn5qmCMsjSaNAQ'

    elif call.data == 'audience-2':
        answer = """
        <b>Лекториум IT-5</b>
        
В этом лектории, где регулярно проходят увлекательные лекции приглашенных спикеров из крупных IT-компаний, студенты погружаются в мир последних технологических разработок и инноваций. Однако, когда они переносят свой взгляд на мониторы старых компьютеров в кружке ретро техники на ИТ-этаже, они открывают для себя совершенно иную реальность.

Эти старые компьютеры становятся не только артефактами прошлого, но и воротами в мир, где история компьютеров и их эволюция становятся источником вдохновения для будущих проектов.

В Институте №8 не только формируются будущие эксперты в области информационных технологий через лекции приглашенных спикеров, но и сохраняется связь с прошлым через кружок ретро-техники. Этот плавный переход между современными технологиями и их историческими корнями помогает студентам расширить свои горизонты, понять и ценить эволюцию технологий и вдохновиться новыми достижениями в мире компьютерных наук.
"""
        mrkp = get_keyboard_nav(int(call.data.split('-')[1]))
        config.VIEW_DATA[call.from_user.username]['audience-2'] = True
        answer_video_note = 'DQACAgIAAxkBAAIDEGW0ZQG_yGkwR7xtiQkCXI0i_jG1AAK6OAACyJ-oSW_swoeo1EXdNAQ'

        album_builder = MediaGroupBuilder()
        album_builder.add_photo(
            media='AgACAgIAAxkBAAID_GW0qv-nMCHgvSbDGrspYhktgH-XAAKJ1jEbPkioSUAZvaV2g1DUAQADAgADeQADNAQ'
        )
        album_builder.add_photo(
            media='AgACAgIAAxkBAAID_mW0qws1oMOLFvM4rEL3YnemA30NAAKK1jEbPkioSf746bBqFZO-AQADAgADeQADNAQ'
        )
        album_builder.add_photo(
            media='AgACAgIAAxkBAAID-GW0quuR-LWiD2c_9WJfELM1P-qCAAKH1jEbPkioSQuS3uteiMq2AQADAgADeQADNAQ'
        )
        album_builder.add_photo(
            media='AgACAgIAAxkBAAID-mW0qvQRJaO-8HTV3YiYlEp_TuL_AAKI1jEbPkioSX09stndd5vbAQADAgADeQADNAQ'
        )
        await call.message.answer_media_group(
            media=album_builder.build()
        )

    elif call.data == 'audience-3':
        answer = """
        <b>Лаборатория искусстевнного интеллекта и математического моделирования IT-8</b>
        
Алан Тьюринг, выдающийся ученый и пионер в области информатики, оказал значительное влияние на мировую науку и технологии. Его работа в области вычислительной математики и искусственного интеллекта стала отправной точкой для многих инноваций. Вдохновленные его наследием, мы создали уникальную лабораторию математического моделирования в нашем университете. Эта лаборатория, названная в его честь, призвана продолжить его наследие и стать центром развития математического моделирования в различных областях.

Здесь студенты и преподаватели МАИ воплощают свои идеи в жизнь, работая над уникальными проектами. Одним из таких проектов является "Сбер Паводки". Этот проект представляет собой сотрудничество с ведущей финансовой компанией Сбер и направлен на моделирование поведения реки Амур и реки Зея в период паводков с использованием методов машинного обучения.

"Сбер Паводки" - это не только применение передовых технологий в прогнозировании природных явлений, но и важный шаг в развитии сотрудничества между образовательными учреждениями и бизнесом. Этот проект демонстрирует, как совместные усилия ученых и предпринимателей могут привести к созданию инновационных решений, способных решать реальные проблемы.
"""
        mrkp = get_keyboard_nav(int(call.data.split('-')[1]))
        config.VIEW_DATA[call.from_user.username]['audience-3'] = True
        answer_video_note = 'DQACAgIAAxkBAAIDDmW0ZO6R_-Biuvm0xwUu2hm517jaAAK4OAACyJ-oSVfx3KFomKNSNAQ'


    elif call.data == 'audience-4':
        answer = """
        Цикл работ "Люди и роботы" был создан в ответ на появление нейрогенеративной модели Stable Diffusion, как проект по исследованию генеративных возможностей нейросети и её "внутреннего мира". В результате тщательно подобранных промптов и последующего отбора работ был создан цикл изображений, в различных художественных стилях и жанрах, показывающих видение сетью человека и робота. Вглядываясь в них мы размышляем на тему "а что же делает нас людьми, и что делает роботов - роботами". Ответ на этот вопрос не всегда очевиден...

Использованные средства: нейросеть Stable Diffusion 1.3, Latent Diffusion Super-Resolution 4x, минимальное ручное ретуширование, печать на холсте.

Посетите <a href='https://soshnikov.com/museum/'>виртуальный музей</a> Дмитрия Валерьевича Сошникова.
        """
        mrkp = get_keyboard_nav(int(call.data.split('-')[1]))
        config.VIEW_DATA[call.from_user.username]['audience-4'] = True
        answer_video_note = 'DQACAgIAAxkBAAIDCmW0ZMOk5QNCRV-7LcgW0De_-g07AAK0OAACyJ-oSZgSySki_KOeNAQ'


    elif call.data == 'audience-5':
        answer = """
        <b>Студентческая лаборатория IT-9 Лямбда</b>
Сейчас IT-9 - это лаборатория машинного обучения, основанная и управляемая студентами Института №8. Этот инновационный проект создан для того, чтобы предоставить студентам возможность воплотить свои идеи в области искусственного интеллекта и машинного обучения в жизнь. Среди их выдающихся проектов наиболее заметными являются "Контур" и "AI-Space".

"Контур" - это решение в области компьютерного зрения, разработанное студентами лаборатории. Эта система позволяет мониторить территорию МАИ и распознавать различные виды нарушений. Среди этих нарушений могут быть драки, проникновение на запрещенную территорию, нарушение правил парковки и многое другое. "Контур" не только обеспечивает безопасность на территории университета, но и помогает эффективно реагировать на возможные инциденты.

"AI-Space" - это облачное решение, представленное лабораторией. Эта платформа предоставляет студентам возможность обучать модели машинного обучения на наших суперкомпьютерах: Шелдон, Красный и Синий ящики. Это уникальное преимущество, которым не могут похвастаться многие IT-компании. Использование мощных вычислительных ресурсов университета позволяет студентам решать сложные задачи в области искусственного интеллекта и машинного обучения, делая проекты лаборатории еще более перспективными и значимыми.
        """
        mrkp = get_keyboard_nav(int(call.data.split('-')[1]))
        config.VIEW_DATA[call.from_user.username]['audience-5'] = True
        answer_video_note = 'DQACAgIAAxkBAAIDEmW0ZRZE1C4ZN4NeZ9JEdHY-sMvwAAK8OAACyJ-oSTjL3_g1MSaMNAQ'

    elif call.data == 'audience-6':
        answer = """
        <b>Центр олимпиадного программирования</b>
МАИ входит в топ 5 ВУЗов, на ряду с МГУ и ВШЭ, где есть площадки Яндекс Лицея, обучаясь именно в МАИ у школьников есть возможность представить себя студентом-маёвцем и подумать о будущем поступлении. Открытие новой образовательной площадки вызвало большой интерес, за две недели набора учащихся поступило более 100 заявок, а конкурс составил 3 человека на место.

А узнать про олимпиадное программирование из первых уст и кто такой ZZZ можно <a href='https://www.youtube.com/watch?v=RJ-WUgsIvQQ&embeds_referring_euri=https%3A%2F%2Fvk.com%2F&embeds_referring_origin=https%3A%2F%2Fvk.com&source_ve_path=MjM4NTE&feature=emb_title&ab_channel=IT-%D1%86%D0%B5%D0%BD%D1%82%D1%80%D0%9C%D0%90%D0%98'>в нашем подкасте</a>.
        """
        mrkp = get_keyboard_nav(int(call.data.split('-')[1]))
        config.VIEW_DATA[call.from_user.username]['audience-6'] = True
        answer_video_note = 'DQACAgIAAxkBAAIE1GW0wbpml5dqT9vRQMUzhxsnFZcsAAJBQgACIWigSVF4ucp3Ya_KNAQ'


    elif call.data == 'audience-7':
        answer = """
        Именно сегодня тут будет ждать тебя маскот Института №8 - робособака Дора.
        """
        album_builder = MediaGroupBuilder(caption='Сердце Восьмерки')
        album_builder.add_photo(
            media='AgACAgIAAxkBAAIFdGW0yFEnhVqOQyNu02eAtCf1svZlAAIL1zEbPkioSQb6zGmxI_mzAQADAgADeQADNAQ'
        )
        await call.message.answer_media_group(
            media=album_builder.build()
        )
        mrkp = get_keyboard_nav(int(call.data.split('-')[1]))
        config.VIEW_DATA[call.from_user.username]['audience-7'] = True
        answer_video_note = 'DQACAgIAAxkBAAIDCGW0ZKakyAPJSyoNqrxI_yOqUqO4AAKyOAACyJ-oSRyeFJ6XAU--NAQ'


    elif call.data == 'audience-8':
        answer = """
        Сотрудничество 8 института МАИ с ведущими IT-компаниями, такими как Yandex, VK, SBER, Cloud, IVI, МТС, билайн, Лаборатория Касперского, открывает студентам широкие возможности для профессионального роста. Студенты получают доступ к стажировкам, совместным проектам и обучающим курсам, что дает им ценный опыт работы в индустрии информационных технологий. Онлайн магистратура, организованная совместно с Сбером, обеспечивает студентам высококачественное образование, соответствующее современным требованиям рынка, и способствует их профессиональному развитию.
        """
        mrkp = get_keyboard_nav(int(call.data.split('-')[1]))
        config.VIEW_DATA[call.from_user.username]['audience-8'] = True
        answer_video_note = 'DQACAgIAAxkBAAIFMGW0xmzAyTogHEROD5qj4_7HJTCgAAJHQgACIWigSVvDoMYV6ubHNAQ'


    elif call.data == 'audience-9':
        answer = """
        Мы можем отметить, что у нас на кафедре есть несколько серверных, каждая из них выполняет свою функцию. Например, за этой красивой "стенкой" не такая открытая и прозрачная, как другие серверные, которые у нас есть. Это потому, что там находится дисковое хранилище - наша система хранения данных, где хранятся все данные по проектам, закрытые. Поэтому необходимо, чтобы она была за кирпичной стеной, так как жесткие диски шумят, и нужно охлаждение.
        
Наши студенты занимаются на современном оборудовании, всем хватает компов, они мощные, с мощными видеокартами и ребята учатся на IT-этаже прямо с первого курса. На этаже также присутствуют маленькие уютные местечки, чтобы сесть, поработать, поговорить с преподавателем.
        """
        mrkp = get_keyboard_nav(int(call.data.split('-')[1]))
        config.VIEW_DATA[call.from_user.username]['audience-9'] = True
        answer_video_note = 'DQACAgIAAxkBAAIDBmW0ZI9HwdpLimBea6BjFKNWbGc0AAKwOAACyJ-oSYixdJ7e-qX6NAQ'
    elif call.data.startswith('page_aud'):
        answer = navigator
        mrkp = get_keyboard_all_audience(int(call.data.split('-')[1]))
        is_edit = True
    elif call.data == 'all_audience':
        answer = navigator
        mrkp = get_keyboard_all_audience(0)
    elif call.data == 'main':
        answer = ("""
        Сегодня у нас день открытых дверей, так что держи расписание на сегодняшний день. Не забудь заглянуть на какие-нибудь классные мероприятия, которые тебе нравятся. 
        
Присоединяйся к нашему <a href="https://t.me/pk8mai">телеграм-чату абитуриентов 2024</a>""")
        answer_photo = config.TG_ID_SCHEDULE
        mrkp = get_keyboard_main()
    elif call.data == 'contact':
        answer = """
Присоединяйся к нашему <a href="https://t.me/pk8mai">телеграм-чату абитуриентов 2024</a> и группе в <a href="https://vk.com/postupi8">ВК</a> для новостей и обсуждений. Также зацени наш канал <a href="https://t.me/itcmai">IT-центра МАИ</a> для последних трендов в мире IT! 💬✨
        
Готов окунуться в мир компьютерных наук и математики? Тогда давай начнем это путешествие вместе! 🚀
        """
        mrkp = get_keyboard_contact()

    if answer_photo:
        await call.message.answer_photo(caption=answer,
                                        photo=answer_photo,
                                        reply_markup=mrkp)
    elif answer_video:
        await call.message.answer_video(caption=answer,
                                        video=answer_video,
                                        reply_markup=mrkp)
    elif answer_video_note:
        await call.message.answer_video_note(video_note=answer_video_note)
        await call.message.answer(answer, reply_markup=mrkp)

    elif is_edit:
        await call.message.edit_text(answer, reply_markup=mrkp, parse_mode=ParseMode.HTML)
    else:
        await call.message.answer(answer, reply_markup=mrkp, parse_mode=ParseMode.HTML)
    await call.answer()
