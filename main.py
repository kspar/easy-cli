import argparse

from autoass import autoass
from new_course import new_course
from new_course_exercise import new_course_exercise
from new_exercise import new_exercise
from add_teacher import add_teacher


def handle_new_course(args):
    new_course(args.title)


def handle_new_exercise(args):
    new_exercise(args.title, args.text_file, args.public, args.grader, args.grading_file,
                 args.image, args.max_time, args.max_mem, args.asset_files, args.executors)


def handle_new_course_ex(args):
    new_course_exercise(args.course_id, args.exercise_id, args.threshold, args.soft_deadline, args.hard_deadline,
                        args.student_visible, args.assessments_student_visible, args.instructions_html,
                        args.title_alias)


def handle_teacher_autoass(args):
    autoass(args.course, args.exercise, args.solution_file)

def handle_add_teacher(args):
    add_teacher(args.course_id, args.teachers)



if __name__ == '__main__':
    top_parser = argparse.ArgumentParser()
    subparsers = top_parser.add_subparsers()

    # New course
    new_course_parser = subparsers.add_parser("new-course")
    new_course_parser.add_argument("--title", required=True)
    new_course_parser.set_defaults(func=handle_new_course)

    # New exercise
    new_ex = subparsers.add_parser("new-exercise")
    new_ex.add_argument("--title", required=True)
    new_ex.add_argument("--text-file", required=True)
    new_ex.add_argument("--public", action='store_true')
    new_ex.add_argument("--grader", required=True, choices=['auto', 'teacher'])
    new_ex.add_argument("--grading-file", required=False)
    new_ex.add_argument("--image", required=False)
    new_ex.add_argument("--max-time", required=False, type=int)
    new_ex.add_argument("--max-mem", required=False, type=int)
    new_ex.add_argument('--asset-files', nargs='*', default=[])
    new_ex.add_argument('--executors', nargs='+', required=False)
    new_ex.set_defaults(func=handle_new_exercise)

    # New course exercise
    new_course_ex = subparsers.add_parser("add-exercise-to-course")
    new_course_ex.add_argument('--course-id', required=True)
    new_course_ex.add_argument('--exercise-id', required=True)
    new_course_ex.add_argument('--threshold', required=True, type=int)
    new_course_ex.add_argument('--soft-deadline')
    new_course_ex.add_argument('--hard-deadline')
    new_course_ex.add_argument('--student-visible', action='store_true', default=True)
    new_course_ex.add_argument('--assessments-student-visible', action='store_true', default=True)
    new_course_ex.add_argument('--instructions-html')
    new_course_ex.add_argument('--title-alias')
    new_course_ex.set_defaults(func=handle_new_course_ex)

    # Teacher autoassess
    autoassess = subparsers.add_parser("autoassess")
    autoassess.add_argument("--course", required=True)
    autoassess.add_argument("--exercise", required=True)
    autoassess.add_argument("--solution-file", required=True)
    autoassess.set_defaults(func=handle_teacher_autoass)

    # Add teacher
    add_teacher_parser = subparsers.add_parser("add-teacher")
    add_teacher_parser.add_argument('--course-id', required=True)
    add_teacher_parser.add_argument('--teachers', nargs='+', required=True)
    add_teacher_parser.set_defaults(func=handle_add_teacher)

    args = top_parser.parse_args()
    args.func(args)
