import argparse, getpass
from pysnip import client

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("FILE", help=("File to publish"))
    p.add_argument("-n","--name",required=True,help=("Name of snippet"))
    p.add_argument("-a","--author",help=("Your name"))
    p.add_argument("-p","--password",required=False,help=("Password. Getpass will be used if not provided"))
    return p.parse_args()

def main(args):
    res = client.upload(
        args.name,
        args.password or getpass.getpass(),
        open(args.FILE, "r").read(),
        args.author,
    )
    print(res)

if __name__ == "__main__":
    main(parse_args())

