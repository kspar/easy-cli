import argparse

from new_course import new_course


def handle_new_exercise(args):
    print('new-exercise')
    print(args)
    # TODO


def handle_new_course(args):
    new_course(args.title)


if __name__ == '__main__':
    top_parser = argparse.ArgumentParser()
    subparsers = top_parser.add_subparsers(required=True)

    # New exercise
    new_ex_parser = subparsers.add_parser("new-exercise")
    new_ex_parser.add_argument("--title", required=True)
    new_ex_parser.add_argument("--text-file", required=True)
    new_ex_parser.add_argument("--grader", required=True, choices=['auto', 'teacher'])
    new_ex_parser.add_argument("--public", action='store_true')
    new_ex_parser.add_argument("--aas-id")
    new_ex_parser.set_defaults(func=handle_new_exercise)

    # New course
    new_course_parser = subparsers.add_parser("new-course")
    new_course_parser.add_argument("--title", required=True)
    new_course_parser.set_defaults(func=handle_new_course)

    args = top_parser.parse_args()
    args.func(args)
