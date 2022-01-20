from modules import parser, detectors


options = parser.args_parser()
detectors.person_detector(options)
