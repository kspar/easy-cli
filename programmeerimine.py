from new_exercise import new_exercise
from new_course import new_course
from new_course_exercise import new_course_exercise
from add_teacher import add_teacher


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


def add_exercises(course_id, exercise_ids, threshold):
    for ex in exercise_ids:
        new_course_exercise(course_id, ex, threshold, None, None, True, True, None, None)


def add_teachers(course_id, teachers):
    add_teacher(course_id, teachers)


if __name__ == '__main__':
    #course_id = create_course('Tehnoloogia tarbijast loojaks (rühmT)')
    #print(course_id)
    #ex_ids = create_exercises()
    #print(ex_ids)
    course_id = '31'
    #ex_ids = list(map(str,[48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 64, 153, 154, 155, 160, 156, 157, 158, 159, 161, 162, 21, 22, 163, 24, 25, 191, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]))

    # TTL
    #ex_ids = list(map(str,[51, 52, 53, 137, 138, 139, 140, 141, 59, 61, 64, 153, 154, 155, 160, 156, 157, 158, 159, 161, 162, 21, 22, 163, 24, 25, 191, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 192]))

    # Tarkvaraarendus
    ex_ids = list(map(str,[164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190]))

    # TTL ver 2
    # ex_ids = list(map(str,[48, 193, 50, 51, 52, 194, 195, 138, 139, 140, 141, 59, 61, 64, 153, 154, 155, 160, 156, 157, 158, 159, 161, 162, 21, 22, 163, 24, 25, 191, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 192]))
    add_exercises(course_id, ex_ids, 100)
    add_teachers(course_id, ['tauno.palts@ut.ee'])



