import argparse

from new_course import new_course
from new_exercise import new_exercise


def handle_new_exercise(args):
    new_exercise(args.title, args.text_file, args.public, args.grader, args.grading_file,
                 args.image, args.max_time, args.max_mem, args.asset_files, args.executors)


def handle_new_course(args):
    new_course(args.title)


if __name__ == '__main__':
    top_parser = argparse.ArgumentParser()
    subparsers = top_parser.add_subparsers()

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

    # New course
    new_course = subparsers.add_parser("new-course")
    new_course.add_argument("--title", required=True)
    new_course.set_defaults(func=handle_new_course)

    args = top_parser.parse_args()
    args.func(args)
