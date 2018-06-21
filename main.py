from optparse import OptionParser
from parser import Parser
from draw import Drawer


if __name__ == '__main__':
    opt_parser = OptionParser()
    opt_parser.add_option("-o", "--output", dest="output", help="where to save the image")

    (options, args) = opt_parser.parse_args()

    try:
        parser = Parser(args[0])
        drawer = Drawer(parser.screen, parser.figures, parser.palette)
        drawer.draw()

        if vars(options)['output']:
            drawer.save(vars(options)['output'])
    except (ValueError, FileNotFoundError) as error:
        print(error)
