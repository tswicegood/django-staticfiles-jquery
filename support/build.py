"""
Builds the version of jQuery that's in vendor/jquery and packages
it as a Django app for use with Django staticfiles.
"""
import subprocess
import sys

DEFAULT_VERSION = "1.8.3"


def cp(src):
    cmd = [
        "cp -R vendor/jquery/%s jquery/static/jquery/" % src,
    ]
    subprocess.call(cmd, shell=True)


def main():
    args = {
        "build": "./node_modules/grunt/bin/grunt",
        "version": DEFAULT_VERSION if len(sys.argv) is 1 else sys.argv[1],
    }
    subprocess.call(["mkdir -p ./jquery/static/jquery"], shell=True)
    subprocess.call(
            ["cd vendor/jquery && git fetch origin && git submodule update && git checkout %(version)s && %(build)s" %
                args],
            shell=True)
    cp("dist/*")
    cp("MIT-LICENSE.txt")

    with open("./VERSION", "w") as f:
        f.write(args["version"])


if __name__ == "__main__":
    main()
