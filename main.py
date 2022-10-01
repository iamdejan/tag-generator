import argparse
import semver

VALID_PARTS = ["major", "minor", "patch", "prerelease"]

REQUIRED_ARG_MESSAGE = f"At least one argument between {VALID_PARTS[:-1]} must be specified."
VERSION_VALUE_MESSAGE = f"If not specified, the default value is 0."

parser = argparse.ArgumentParser(description="A simple program to generate and bump SemVer tag.")

subparser = parser.add_subparsers(dest="command")
create = subparser.add_parser("create", help="Generate a new tag from scratch.", description=REQUIRED_ARG_MESSAGE)
bump = subparser.add_parser("bump", help="Bump existing tag given previous tag.")

create.add_argument("--major", type=int, help=f"Major version. {VERSION_VALUE_MESSAGE}")
create.add_argument("--minor", type=int, help=f"Minor version. {VERSION_VALUE_MESSAGE}")
create.add_argument("--patch", type=int, help=f"Patch version. {VERSION_VALUE_MESSAGE}")
create.add_argument("--prerelease", type=str, help=f'Pre-release version. Accepted format: "alphabet.number", e.g. "alpha.1"')
create.add_argument("--build", type=str, help=f"Build version. If you bump up the tag, build version will be reset.")

bump.add_argument("--previous-tag", type=str, help="Previously generated tag that you want to bump. Recommended if the previous tag is 
generated using create sub-command.")
bump.add_argument("--part", type=str, help=f"Determine which part you want to bump. Accepted values: {VALID_PARTS}")


def validate_prerelease(prerelease) -> str:
    if prerelease == None:
        return ""
    prerelease = prerelease.strip()
    if prerelease == "":
        return ""
    try:
        (_, prerelease_number) = prerelease.split(".")
        prerelease_number = int(prerelease_number)
        return ""
    except ValueError:
        return f'Pre-release "{prerelease}" is invalid. It should be in "alphabet.number" format, e.g. "beta.2"'


def print_tag(raw_tag):
    print("Generated tag:")
    print(f"v{raw_tag}")


def create_tag(args):
    if args.major == None and args.minor == None and args.patch == None:
        print("At least one of either --major, --minor, or --patch should be provided!")
        print(f"For more information, please use 'create -h' or 'create --help' to see the documentation for 'create' subcommand!")
        exit(1)
    major = 0 if args.major == None else args.major
    minor = 0 if args.minor == None else args.minor
    patch = 0 if args.patch == None else args.patch
    prerelease = args.prerelease
    error = validate_prerelease(prerelease)
    if error:
        print(error)
        exit(1)
    print_tag(semver.VersionInfo(major, minor, patch, prerelease, build=args.build))


def bump_tag(args):
    if args.previous_tag == None:
        print("Previous tag should be provided! See 'bump -h' or 'bump --help' for more information.")
        exit(1)

    previous_tag = args.previous_tag
    if previous_tag[0] != 'v':
        print('Previous tag should start with "v"!')
        exit(1)
    part = args.part
    if args.part == None or part not in VALID_PARTS:
        print(f"Argument --part should be provided! Accepted values: {VALID_PARTS}")
        exit(1)
    tag = semver.VersionInfo.parse(previous_tag[1:])
    print_tag(tag.next_version(part))


def main():
    args = parser.parse_args()
    if args.command == 'create':
        create_tag(args)
    elif args.command == 'bump':
        bump_tag(args)
    else:
        print("Please use --help or -h for documentation.")
        exit(1)


if __name__ == "__main__":
    main()

