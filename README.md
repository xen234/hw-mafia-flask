# hw-mafia-flask
HW-4 Added frontend on flask for mafia game

## Запуск 
```
docker-compose up --build
```
В контейнеры завернуты grpc сервер, api, rq-worker и redis сервер.

Далее запускается клиент из консоли, создаете юзеров/комнату в игре и по адресам просматривается информация пользователей

## Структура проекта
Обновленная версия проекта с добавлением front-end на flask

Пути, по которым доступны команды:
1. Домашняя страница
```
 /
```
2. Отдельный показ аватарки юзера в заданной игровой комнате
```
 /<room_name>/<user>/avatar
```
3. Изменение аватара юзера в заданной игровой комнате
```
 /set_avatar/<room_name>/<username>
```
4. Изменение параметров профиля юзера
```
 /change/<room_name>/<user_id>
```
5. Просмотр профилей всех пользователей в определенной комнате
```
 /user/<room_id>
```
6. Просмотр профиля определенного юзера
```
 /user/<room_id>/<user_id>
```
7. Генерация PDF-файла

Команды ниже создают задачу, и по мере ее выполнения возвращают job_id или ссылку на пдф документ. При переходе по ссылке загрузка должна начаться автоматически. Пример сгеренированного документа в папке static.
```
curl -X POST http://127.0.0.1:3001/<room_id>/<user_id>/generate_pdf
curl http://127.0.0.1:3001/jobs/<job_id>
```
