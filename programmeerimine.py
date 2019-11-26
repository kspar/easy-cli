from new_exercise import new_exercise
from new_course import new_course
from new_course_exercise import new_course_exercise


def create_exercises():
    # .../opprog-easy-exercises/exercises/programmeerimine
    base_path = '...'
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
        {'path': '/2/spamm',
         'title': '2.2 Spämm',
         'assets': ['/tester.py']
         },
        {'path': '/2/leedu-perenimed',
         'title': '2.3 Leedu perenimed',
         'assets': ['/tester.py']
         },
        {'path': '/2/pulss',
         'title': '2.4a Pulss',
         'assets': ['/tester.py']
         },
        {'path': '/2/istekoht',
         'title': '2.4b Istekoht',
         'assets': ['/tester.py']
         },
        {'path': '/2/bussid',
         'title': '2.4c Bussid',
         'assets': ['/tester.py']
         },
        {'path': '/3/aratus',
         'title': '3.1 Äratus',
         'assets': ['/tester.py']
         },
        {'path': '/3/laikimine',
         'title': '3.2 Laikimine',
         'assets': ['/tester.py']
         },
        {'path': '/3/taringumang',
         'title': '3.3 Täringumäng',
         'assets': ['/tester.py']
         },
        {'path': '/3/laikimine2',
         'title': '3.4a Laikimine v2',
         'assets': ['/tester.py']
         },
        {'path': '/3/vabavisked',
         'title': '3.4b Vabavisked',
         'assets': ['/tester.py']
         },
        {'path': '/3/male',
         'title': '3.4c Male',
         'assets': ['/tester.py']
         },
        {'path': '/4/suured-tahed',
         'title': '4.1 Suured tähed',
         'assets': ['/tester.py']
         },
        {'path': '/5/mootorrattad',
         'title': '5.1 Mootorrattad',
         'assets': ['/tester.py']
         },
        {'path': '/5/laikimine',
         'title': '5.2 Laikimine (for-tsükliga)',
         'assets': ['/tester.py']
         },
        {'path': '/5/sissetulekud',
         'title': '5.3 Sissetulekud',
         'assets': ['/tester.py']
         },
        {'path': '/5/jukebox',
         'title': '5.4a Jukebox',
         'assets': ['/tester.py']
         },
        {'path': '/5/loomulik-iive',
         'title': '5.4b Loomulik iive',
         'assets': ['/tester.py']
         },
        {'path': '/5/tahvli-juurde',
         'title': '5.4c Tahvli juurde',
         'assets': ['/tester.py']
         },
        {'path': '/6/banner',
         'title': '6.1 Bänner',
         'assets': ['/tester.py', '/rattad.py']
         },
        {'path': '/6/teleri-suurus',
         'title': '6.2 Teleri suurus',
         'assets': ['/tester.py']
         },
        {'path': '/6/peo-eelarve',
         'title': '6.3 Peo eelarve',
         'assets': ['/tester.py']
         },
        {'path': '/6/tervitused-motisklustega',
         'title': '6.4a Tervitused mõtisklustega',
         'assets': ['/tester.py']
         },
        {'path': '/6/mundid',
         'title': '6.4b Mündid',
         'assets': ['/tester.py']
         },
        {'path': '/6/kuupaev',
         'title': '6.4c Kuupäev',
         'assets': ['/tester.py']
         },
        {'path': '/7/telegramm',
         'title': '7.1 Telegramm',
         'assets': ['/tester.py']
         },
        {'path': '/7/paevik',
         'title': '7.2 Päevik',
         'assets': ['/tester.py']
         },
        {'path': '/7/kalkulaator',
         'title': '7.3 Kalkulaator',
         'assets': ['/tester.py']
         },
        {'path': '/7/taiendatud-peo-eelarve',
         'title': '7.4a Täiendatud peo eelarve',
         'assets': ['/tester.py']
         },
        {'path': '/7/nimepaev',
         'title': '7.4b Nimepäev',
         'assets': ['/tester.py']
         },
        {'path': '/7/elutee-number',
         'title': '7.4c Elutee number',
         'assets': ['/tester.py', '/sunnikuupaevad.txt']
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


def add_exercises(course_id, exercise_ids, threshold):
    for ex in exercise_ids:
        new_course_exercise(course_id, ex, threshold, None, None, True, True, None, None)


def add_teachers(course_id, teachers):
    pass


if __name__ == '__main__':
    course_id = create_course('...')
    print(course_id)
    ex_ids = create_exercises()
    print(ex_ids)
    add_exercises(course_id, ex_ids, 100)


