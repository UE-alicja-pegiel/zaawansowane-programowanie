import argparse


def args_parser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-i", "--image", default=None)
    arg_parse.add_argument("-o", "--output", type=str)
    arg_parse.add_argument("-c", "--camera", default=False)
    args = vars(arg_parse.parse_args())

    return args
