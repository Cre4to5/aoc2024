#msullivan/aoc-scrape.py
#https://gist.github.com/msullivan/17a6abba8281e5610e189db9d82b925c

from aocd.get import current_day, most_recent_year
from aocd.models import default_user, Puzzle, User
import bs4
import bs4.element
import html
import os.path
import argparse

# adapated from aocd internals
def get_puzzle(session=None, day=None, year=None):
    """
    Get puzzle for day (1-25) and year (>= 2015)
    User's session cookie is needed (puzzle inputs differ by user)
    """
    if session is None:
        user = default_user()
    else:
        user = User(token=session)
    if day is None:
        day = current_day()
    if year is None:
        year = most_recent_year()
    puzzle = Puzzle(year=year, day=day, user=user)
    return puzzle


def cleanup(el):
    # strip out ems, since those appear in plenty of inputs
    if isinstance(el, bs4.element.NavigableString):
        return str(el)
    elif isinstance(el, bs4.element.Tag) and el.name == 'em':
        return cleanup(el.contents[0])
    else:
        return el


def slurp(soup):
    codes = [y for x in soup.find_all('pre') if (y := x.find('code'))]
    tests = []
    for code in codes:
        cleaned = [cleanup(x) for x in code.contents]
        if all(isinstance(x, str) for x in cleaned):
            tests.append(html.unescape(''.join(cleaned)))

    return tests


def write(day, tests, dirname, dry=True):
    if not dirname:
        dirname = f'inputs'

    if not dry:
        os.makedirs(dirname, exist_ok=True)

        name = os.path.join(dirname, f"{day}.txt")
        print(f'==== {name}')
        print(tests)
        if not dry:
            with open(name, 'w') as f:
                f.write(tests)

def getSession():
    __location__ = os.path.realpath(os.path.join(os.path.expanduser('~'),".config/aocd/token.txt"))
    with open(__location__, "r") as f:
        return f.readline().strip()

parser = argparse.ArgumentParser(description='AOC test input scraper')
parser.add_argument("day", nargs="?", type=int)
parser.add_argument("year", nargs="?", type=int)
parser.add_argument('--dry', '-d', action='store_true',
                    help='Do a dry run, without writing files')
parser.add_argument('--dir', type=str,
                    help='Override target directory')

def getlines(day):
    with open(f"./inputs/{day}.txt", "r")as f:
        return f.readlines()

def main():
    args = parser.parse_args()

    puzzle = get_puzzle(session=getSession(), day=args.day, year=args.year)
    tests = puzzle.input_data
    write(puzzle.day, tests, dirname=args.dir, dry=args.dry)


if __name__ == '__main__':
    main()