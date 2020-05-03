import optparse

import scanner


def get_arguments():
  parser = optparse.OptionParser()
  parser.add_option("-t", "--target", dest="target",
                    help="target URL that you need to check vulnarabilities")
  args_options, arguments = parser.parse_args()
  return args_options


options = get_arguments()
if options.target is not None:
  links_to_ignore = []
  vuln_scanner = scanner.Scanner(str(options.target), links_to_ignore)
  vuln_scanner.run()
