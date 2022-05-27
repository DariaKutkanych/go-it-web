from prettytable.colortable import ColorTable, Themes


class Menu:

    @property
    def main_menu(self):
        show_menu = ColorTable(theme=Themes.OCEAN)
        show_menu.field_names = [f"{18 * '-'}Меню{18 * '-'}"]
        show_menu.hrules = 1
        show_menu.align = "l"
        show_menu.add_rows([["1. Контакти"],
                            ["2. Нотатки"],
                            ["3. Іменниники"],
                            ["4. Сортувати папку"],
                            ["5. Зберегти дані"],
                            ["6. Завантажити дані"],
                            ["7. Вихід"],
                            ])
        return show_menu

    @property
    def main_contact(self):
        show_main_contact = ColorTable(theme=Themes.OCEAN)
        show_main_contact.field_names = [f"{18 * '-'}Контакти{18 * '-'}"]
        show_main_contact.hrules = 1
        show_main_contact.align = "l"
        show_main_contact.add_rows([["1. Створити контакт"],
                                    ["2. Добавити дані до існуючого контакту"],
                                    ["3. Редагувати дані контакту"],
                                    ["4. Видалити дані з контакту"],
                                    ["5. Пошук контакту"],
                                    ["6. Вивести всі контакти"],
                                    ["7. Повернутись в попереднє меню"]])

        return show_main_contact

    @property
    def edit_menu(self):
        show_edit = ColorTable(theme=Themes.OCEAN)
        show_edit.field_names = [f"{18 * '-'}За яким критерієм?{18 * '-'}"]
        show_edit.hrules = 1
        show_edit.align = "l"
        show_edit.add_rows([["1. Телефон"],
                            ["2. Емейл"],
                            ["3. Адресу"],
                            ["4. День народження"],
                            ["5. Повернутись в попереднє меню"]])
        return show_edit

    @property
    def notes_menu(self):
        show_notes_menu = ColorTable(theme=Themes.OCEAN)
        show_notes_menu.field_names = [f"{18 * '-'}Нотатки{18 * '-'}"]
        show_notes_menu.hrules = 1
        show_notes_menu.align = "l"
        show_notes_menu.add_rows([["1. Подивитись всі нотатки"],
                                  ["2. Додати нотатку"],
                                  ["3. Знайти нотатку"],
                                  ["4. Змінити нотатку"],
                                  ["5. Видалити нотатку"],
                                  ["6. Сортувати нотатки за тегами"],
                                  ["7. Повернутись в попереднє меню"]])
        return show_notes_menu

    @property
    def search_note(self):
        show_search = ColorTable(theme=Themes.OCEAN)
        show_search.field_names = [f"{18 * '-'}За яким критерієм будемо шукати?"
                                   f"{18 * '-'}"]
        show_search.hrules = 1
        show_search.align = "l"
        show_search.add_rows([["1. По id замітки"],
                              ["2. По тегу замітки"],
                              ["3. По головному слову"],
                              ["4. Повернутись в попереднє меню"]])
        return show_search

    @property
    def edit_note(self):
        show_search = ColorTable(theme=Themes.OCEAN)
        show_search.field_names = [f"{18 * '-'}Що будемо змінювати?"
                                   f"{18 * '-'}"]
        show_search.hrules = 1
        show_search.align = "l"
        show_search.add_rows([["1. Тег замітки"],
                              ["2. Замітку"],
                              ["3. Повернутись в попереднє меню"]])
        return show_search
