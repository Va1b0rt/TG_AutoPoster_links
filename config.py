TOKEN = ''  # Токен Telegram бота
COUNT = ''  # Число последних записей группы
TOKEN_VK = ''  # Токен авторизации ВК
GROUP_1 = ''  # Ссыка на группу ВК (Например, https://vk.com/test123, значит GROUP_1 = 'test123')
URL_VK_1 = 'https://api.vk.com/method/wall.get?domain=' + GROUP_1 + '&v=5.71&count=' + COUNT + '&filter=owner&access_token=' + TOKEN_VK
CHAT_ID_1 = ''  # Ссылка на канал/супергруппу или ID пользователя Telegram
FILENAME_VK_1 = 'last_known_id_1.txt'  # Файл для сохранения ID последнего отправленного поста. Для каждой группы используется отдельный файл.
BASE_VIDEO_URL = 'https://vk.com/video'  # Базовая ссылка для обработки видео
URLS = {URL_VK_1: (GROUP_1, FILENAME_VK_1, CHAT_ID_1)}  # Словарь со значинями выше. Может быть расширен для работы несколькими группами ВК.