from new_exercise import new_exercise
from new_course import new_course
from new_course_exercise import new_course_exercise
from add_teacher import add_teacher
from add_students import add_students


def create_exercises():
    # .../opprog-easy-exercises/exercises/programmeerimine
    base_path = '/mnt/c/Users/Kusti/Desktop/opprog-easy-exercises/exercises/programmeerimine'
    executors = ['1']
    grader = 'AUTO'
    container_image = 'pygrader'
    max_mem = 30
    max_time = 7
    public = True

    exercises = [
        {'path': '/1/tervitus',
         'title': '1.1 Tervitus',
         'assets': ['/tester.py']
         },
        {'path': '/1/president',
         'title': '1.2 President',
         'assets': ['/tester.py']
        },
        {'path': '/1/astendamine',
         'title': '1.3 Astendamine',
         'assets': ['/tester.py']
         },
        {'path': '/1/nadala-ajakulu',
         'title': '1.4a Nädala ajakulu',
         'assets': ['/tester.py']
         },
        {'path': '/1/trahv',
         'title': '1.4b Trahv',
         'assets': ['/tester.py']
         },
        {'path': '/2/jaatumine',
         'title': '2.1 Jäätumine',
         'assets': ['/tester.py']
         },

        {'path': '/2/leedu-perenimed',
         'title': '2.2 Leedu perenimed',
         'assets': ['/tester.py']
         },
        {'path': '/2/pulss',
         'title': '2.3a Pulss',
         'assets': ['/tester.py']
         },
        {'path': '/2/istekoht',
         'title': '2.3b Istekoht',
         'assets': ['/tester.py']
         },
        {'path': '/2/bussid',
         'title': '2.3c Bussid',
         'assets': ['/tester.py']
         },
        {'path': '/2/spamm',
         'title': '2.3d Spämm',
         'assets': ['/tester.py']
         }

    ]

    ex_ids = []
    for ex in exercises:
        text_file = base_path + ex['path'] + '/exercise.html'
        grading_file = base_path + ex['path'] + '/evaluate.sh'
        asset_files = list(map(lambda a: base_path + ex['path'] + a, ex['assets']))
        ex_id = new_exercise(ex['title'], text_file, public, grader, grading_file, container_image,
                          max_time, max_mem, asset_files, executors)
        ex_ids.append(ex_id)

    return ex_ids


def create_course(title):
    return new_course(title)


def add_exercises(course_id, exercise_ids, threshold, exercise_alias):
    for ex, alias in zip(exercise_ids, exercise_alias):
        new_course_exercise(course_id, ex, threshold, None, None, True, True, None, alias)


def add_teachers(course_id, teachers):
    add_teacher(course_id, teachers)


if __name__ == '__main__':
    #course_id = create_course('Tehnoloogia tarbijast loojaks (rühmT)')
    #print(course_id)
    #ex_ids = create_exercises()
    #print(ex_ids)
    course_id = '108'

    # Programmeerimine
    #ex_ids = list(map(str,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]))


    # TTL
    # ex_ids = list(map(str,[48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 64, 153, 154, 155, 160, 156, 157, 158, 159, 161, 162, 21, 22, 163, 24, 25, 191, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]))

    # TTL viimane
    #ex_ids = list(map(str,[51, 52, 53, 137, 138, 139, 140, 141, 59, 61, 64, 153, 154, 155, 160, 156, 157, 158, 159, 161, 162, 21, 22, 163, 24, 25, 191, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 192]))

    # See on õige TTL, kasuta seda
    ex_ids = list(map(str,[1, 193, 50, 51, 52, 194, 195, 138, 139, 140, 141, 59, 153, 61, 154, 155, 64, 160, 156, 157, 158, 159, 161, 162, 21, 22, 163, 24, 25, 191, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 192]))
    ex_alias = ['1.1 Tervitus', '1.2 Aasta liblikas', '1.3 Astendamine', '1.4a Nädala ajakulu', '1.4b Trahv', '2.1 Pilved', '2.2 Sisseastumine Tartu Ülikooli informaatika bakalaureuseõppesse', '2.3a Pulss', '2.3b Istekoht', '2.3c Bussid', '2.3d Spämm', '3.1 Äratus', '3.2 Jänesevanemate mure', '3.3 Täringumäng', '3.4a Jänesevanemate mure ver. 2', '3.4b Õunte jagamine', '3.4c Male', '4.1 Suured tähed', '4.2a Eesti haldusüksuse lipp', '4.2b Liiklusmärk', '4.2c Maja', '4.2d Malelaud', '5.1 Ülikooli vastuvõetud', '5.2 Jänesevanemate mure ver. 3', '5.3 Sissetulekud', '5.4a Jukebox', '5.4b Rändesaldo', '5.4c Tahvli juurde', '6.1 Bänner', '6.2 Õunamahla tegemine', '6.3 Peo eelarve', '6.4a Tervitused mõtisklustega', '6.4b Mündid', '6.4c Kuupäev', '7.1 Telegramm', '7.2 Päevik', '7.3 Kalkulaator', '7.4a Täiendatud peo eelarve', '7.4b Nimepäev', '7.4c Elutee number', '8.1 Saja aakri mets']
    #ex_alias = ['1.1 Tervitus', '1.2 Aasta liblikas', '1.3 Astendamine', '1.4 Nädala ajakulu', '1.5 Trahv', '2.1 Pilved', '2.2 Sisseastumine Tartu Ülikooli informaatika bakalaureuseõppesse', '2.3 Pulss', '2.4 Istekoht', '2.5 Bussid', '2.6 Spämm', '3.1 Äratus', '3.2 Jänesevanemate mure', '3.3 Täringumäng', '3.4 Jänesevanemate mure ver. 2', '3.5 Õunte jagamine', '3.6 Male', '4.1 Suured tähed', '4.2 Eesti haldusüksuse lipp', '4.3 Liiklusmärk', '4.4 Maja', '4.5 Malelaud', '5.1 Ülikooli vastuvõetud', '5.2 Jänesevanemate mure ver. 3', '5.3 Sissetulekud', '5.4 Jukebox', '5.5 Rändesaldo', '5.6 Tahvli juurde', '6.1 Bänner', '6.2 Õunamahla tegemine', '6.3 Peo eelarve', '6.4 Tervitused mõtisklustega', '6.5 Mündid', '6.6 Kuupäev', '7.1 Telegramm', '7.2 Päevik', '7.3 Kalkulaator', '7.4 Täiendatud peo eelarve', '7.5 Nimepäev', '7.6 Elutee number', '8.1 Saja aakri mets']


    # Tarkvaraarendus
    #ex_ids = list(map(str,[164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190]))
    #ex_alias = ['1.1 Kalade kaalumine', '2.1 Lauatennis', '2.2 Kalorsus', '2.3a Retseptid', '2.3b Kohustuslik kirjandus', '2.3c Vähimatest suurim', '3.1 Koristaja', '3.2 Hinnete tabel', '3.3a Nummerda', '3.3b Bingo reeglite kontrollimine', '3.3c Maksimaalne rida', '3.3d Kas on võitnud?', '3.3e Sudoku lahenduse kontrollimine', '3.3f Anagrammi otsing', '4.1 Hinnete tabel failist', '4.2a Tehnika', '4.2b Programmeerimisest maalähedaselt', '5.1 Teksti analüüs', '5.2 Rahvusvahelised sõidukid', '5.3a Albumid', '5.3b Juhuslik Bingo tabel', '5.3c Lubaduste ühisosa', '5.3d Võiduks veel vaja', '6.1 Alla ja üles', '6.2 Paarissumma', '6.3a Dissonantne järjekord I', '6.3b Dissonantne järjekord II']

    # Programmeerimine uued ülesanded
    #ex_ids = list(map(str,[1, 199, 214, 202, 203, 218, 219, 220, 221, 207, 222, 213, 223, 210, 211, 224, 212, 225, 243, 244, 245, 246, 247, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 239, 240, 248, 241, 242, 198, 197, 196]))
    #ex_alias = ['1.1 Tervitus', '1.2 President', '1.3 Jäägi leidmine', '1.4 Sammulugeja', '1.5 Kergejõustiku kahevõistlus', '2.1 Kehalise kasvatuse tund', '2.2 Hääletaja vanus', '2.3 Lapse pikkus', '2.4 Paki saatmine', '2.5 Rannailm', '2.6 Kalkulaator', '3.1 Juku õpib', '3.2 Taimer', '3.3 Pooliku püramiidi süsteem', '3.4 Iga kolmas võidab', '3.5 Täieliku püramiidi süsteem', '3.6 Investeerimine indeksfondidesse', '4.1 Male käikude üleskirjutamine', '4.2 Lipp, Aafrika riigid', '4.3 Puu', '4.4 Auto', '4.5 Rukkilill', '4.6 Emotikon', '5.1 Hiiumaa populaarsed nimed', '5.2 Pooliku püramiidi süsteem ver. 2', '5.3 Torm', '5.4 Audioraamatud', '5.5 Kontojääk', '5.6 Kampaaniahinnad', '6.1 Loitsu automatiseerija', '6.2 Elektrihind', '6.3 Käimine', '6.4 Täishäälikute tuvastaja', '6.5 Keskmine hinne', '6.6 Tüdrukute nimed', '7.1 Teksti korrastamine', '7.2 Pesukaru', '7.3 Vestlusrobot', '7.4 Sünnipäevatort', '7.6 Tähtpäevade nädalapäevad', '8.1 Mikroinvesteerimine', '8.2 D-vitamiin', '8.3 Maskid']


    # TTL ver 2
    #ex_ids = list(map(str,[48, 193, 50, 51, 52, 194, 195, 138, 139, 140, 141, 59, 61, 64, 153, 154, 155, 160, 156, 157, 158, 159, 161, 162, 21, 22, 163, 24, 25, 191, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 192]))

    # Programmeerimine ITMI
    #ex_ids = list(map(str, [1, 200, 201, 202, 203, 204, 205, 8, 206, 207, 10, 11, 213, 210, 211, 155, 212, 17, 215, 21, 216, 22, 24, 217, 191, 235, 238, 29, 237, 30, 239, 249, 248, 35, 251, 36, 165, 166, 167, 168, 170, 169, 197, 198, 192, 172, 179, 256, 177, 173, 175, 181, 255, 185, 182, 178, 174, 187, 188, 259, 260]))
    #ex_alias = ['1.1. Tervitus', '1.2. Aasta loom', '1.3. Ringi ümbermõõdu arvutamine', '1.4. Sammulugeja', 'Lisaülesanne 1.5. Kergejõustiku kahevõistlus', 'Lisaülesanne 1.6. Küpsisetort', '2.1 Parool', '2.2 Leedu perenimed', '2.3 Elektriauto', '2.4 Rannailm', 'Lisaülesanne 2.5 Istekoht', 'Lisaülesanne 2.6 Bussid', '3.1 Juku õpib', '3.2 Pooliku püramiidi süsteem', '3.3 Iga kolmas võidab', '3.4 Õunte jagamine', 'Lisaülesanne 3.5 Investeerimine indeksfondidesse', 'Lisaülesanne 3.6 Male', '4.1 Töögraafik', '4.2 Sissetulekud', '4.3 Palindroomid', '4.4 Jukebox', 'Lisaülesanne 4.5 Tahvli juurde', 'Lisaülesanne 4.6 Kampaaniahinnad', '5.1 Õunamahla tegemine', '5.2 Täishäälikute tuvastaja', '5.3 Nimede järjestaja', '5.4 Mündid', 'Lisaülesanne 5.5 Tüdrukute nimed', 'Lisaülesanne 5.6 Kuupäev', '6.1 Teksti korrastamine', '6.2 Logi', '6.3 Vestlusrobot', '6.4 Nimepäev', 'Lisaülesanne 6.5 Vigane pangaautomaat', 'Lisaülesanne 6.6 Elutee number', '7.1 Lauatennis', '7.2 Kalorsus', '7.3 Retseptid', '7.4 Kohustuslik kirjandus', 'Lisaülesanne 7.5 Koristaja', 'Lisaülesanne 7.6 Vähimatest suurim', '8.1 D-vitamiin', '8.2 Mikroinvesteerimine', 'Lisaülesanne 8.3 Saja Aakri mets', '10.1 Nummerda', '10.2 Tehnika', '10.3 Absoluutsed tabelid', '10.4 Anagrammi otsing', 'Lisaülesanne 10.5 Bingo reeglite kontrollimine', 'Lisaülesanne 10.6 Kas on võitnud?', '11.1 Teksti analüüs', '11.2 Listid sõnastikuks', '11.3 Lubaduste ühisosa', '11.4 Rahvusvahelised sõidukid', 'Lisaülesanne 11.5 Hinnete tabel failist', 'Lisaülesanne 11.6 Maksimaalne rida', '12.1 Alla ja üles', '12.2 Paarissumma', 'Lisaülesanne 12.3 Pikim pikkus', 'Lisaülesanne 12.4 Rekursiivne kuup']

    add_exercises(course_id, ex_ids, 100, ex_alias)
    add_teachers(course_id, [''])



