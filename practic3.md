## Задача 1
Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
```bash
local arr = std.makeArray(25, function(x) "ИKБO-" + (x + 1) + "-23");

local Person(age, group, name) = {
  age: age,
  group: arr[group - 1],
  name: name,
};

{
  groups: arr,
  students: [
    Person(19, 4, 'Иванов И.И.'),
    Person(18, 5, 'Петров П.П.'),
    Person(18, 5, 'Сидоров С.С.'),
    Person(19, 63, 'Головач Н.Е.'),
  ],
  subject: "",
}
```

##Вывод:
```bash
{
  "groups": [
    "ИКБО-1-23",
    "ИКБО-2-23",
    "ИКБО-3-23",
    "ИКБО-4-23",
    "ИКБО-5-23",
    "ИКБО-6-23",
    "ИКБО-7-23",
    "ИКБО-8-23",
    "ИКБО-9-23",
    "ИКБО-10-23",
    "ИКБО-11-23",
    "ИКБО-12-23",
    "ИКБО-13-23",
    "ИКБО-14-23",
    "ИКБО-15-23",
    "ИКБО-16-23",
    "ИКБО-17-23",
    "ИКБО-18-23",
    "ИКБО-19-23",
    "ИКБО-20-23",
    "ИКБО-21-23",
    "ИКБО-22-23",
    "ИКБО-23-23",
    "ИКБО-24-23"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-23",
      "name": "Иванов И.И"
    },
    {
      "age": 18,
      "group": "ИКБО-5-23",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-23",
      "name": "Сидоров С.С."
    },
    {
      "age": 19,
      "group": "ИКБО-63-23",
      "name": "Головач Н.Е."
    }
  ],
  "subject": "Конфигурационное управление"
}
```
## Задача 2
Реализовать на Dhall приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
```bash
let List/generate = https://prelude.dhall-lang.org/v1
let groups = List/generate 24 Text
    (\(n : Natural) ->
    "ИКБО-${Natural/show (n + 1)}-20"
    )
let person =
    \(name : Text) ->
    \(age : Natural) ->
    \(group : Natural) ->
    {
        name = name,
        age = age,
        group = "ИКБО-${Natural/show group}-20"
    }

in {
    groups
    ,students = [
      person("Иванов И.И", 19, 4),
      person("Петров П.П.", 18, 5),
      person("Сидоров С.С.", 18, 5),
      person("Головач Н.Е.", 19, 63)
    ]
    ,subject = "Конфигурационное управление"
}
```
##Вывод:
```bash
groups:
  - "ИКБО-1-20"
  - "ИКБО-2-20"
  - "ИКБО-3-20"
  - "ИКБО-4-20"
  - "ИКБО-5-20"
  - "ИКБО-6-20"
  - "ИКБО-7-20"
  - "ИКБО-8-20"
  - "ИКБО-9-20"
  - "ИКБО-10-20"
  - "ИКБО-11-20"
  - "ИКБО-12-20"
  - "ИКБО-13-20"
  - "ИКБО-14-20"
  - "ИКБО-15-20"
  - "ИКБО-16-20"
  - "ИКБО-17-20"
  - "ИКБО-18-20"
  - "ИКБО-19-20"
  - "ИКБО-20-20"
  - "ИКБО-21-20"
  - "ИКБО-22-20"
  - "ИКБО-23-20"
  - "ИКБО-24-20"
students:
  - age: 19
    group: "ИКБО-4-20"
    name: "Иванов И.И."
  - age: 18
    group: "ИКБО-5-20"
    name: "Петров П.П."
  - age: 18
    group: "ИКБО-5-20"
    name: "Сидоров С.С."
  - age: 19
    group: "ИКБО-63-20"
    name: "Головач Н.Е."
subject: "Конфигурационное управление"

```
## Задача 3
Реализовать грамматики, описывающие следующие языки (для каждого решения привести БНФ). Код решения должен содержаться в переменной BNF. 
```bash
import random

def parse_bnf(text):
    ```
    Преобразовать текстовую запись БНФ в словарь.
    ```
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    ```
    Сгенерировать случайную фразу.
    ```
    if start in grammar:
        seq = random.choice(grammar[start])
        phrase = ''
        for name in seq:
            phrase += generate_phrase(grammar, name)
        return phrase
    return str(start)

BNF = '''E = 0 E | 1 E | 0 | 1'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), start='E'))
```
##Вывод:

```python
Process finished with exit code 0
```
