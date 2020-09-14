from tldextract import TLDExtract

# cache locally, where we can write files
no_fetch_extract = TLDExtract(cache_file='./.tld_cache')


def main():
    provider_file = open('email-providers.csv', 'r')

    all_good = True
    for line in provider_file.readlines():
        provider_domain = line.rstrip()
        domain_parts = no_fetch_extract(provider_domain)
        if not (domain_parts.domain and domain_parts.suffix):
            all_good = False
            print('Not a valid domain: {} ({})'.format(
                provider_domain,
                domain_parts,
            ))

    if not all_good:
        exit(1)


if __name__ == '__main__':
    main()
