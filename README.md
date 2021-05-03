**Задача 1**

Реализовать программу, осуществляющую копирование файлов в соответствии с конфигурационным файлом. Конфигурационный файл
должен иметь формат ```xml```. Для каждого файла в конфигурационном файле должно быть указано его имя, исходный путь и
путь, по которому файл требуется скопировать.

**Пример**

Конфигурационный файл:


```<pre>
<code>
&lt;config&gt;
    &lt;file
            source_path="C:\Windows\system32"
            destination_path="C:\Program files"
            file_name="kernel32.dll"
    /&gt;
    &lt;file
            source_path="/var/log"
            destination_path="/etc"
            file_name="server.log"
    /&gt;
&lt;/config&gt;
</code>
</pre>
```
