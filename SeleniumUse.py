"""
Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
1. Спрашивать у пользователя первоначальный запрос.
2. Переходить по первоначальному запросу в Википедии.
3. Предлагать пользователю три варианта действий:
    3.1 листать параграфы текущей статьи;
    3.2 перейти на одну из связанных страниц — и снова выбор из двух пунктов:
        - листать параграфы статьи;
        - перейти на одну из внутренних статей.
    3.3 выйти из программы.
"""

from selenium import webdriver
from selenium.webdriver import Keys     # Взаимодействие с клавиатурой
from selenium.webdriver.common.by import By     # Для поиска элементов на странице через DOM
import time
import random


print("Эта программа просит пользователя ввести начальный запрос "
      "по которому осуществит поиск в Википедии\n")

# find_string = input("Введите свой запрос к Википедии: ")    # Строка для поиска
find_string = 'Солнце'
driver = webdriver.Firefox()
# Открываем страницу Википедии
# driver.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
driver.get('https://ru.wikipedia.org/wiki/%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C')
# search_element = driver.find_element(By.ID, 'searchInput')      # Позиционируемся в поле "Искать в Википедии"
# search_element.send_keys(find_string)    # Подставляем строку поиска в поле поиска
# search_element.send_keys(Keys.RETURN)    # Имитируем нажатие клавиши ENTER
time.sleep(10)
# Получаем HTML-код страницы
web_page = driver.current_url
print(web_page)
print("!")
def get_wikipedia_links(driver, url):
      # Ищем связанные страницы
      # Находим все элементы <a> с href
    # links = driver.find_elements(By.CSS_SELECTOR, "ul > li > a")
    links = driver.find_elements(By.CSS_SELECTOR, "a")

      # Создаём список со связанными страницами
    links_list = []
    count = 1

    for link in links:
        title = link.get_attribute('title')
        href = link.get_attribute('href')
        links_list.append((title, href))

        # href = link.get_attribute('href')
        #
        # if href and href.startswith(url) and ':' not in href:
        #     print(href.title)
        #     input()
        #     link_pages[count] = href
        #     count += 1
    print(links_list)
    return links_list

def get_wikipedia_paragraph(driver):
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input()


# link_pages = get_wikipedia_links(driver, web_page)
# print(link_pages[0])

paragraphs_print = get_wikipedia_paragraph(driver)

# for key, value in link_pages.items():
#     print(f"{key}: {value}")
# print(link_pages)
# def search_wikipedia(driver, query):
#     search_box = driver.find_element(By.NAME, "search")
#     search_box.clear()
#     search_box.send_keys(query)
#     search_box.send_keys(Keys.RETURN)
#     time.sleep(2)  # Ждем загрузки страницы
#
# def list_paragraphs(driver):
#     paragraphs = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text p")
#     for i, para in enumerate(paragraphs):
#         print(f"Paragraph {i+1}: {para.text[:200]}...")  # Выводим первые 200 символов
#         if (i + 1) % 5 == 0:  # Показываем по 5 параграфов за раз
#             cont = input("Показать ещё 5 параграфов? (y/n): ")
#             if cont.lower() != 'y':
#                 break
#
# def list_internal_links(driver):
#     links = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text a")
#     internal_links = [link for link in links if link.get_attribute('href').startswith("https://ru.wikipedia.org/wiki/")]
#     for i, link in enumerate(internal_links):
#         print(f"{i+1}: {link.text} - {link.get_attribute('href')}")
#     return internal_links
#
# def main():
#     # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver = webdriver.Firefox()
#     driver.get("https://www.wikipedia.org/")
#
#     query = input("Введите ваш запрос: ")
#     search_wikipedia(driver, query)
#
#     while True:
#         print("Выберите действие:")
#         print("1. Листать параграфы текущей статьи")
#         print("2. Перейти на одну из связанных страниц")
#         print("3. Выйти из программы")
#         choice = input("Ваш выбор: ")
#
#         if choice == '1':
#             list_paragraphs(driver)
#         elif choice == '2':
#             internal_links = list_internal_links(driver)
#             link_choice = int(input("Введите номер ссылки для перехода: ")) - 1
#             if 0 <= link_choice < len(internal_links):
#                 driver.get(internal_links[link_choice].get_attribute('href'))
#                 while True:
#                     print("Выберите действие:")
#                     print("1. Листать параграфы текущей статьи")
#                     print("2. Перейти на одну из внутренних статей")
#                     print("3. Вернуться к предыдущему меню")
#                     sub_choice = input("Ваш выбор: ")
#
#                     if sub_choice == '1':
#                         list_paragraphs(driver)
#                     elif sub_choice == '2':
#                         internal_links = list_internal_links(driver)
#                         link_choice = int(input("Введите номер ссылки для перехода: ")) - 1
#                         if 0 <= link_choice < len(internal_links):
#                             driver.get(internal_links[link_choice].get_attribute('href'))
#                         else:
#                             print("Неверный выбор")
#                     elif sub_choice == '3':
#                         break
#                     else:
#                         print("Неверный выбор")
#         elif choice == '3':
#             break
#         else:
#             print("Неверный выбор")
#
#     driver.quit()
#
# if __name__ == "__main__":
#     main()
