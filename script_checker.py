import argparse
import csv


class ScriptTrippinOrNah(object):
    def __init__(self, orig, new):
        self.orig = orig
        self.new = new

    def read_organizers_from_csv(self, file):
        with open(file, 'rb') as f:
            reader = csv.reader(f)
            data = list(reader)
        organizer_ids = [organizer_id for sublist in data for organizer_id in sublist]
        return organizer_ids

    def main(self):
        orig_ids = self.read_organizers_from_csv(self.orig)
        ids_left = self.read_organizers_from_csv(self.new)

        if list(set(orig_ids).intersection(ids_left)):
            print('Script missed some ids')
        else:
            print('New ids popped up while you were writing the script')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Is your script trippin or nah?'
    )

    parser.add_argument(
        'orig',
        help='path to original csv'
    )

    parser.add_argument(
        'new',
        help='path to new csv'
    )

    args = parser.parse_args()

    orig, new = [getattr(args, arg) for arg in vars(args)]

    ScriptTrippinOrNah(
        orig,
        new,
    ).main()
