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

def search_wikipedia(driver, query):
    search_box = driver.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Ждем загрузки страницы

def list_paragraphs(driver):
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for i, para in enumerate(paragraphs):
        print(f"Paragraph {i+1}: {para.text[:200]}...")  # Выводим первые 200 символов
        if (i + 1) % 5 == 0:  # Показываем по 5 параграфов за раз
            cont = input("Показать ещё 5 параграфов? (y/n): ")
            if cont.lower() != 'y':
                break

def list_internal_links(driver, query):
    # # Находим все элементы ссылок (`<a>`) внутри элемента с ID `mw-content-text`
    # links = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text a")
    #
    # internal_links = []
    # for link in links:
    #     # Проверка атрибута `href`
    #     href = link.get_attribute('href')
    #     # Для каждой найденной ссылки сначала получаем значение атрибута `href`.
    #     # Если `href` не равно `None` и начинается с "https://ru.wikipedia.org/wiki/",
    #     # добавляем ссылку в список `internal_links`
    #     if href and href.startswith(query):
    #         internal_links.append(link)
    #
    # for i, link in enumerate(internal_links):
    #     print(f"{i + 1}: {link.text} - {link.get_attribute('href')}")
    # return internal_links
    hatnotes = []
    for element in driver.find_elements(By.TAG_NAME, 'div'):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)
    return hatnotes
def main():
    driver = webdriver.Firefox()
    driver.get("https://www.wikipedia.org/")

    query = input("Введите ваш запрос: ")
    search_wikipedia(driver, query)

    while True:
        print("Выберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Ваш выбор: ")

        if choice == '1':
            list_paragraphs(driver)
        elif choice == '2':
            internal_links = list_internal_links(driver, query)
            # internal_links = list_internal_links(driver)
            if len(internal_links) == 0:
                print("На этой странице нет внутренних статей")
            else:
                link = random.choice(internal_links)
                print(link)
                # driver.get(link.get_attribute('href'))
                driver.get(link)
            # print(internal_links)
            # link_choice = int(input("Введите номер ссылки для перехода: ")) - 1
            # if 0 <= link_choice < len(internal_links):
            #     driver.get(internal_links[link_choice].get_attribute('href'))
                while True:
                    print("Выберите действие:")
                    print("1. Листать параграфы текущей статьи")
                    print("2. Перейти на одну из внутренних статей")
                    print("3. Вернуться к предыдущему меню")
                    sub_choice = input("Ваш выбор: ")

                    if sub_choice == '1':
                        list_paragraphs(driver)
                    elif sub_choice == '2':
                        internal_links = list_internal_links(driver, query)
                        if len(internal_links) == 0:
                            print("На этой странице нет внутренних статей")
                        else:
                            link = random.choice(internal_links)
                            driver.get(link)
                        # link_choice = int(input("Введите номер ссылки для перехода: ")) - 1
                        # if 0 <= link_choice < len(internal_links):
                        #     driver.get(internal_links[link_choice].get_attribute('href'))
                        # else:
                        #     print("Неверный выбор")
                    elif sub_choice == '3':
                        break
                    else:
                        print("Неверный выбор")
        elif choice == '3':
            break
        else:
            print("Неверный выбор")

    driver.quit()

if __name__ == "__main__":
    main()
