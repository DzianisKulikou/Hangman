from random import choice

word_list = ['снижение', 'услуга', 'рынок', 'половина', 'сила', 'коллектив', 'множество', 'бизнес', 'команда',
             'запись', 'заказ', 'путь', 'сказка', 'продажа', 'колено', 'образец', 'стул', 'библиотека', 'птица',
             'гражданин', 'разница', 'раз', 'море', 'взгляд', 'идея', 'больница', 'философия', 'наука', 'серия',
             'сущность', 'удовольствие', 'понятие', 'свидетель', 'пост', 'миллион', 'утро', 'метр', 'собственность',
             'песня', 'поле', 'звонок', 'ожидание', 'парк', 'корпус', 'зуб', 'обстановка', 'растение', 'заключение',
             'обучение', 'совет', 'величина', 'ключ', 'трубка', 'бумага', 'дух', 'забота', 'камера', 'диван', 'водка',
             'тюрьма', 'сознание', 'поворот', 'вариант', 'время', 'целое', 'защита', 'генерал', 'доллар', 'звезда',
             'признак', 'колесо', 'председатель', 'хлеб', 'учреждение', 'музей', 'тенденция', 'специалист', 'модель',
             'член', 'бутылка', 'кулак', 'выпуск', 'замок', 'доктор', 'сезон', 'секретарь', 'возраст', 'студент',
             'фонд', 'мальчик', 'хозяйство', 'граница', 'цифра', 'мощность', 'болезнь', 'вершина', 'литература',
             'водитель', 'остаток', 'вино', 'банк', 'сведение', 'пол', 'господин', 'отношение', 'предмет', 'фраза',
             'книга', 'порог', 'класс', 'изменение', 'пыль', 'октябрь', 'куст', 'компьютер', 'выборы', 'масштаб',
             'жизнь', 'запах', 'течение', 'кость', 'метод', 'глубина', 'зона', 'двор', 'эксперимент', 'женщина',
             'доска', 'интерес', 'ноябрь', 'черт', 'энергия', 'компания', 'субъект', 'причина', 'тон', 'человечество',
             'одежда', 'вещь', 'ракета', 'зал', 'передача', 'помещение', 'сердце', 'характеристика', 'описание',
             'ручка', 'сутки', 'вес', 'параметр', 'производитель', 'тетя', 'тип', 'указание', 'платье', 'момент',
             'контакт', 'толпа', 'гора', 'очки', 'армия', 'старик', 'ребенок', 'родина', 'спектакль', 'природа',
             'результат', 'оборона', 'влияние', 'январь', 'закон', 'стол', 'воля', 'воздействие', 'факт', 'мечта',
             'мешок', 'судьба', 'смена', 'рабочий', 'выход', 'ученый', 'реформа', 'фигура', 'карта', 'мастер', 'удар',
             'конференция', 'губернатор', 'честь', 'бок', 'почва', 'должность', 'база', 'костюм', 'надежда', 'подъезд',
             'позиция', 'условие', 'час', 'адрес', 'группа', 'солнце', 'потребность', 'набор', 'капитан', 'нос',
             'заместитель', 'представление', 'воспоминание', 'бог', 'налог', 'ресурс', 'добро', 'мужик', 'зрение',
             'формула', 'данные', 'просьба', 'самолет', 'процедура', 'милиция', 'ответственность', 'баба', 'область',
             'выставка', 'начальство', 'телевизор', 'беда', 'техника', 'рисунок', 'подарок', 'правда', 'корень',
             'число', 'крыло', 'свобода', 'работник', 'мысль', 'слух', 'расчет', 'двигатель', 'декабрь', 'помощь',
             'кресло', 'воздух', 'скорость', 'повод', 'знакомый', 'производство', 'инженер', 'поселок', 'недостаток',
             'помощник', 'министр', 'создание', 'небо', 'танк', 'поток', 'конкурс', 'ум', 'работа', 'постановление',
             'угол', 'предложение', 'завод', 'секунда', 'обязанность', 'достоинство', 'вирус', 'хозяйка', 'монастырь',
             'сеть', 'рассмотрение', 'объединение', 'кожа', 'контроль', 'коммунист', 'администрация', 'организм',
             'стена', 'технология', 'точка', 'редакция', 'встреча', 'черта', 'средство', 'объяснение', 'отдел',
             'практика', 'торговля', 'огонь', 'площадка', 'инструмент', 'миг', 'направление', 'смех', 'обязательство',
             'рубеж', 'беседа', 'основа', 'дурак', 'эффект', 'шаг', 'доклад', 'операция', 'кофе', 'выражение',
             'автобус', 'известие', 'личность', 'фронт', 'отрасль', 'территория', 'память', 'радость', 'рождение',
             'акция', 'война', 'сотрудничество', 'ужас', 'поэт', 'атмосфера', 'цвет', 'пиво', 'способность', 'боль',
             'край', 'живот', 'характер', 'рост', 'политика', 'поведение', 'будущее', 'внимание', 'образ', 'рот',
             'дождь', 'лоб', 'машина', 'заявление', 'комиссия', 'революция', 'март', 'кино', 'движение', 'сад',
             'федерация', 'категория', 'реклама', 'обед', 'лист', 'этап', 'суд', 'партия', 'впечатление', 'воспитание',
             'нога', 'ладонь', 'способ', 'папа', 'проект', 'труд', 'кухня', 'дворец', 'минута', 'река', 'записка',
             'дед', 'событие', 'творчество', 'телефон', 'тайна', 'кризис', 'структура', 'лестница', 'окно', 'сцена',
             'церковь', 'господь', 'возможность', 'собрание', 'эффективность', 'обстоятельство', 'поезд', 'оружие',
             'слава', 'книжка', 'участник', 'противник', 'пункт', 'отличие', 'сумка', 'суть', 'размер', 'приказ',
             'ухо', 'сумма', 'товарищ', 'кодекс', 'ряд', 'вопрос', 'сон', 'исследование', 'восторг', 'пьеса', 'крыша',
             'ученик', 'частность', 'сын', 'традиция', 'неделя', 'сестра', 'кредит', 'приятель', 'схема', 'царь',
             'союз', 'коридор', 'свет', 'статус', 'эксперт', 'сигнал', 'пистолет', 'округ', 'дверь', 'исключение',
             'вид', 'фотография', 'сотрудник', 'печать', 'писатель', 'ветер', 'дядя', 'ребята', 'пора', 'молоко',
             'шум', 'ход', 'офицер', 'общение', 'крик', 'профессор', 'родственник', 'потеря', 'взаимодействие',
             'дочка', 'часы', 'роль', 'русский', 'год', 'волна', 'элемент', 'дочь', 'коллега', 'художник', 'сравнение',
             'нож', 'существо', 'девушка', 'сентябрь', 'вывод', 'кольцо', 'десяток', 'ошибка', 'подход', 'президент',
             'мера', 'открытие', 'источник', 'герой', 'курс', 'имущество', 'площадь', 'бабушка', 'дым', 'требование',
             'мама', 'фамилия', 'власть', 'применение', 'корабль', 'учитель', 'дело', 'жена', 'рыба', 'польза',
             'договор', 'мероприятие', 'глава', 'деталь', 'смысл', 'наблюдение', 'количество', 'предприятие', 'снег',
             'хозяин', 'совесть', 'пакет', 'вкус', 'майор', 'достижение', 'отдых', 'теория', 'страна', 'народ',
             'конфликт', 'памятник', 'премия', 'психология', 'кровь', 'реализация', 'клетка', 'регион', 'университет',
             'концепция', 'ценность', 'голос', 'повышение', 'итог', 'стоимость', 'список', 'линия', 'шутка', 'масло',
             'войско', 'картина', 'часть', 'танец', 'житель', 'рука', 'здоровье', 'карман', 'проведение', 'рубль',
             'гостиница', 'театр', 'буква', 'темнота', 'плата', 'ресторан', 'единица', 'детство', 'убийство',
             'редактор', 'мужчина', 'взрыв', 'форма', 'палата', 'игра', 'поиск', 'поездка', 'здание', 'урок', 'высота',
             'сфера', 'лето', 'поддержка', 'поколение', 'информация', 'связь', 'версия', 'ворота', 'комната', 'весна',
             'берег', 'переговоры', 'лошадь', 'цветок', 'цель', 'артист', 'принятие', 'страница', 'страх', 'ставка',
             'большинство', 'магазин', 'министерство', 'краска', 'выступление', 'давление', 'вечер', 'занятие',
             'опасность', 'произведение', 'деревня', 'шея', 'товар', 'поверхность', 'жертва', 'деятельность',
             'испытание', 'клуб', 'пенсия', 'блок', 'усилие', 'гость', 'расход', 'фактор', 'проблема', 'статья',
             'фирма', 'руководитель', 'улыбка', 'штаб', 'комплекс', 'пара', 'анализ', 'парень', 'журналист',
             'разработка', 'судья', 'плечо', 'начальник', 'изучение', 'профессия', 'правило', 'автомобиль', 'успех',
             'объем', 'животное', 'зеркало', 'выполнение', 'автомат', 'организация', 'зима', 'имя', 'музыка', 'тень',
             'отказ', 'вещество', 'храм', 'семья', 'место', 'степень', 'зарплата', 'отсутствие', 'знание', 'центр',
             'след', 'нефть', 'лед', 'строительство', 'основание', 'родитель', 'правительство', 'установка',
             'разрешение', 'название', 'стекло', 'квартира', 'законодательство', 'сторона', 'изображение', 'вагон',
             'развитие', 'директор', 'село', 'окончание', 'назначение', 'рамка', 'том', 'соединение', 'мясо', 'газета',
             'масса', 'предел', 'задача', 'мозг', 'билет', 'столик', 'очередь', 'обращение', 'среда', 'определение',
             'преступление', 'право', 'руководство', 'соглашение', 'лейтенант', 'прошлое', 'главное', 'программа',
             'перевод', 'дача', 'новость', 'режим', 'молодежь', 'канал', 'озеро', 'вход', 'промышленность', 'выбор',
             'улица', 'июнь', 'общество', 'зависимость', 'лагерь', 'дыхание', 'текст', 'угроза', 'показатель', 'звук',
             'еврей', 'увеличение', 'депутат', 'спорт', 'месяц', 'лес', 'золото', 'перспектива', 'ящик', 'красота',
             'затрата', 'следователь', 'сигарета', 'последствие', 'рассказ', 'ощущение', 'строй', 'бой', 'возвращение',
             'нарушение', 'муж', 'сообщение', 'фильм', 'победа', 'этаж', 'подразделение', 'объект', 'система',
             'читатель', 'уровень', 'труба', 'деньги', 'командир', 'активность', 'продукт', 'стиль', 'счет', 'род',
             'состояние', 'смерть', 'препарат', 'ситуация', 'чай', 'режиссер', 'транспорт', 'норма', 'публика', 'июль',
             'газ', 'слеза', 'знак', 'чудо', 'тысяча', 'горло', 'участие', 'аппарат', 'температура', 'километр',
             'кандидат', 'партнер', 'процесс', 'отец', 'глаз', 'спина', 'охрана', 'сомнение', 'остров', 'случай',
             'речь', 'расстояние', 'счастье', 'шанс', 'прием', 'автор', 'истина', 'следствие', 'период',
             'доказательство', 'подготовка', 'душа', 'праздник', 'срок', 'заседание', 'немец', 'брат', 'начало',
             'кабинет', 'апрель', 'москвич', 'конец', 'бюджет', 'князь', 'яблоко', 'мальчишка', 'история', 'сбор',
             'язык', 'присутствие', 'доход', 'тело', 'поэзия', 'журнал', 'февраль', 'борьба', 'король', 'август',
             'дружба', 'осень', 'получение', 'механизм', 'любовь', 'покупатель', 'явление', 'таблица', 'школа',
             'длина', 'порядок', 'старуха', 'штука', 'продукция', 'дама', 'лицо', 'человек', 'функция', 'отделение',
             'собака', 'жилье', 'песок', 'щека', 'круг', 'материал', 'процент', 'признание', 'город', 'номер', 'хвост',
             'строка', 'кровать', 'мгновение', 'фон', 'вода', 'постель', 'американец', 'риск', 'государство', 'дно',
             'зло', 'разговор', 'орган', 'ночь', 'мост', 'еда', 'желание', 'дума', 'капитал', 'тема', 'дорога', 'штат',
             'полковник', 'значение', 'слово', 'стихи', 'кадр', 'долг', 'основное', 'республика', 'полет', 'чтение',
             'мир', 'прокурор', 'действие', 'культура', 'акт', 'документ', 'пример', 'дом', 'сотня', 'кусок',
             'середина', 'управление', 'полоса', 'реакция', 'девочка', 'портрет', 'проверка', 'комитет',
             'существование', 'страсть', 'запас', 'мать', 'качество', 'настроение', 'грудь', 'лидер', 'обеспечение',
             'уход', 'камень', 'план', 'учет', 'крест', 'солдат', 'сюжет', 'положение', 'столица', 'талант',
             'содержание', 'конструкция', 'состав', 'ответ', 'формирование', 'актер', 'лев', 'грех', 'спор',
             'владелец', 'тишина', 'инициатива', 'решение', 'зритель', 'вера', 'станция', 'враг', 'участок', 'металл',
             'появление', 'волос', 'принцип', 'концерт', 'оборудование', 'оплата', 'день', 'экран', 'район',
             'использование', 'действительность', 'сожаление', 'оценка', 'губа', 'ремонт', 'слой', 'сделка',
             'экономика', 'покой', 'вина', 'образование', 'цена', 'лодка', 'особенность', 'больной', 'роман',
             'необходимость', 'палец', 'искусство', 'брак', 'наличие', 'эпоха', 'сосед', 'стакан', 'понимание',
             'подруга', 'запад', 'академия', 'безопасность', 'свойство', 'век', 'чиновник', 'население', 'служба',
             'голова', 'эксплуатация', 'издание', 'устройство', 'чувство', 'врач', 'попытка', 'пространство',
             'восток', 'друг', 'клиент', 'представитель', 'сочинение', 'письмо', 'сапог', 'переход', 'земля', 'трава',
             'опыт', 'удивление', 'потолок', 'реальность', 'дерево', 'май', 'мнение', 'соответствие', 'институт',
             'исполнение', 'доля']


def get_word():
    return choice(word_list).upper()


def display_hangman(tries):
    stages = [
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]