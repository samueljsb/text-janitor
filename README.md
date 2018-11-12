Text Janitor
============

A Python tool to clean text files.
This tool was specifically developed to clean websites affected by the Location For Expert redirection attack (detailed [here][DNC]), however it can be used to clean any text from files by using a different regex pattern file.

**N.B.**
This tool trips up on non-unicode files (or those encoded in a format which cannot be opened by Python).
Therefore, it cannot guarantee a perfect clean.

Usage
-----

    usage: text_janitor.py [-h] directory output_dir patterns

    Clean malicious code from text files in a directory.

    positional arguments:
    directory   the directory containing the website
    output_dir  the directory the edited files will be written to
    patterns    file containing the regex patterns to remove

    optional arguments:
    -h, --help  show this help message and exit

_e.g._

    python3 text_janitor.py ~/website ~/website_clean location-for-expert.txt

Shell script
------------

The included shell script can be used to modify files in place, using the patters.txt regex.

    usage: ./clean_site.sh site_directory pattern_file

_e.g._

    ./clean_site ~/website patterns.txt

[DNC]: https://malware.dontneedcoffee.com/hosted/anonymous/kotd.html
