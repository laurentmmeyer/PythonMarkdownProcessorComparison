# adb

> Android Debug Bridge: управление запущенным эмулятором Android или подключенным устройством Android.
> Некоторые подкоманды, такие как `adb shell`, имеют собственную документацию по использованию.
> Больше информации: <https://developer.android.com/studio/command-line/adb>.

- Проверить, запущен ли процесс сервера adb и запустить его:

`adb start-server`

- Завершить процесс сервера adb:

`adb kill-server`

- Запустить удалённую оболочку на целевом эмуляторе/устройстве:

`adb shell`

- Установить приложение Android на эмуляторе/устройстве:

`adb install -r {{путь/до/файла.apk}}`

- Скопировать файл/папку с целевого устройства:

`adb pull {{путь/до/папки_или_файла_на_устройстве}} {{путь/до/локальной_папки}}`

- Скопировать файл/папку на целевое устройство:

`adb push {{путь/до/локального_файла_или_папки}} {{путь/до/целевой_папки_на_устройстве}}`

- Вывести список подключенных устройств:

`adb devices`