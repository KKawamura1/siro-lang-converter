import argparse
from typing import Sequence
import sys


def chars_to_ords(chars: Sequence[str]) -> Sequence[int]:
    return [ord(c) for c in chars]


def num_to_10bases(num: int, max_num_digits: int = 5) -> Sequence[int]:
    ans = []
    for d in range(max_num_digits):
        ans.append(num % 10)
        num //= 10
    return list(reversed(ans))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('string', type=str)
    params = parser.parse_args()
    string = params.string
    if len(string) == 1:
        chars = [string]
    else:
        chars = list(string)

    ords = chars_to_ords(chars)
    num_ords = len(ords)
    ords_with_10bases = [num_to_10bases(num) for num in ords]
    str1 = '[-]>' * (4 + num_ords) + '[-]' + '<' * (4 + num_ords)
    str2 = (
        f'++++++++++[>++++++++++[>++++++++++[>++++++++++[> '
        f'{ ">".join(["+" * n for n in [bases10[0] for bases10 in ords_with_10bases]]) } { "<" * (num_ords - 1) } <-]'
        f'> { ">".join(["+" * n for n in [bases10[1] for bases10 in ords_with_10bases]]) } { "<" * (num_ords - 1) } < <-]'
        f'>> { ">".join(["+" * n for n in [bases10[2] for bases10 in ords_with_10bases]]) } { "<" * (num_ords - 1) } << <-]'
        f'>>> { ">".join(["+" * n for n in [bases10[3] for bases10 in ords_with_10bases]]) } { "<" * (num_ords - 1) } <<< <-]'
        f'>>>> { ".>".join(["+" * n for n in [bases10[4] for bases10 in ords_with_10bases]]) } . { "<" * (num_ords - 1) } <<<<'
    )
    print(str1)
    print(str2)


if __name__ == '__main__':
    main()