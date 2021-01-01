#!/usr/bin/python3

import os

def main():
    file_paths = ["email-providers.csv", "../email-providers.csv"]
    file_path = file_paths[0]
    for path in file_paths:
        if os.path.exists(path):
            file_path = path
            break
    provider_file = open(file_path, 'r')

    provider_domains = []
    all_good = True
    for line in provider_file.readlines():
        provider_domain = line.rstrip()
        if provider_domain in provider_domains:
            print('Duplicate entry: {}'.format(provider_domain))
            all_good = False
        if provider_domains:
            previous_domain = provider_domains[-1]
            current_order = [previous_domain, provider_domain]
            if sorted(current_order) != current_order:
                print('Wrong sorting: {} after {}'.format(
                    provider_domain,
                    previous_domain,
                ))
                all_good = False
        provider_domains.append(provider_domain)

    if not all_good:
        exit(1)


if __name__ == '__main__':
    main()
