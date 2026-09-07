adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print(adwentures_of_tom_sawer.replace("\n", " "))
# task 02 ==
""" Замініть .... на пробіл
"""
print(adwentures_of_tom_sawer.replace("....", " "))
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer_remake = adwentures_of_tom_sawer.replace("....", "")
print(adwentures_of_tom_sawer_remake.replace("  ", ""))
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(adwentures_of_tom_sawer.count("h"))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count = 0
for word in adwentures_of_tom_sawer.split():
    if word[0].isupper():
        count += 1
print(count)
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
tom1 = adwentures_of_tom_sawer.index("Tom")
print(adwentures_of_tom_sawer.index("Tom", tom1 + 1))

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
text = adwentures_of_tom_sawer.replace("\n", " ")
text2 = text.replace("....", "gggg")
text3 = text2.replace(".", ".\n")
text4 = text3.replace("gggg", "....")
adwentures_of_tom_sawer_sentences = text4
print(text4)
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
pred4 = adwentures_of_tom_sawer_sentences.split(".\n")
pred4[3] = pred4[3].lower()
print(pred4)
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
is_it_start_with = 0
for sentence in pred4:
    if sentence.startswith("By the time"):
        print("True")
        break
    else:
        is_it_start_with += 1
if is_it_start_with > 0:
    print("False")
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
pred4[-2] = pred4[-2].split()
print(len(pred4[-2]))