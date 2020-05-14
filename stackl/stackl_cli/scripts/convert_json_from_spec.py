#!/opt/venv/bin/python
from abc import ABC, abstractmethod
from glom import glom
import json
import argparse
import sys


class Converter(ABC):
    @property
    @abstractmethod
    def input_doc(self):
        pass

    @property
    @abstractmethod
    def spec_doc(self):
        pass

    @property
    @abstractmethod
    def output_path(self):
        pass

    @abstractmethod
    def convert(self):
        pass


class JsonConverter(Converter):
    @property
    def spec_doc(self):
        pass

    @property
    def output_path(self):
        pass

    @property
    def input_doc(self):
        pass

    def __init__(self,
                 spec_doc_file: str = 'spec.json',
                 json_doc_file: str = 'inputs.json',
                 outputs_file: str = 'outputs.json'):
        self.spec_doc_file = spec_doc_file
        self.json_doc_file = json_doc_file
        self.outputs_file = outputs_file
        self.read_files()

    def read_files(self):
        with open(self.json_doc_file) as f:
            self.json_doc = json.load(f)
        with open(self.spec_doc_file) as f:
            self.json_spec = json.load(f)

    def convert(self):
        result = {}
        for field_name, field_spec in self.json_spec.items():
            result[field_name] = glom(self.json_doc, field_spec)
        return result


def get_args(args=[]):
    """Initializes a parser of :class:`ArgumentParser` object and returns the
    parsed arguments

    :param args: An array with arguments in short or long form
    :type args: list, optional
    :return: parsed arguments, can be used like a dict
    :rtype: ArgumentParser
    """
    parser = argparse.ArgumentParser(
        description='Arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s',
                        '--spec',
                        required=False,
                        action='store',
                        default='spec.json',
                        help='The spec file to ready')
    parser.add_argument('-d',
                        '--doc',
                        required=False,
                        action='store',
                        default='inputs.json',
                        help='The doc file to convert')
    parser.add_argument('-f',
                        '--doc-format',
                        required=False,
                        action='store',
                        default='json',
                        help='The file format in your input document')
    parser.add_argument('-o',
                        '--outputs-file',
                        required=False,
                        action='store',
                        default='outputs.json',
                        help='The output file')
    args = parser.parse_args(args)
    return args


def main():
    args = get_args(sys.argv[1:])
    doc_format = args.doc_format
    if doc_format == 'json':
        converter = JsonConverter(json_doc_file=args.doc,
                                  spec_doc_file=args.spec,
                                  outputs_file=args.outputs_file)
    result = converter.convert()
    with open(args.outputs_file, 'w') as f:
        json.dump(result, f)


if __name__ == "__main__":
    # Execute only if run as a script, not when used in unit tests
    main()