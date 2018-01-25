"""
Usage: FrontPi.py [-h|--help|-v|--version]

Options:
 -h --help     Show this help message.
 -v --version  Show the version.
"""
import docopt
import schema
import yaml

if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    with open('config.yml') as cfg:
        conf = yaml.load(cfg.read())
    options = {}
    options.update(conf)
    options.update({k.replace('-', ''): v for k, v in args.items()})
    pattern = schema.Schema({'ride_pin': schema.Use(int),
                             'flag_pin': schema.Use(int),
                             'led_pin': schema.Use(int)})
    options = pattern.validate(options)
