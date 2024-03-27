import os
from collections import defaultdict
from Peak import Peak


def parse_seq_file(file_path: str):
    res_dict = {}

    res_file = open(file_path, 'r')
    for line in res_file:
        res_dict[int(line.split()[1])] = line.split()[0]

    return res_dict


def parse_ambig_file(file_path: str, seq_dict: dict):
    ambig_dict = defaultdict(list)

    ambig_file = open(file_path, 'r')
    for line in ambig_file:
        pairs = line.split(",")
        key = Peak(pairs[0], seq_dict)

        for p in pairs[1:]:
            ambig_dict[key].append(Peak(p, seq_dict))

    return ambig_dict


def generate_result_file(upl_file_path: str, ambig_dict):
    resources_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources")
    output_file_path = os.path.join(resources_dir, 'out.upl')

    upl_file = open(upl_file_path, 'r')
    out_file = open(output_file_path, 'w')

    for line in upl_file:
        if line.strip().startswith('#'):
            continue

        peak = Peak(line, None)
        out_file.write(line)
        for p in ambig_dict[peak]:
            out_file.write(f'{p} 0.00\n')


def main():
    resources_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources")

    # 1. Parse seq file -> dict[res_num] = 'res_name'
    seq_file_path = os.path.join(resources_dir, 'watx.seq')
    seq_dict = parse_seq_file(seq_file_path)
    print(f'Parsed seq file with {len(seq_dict)} sequences')

    # 2. Parse ambig file -> dict[first_peak] = [list of other peaks]
    ambig_file_path = os.path.join(resources_dir, 'ambig.txt')
    ambig_dict = parse_ambig_file(ambig_file_path, seq_dict)
    print(f'Parsed ambig file with {len(ambig_dict)} peaks:')

    # 3. Read line by line from 3 line to end -> generate output file
    # where after target peak add lines with ambitious peaks
    upl_file_path = os.path.join(resources_dir, 'watx_stas_8.upl')
    generate_result_file(upl_file_path, ambig_dict)


if __name__ == '__main__':
    main()
