# Модуль для сортировки файлов

  
## Функционал  
По указанному пути создаёт папки под все типы расширений, после чего перемещает туда соответствующие файлы.  
Можно запускать из исходного файла (путь вставить в консоль) или импортировать в свой проект, передав путь аргументом:  

```python
from file_organizer import FileOrganizer
FileOrganizer.organize_files('path/to/') 
```
Использованы только стандартные библиотеки, так что дополнительных зависимостей нет.
  