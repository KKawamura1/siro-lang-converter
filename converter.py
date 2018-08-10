import argparse
import re
import sys
from typing import AbstractSet, Sequence, Mapping


class BrainF__kLang:
    def __init__(
            self,
            inc_ptr: str, dec_ptr: str,
            inc_val: str, dec_val: str,
            begin_loop: str, end_loop: str,
            std_input: str, std_output: str
    ) -> None:
        self.inc_ptr = inc_ptr
        self.dec_ptr = dec_ptr
        self.inc_val = inc_val
        self.dec_val = dec_val
        self.begin_loop = begin_loop
        self.end_loop = end_loop
        self.std_input = std_input
        self.std_output = std_output
        self.commands_names = set(['inc_ptr', 'dec_ptr',
                                   'inc_val', 'dec_val',
                                   'begin_loop', 'end_loop',
                                   'std_input', 'std_output'])

    @property
    def commands_set(self) -> AbstractSet[str]:
        return set([getattr(self, name) for name in self.commands_names])

    @property
    def commands_dict(self) -> Mapping[str, str]:
        return {name: getattr(self, name) for name in self.commands_names}


    def clean_up(self, source: str) -> Sequence[str]:
        pattern = f'({ "|".join([re.escape(command) for command in self.commands_set]) })'
        commands = re.findall(pattern, source)
        return commands

    def convert_to(self, source: str, target_lang: 'BrainF__kLang') -> str:
        commands = self.clean_up(source)
        command_to_abstractname = {command: abstractname
                                   for abstractname, command in self.commands_dict.items()}
        abstract_name_to_command = target_lang.commands_dict
        return ''.join([abstract_name_to_command[command_to_abstractname[command]]
                        for command in commands])



def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['bts', 'stb'])
    params = parser.parse_args()
    mode = params.mode

    brainf__k = BrainF__kLang('>', '<', '+', '-', '[', ']', ',', '.')
    sirolang = BrainF__kLang('いーねっ！', 'ｷｭｰｲ', 'おほほい', 'ぱいーん', '白組さん', '救済', 'ズンドコズンドコ♪', 'なんて日だ！')

    if mode == 'bts':
        # brainf**k to sirolang
        def convert(source: str) -> str:
            return brainf__k.convert_to(source, sirolang)
    elif mode == 'stb':
        # sirolang to brainf**k
        def convert(source: str) -> str:
            return sirolang.convert_to(source, brainf__k)
    else:
        raise
    for line in sys.stdin:
        print(convert(line), file=sys.stdout)



if __name__ == '__main__':
    main()
