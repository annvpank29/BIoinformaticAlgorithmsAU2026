# Homework 1

ФИО: Панкратова Анна

Группа: 402 БИ

## Выполненные задачи

- Reverse Complement
- Neighbors
- Frequent Words with Mismatches and Reverse Complements

## Git commands

- `git status` — посмотреть состояние файлов
- `git diff` — посмотреть изменения
- `git add FILE` — подготовить файл к коммиту
- `git commit -m "MESSAGE"` — создать коммит
- `git push` — отправить коммиты на GitHub
- `git log --oneline` — посмотреть историю
- `git branch NAME` — создать ветку
- `git switch NAME` — перейти в другую ветку
- `git switch -c NAME` — создать ветку и перейти в неё
- `git merge BRANCH` — выполнить слияние
- `git revert -m 1 HASH` — отменить merge-коммит
- `git revert HASH` — отменить обычный коммит
- `git log --oneline --graph --all` — показать историю и ветвление
- `git branch -d NAME` — удалить локальную ветку
- `git push origin --delete NAME` — удалить удалённую ветку

## Branching and revert

### Состояние после первого слияния

После первого слияния ветки `testing` в `HW1` в ветке `HW1` появились:

- `HW1/neighbors.py`
- изменения из ветки `testing`

При этом в истории был создан merge-коммит `Merge testing into HW1`.

### Состояние после отмены слияния

Команда `git revert -m 1` отменила изменения, внесённые первым merge-коммитом.

В результате файл `HW1/neighbors.py` исчез из ветки `HW1`, но сам merge-коммит остался в истории.

### Результат повторного слияния

1. **Какой результат я ожидала?**

   Я ожидала, что при повторном слиянии ветки `testing` файл `neighbors.py` снова появится в `HW1`.

2. **Что произошло на самом деле?**

   При повторном слиянии появился только новый файл `frequent_kmers.py`. Файл `neighbors.py` не восстановился.

3. **Почему файл `neighbors.py` не восстановился?**

   Потому что Git уже учитывал первый merge в истории. Команда `git revert` не удаляет merge-коммит, а только отменяет внесённые им изменения. Поэтому при повторном merge Git переносит только новые изменения из `testing`.

4. **Какой командой я восстановила его?**

   `git revert 9bb9f5d`