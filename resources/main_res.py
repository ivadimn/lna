from collections import namedtuple


Event = namedtuple("Event", ["icon", "title", "status_tip"])

main_res = {
    "RP_EVENT" : Event("images/table.png", "Разделы персонала", "Посмотреть разделы персонала"),
    "OS_EVENT" : Event("images/tree.png", "Орг. структура", "Посмотреть организационную структуру"),
}

rp_res = {
    "HEADERS": ["Ид.", "Наименование", "Организация"],
    "ADD_EVENT": Event("images/database-insert.png", "Добавить", "Создать новый раздел персонала"),
    "EDIT_EVENT": Event("images/edit.png", "Изменить", "Изменить раздел персонала"),
    "DELETE_EVENT": Event("images/database-delete.png", "Удалить", "Удалить раздел персонала"),
}
