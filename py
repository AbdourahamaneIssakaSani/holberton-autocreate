#!/usr/bin/env bash

# py index.js
# py index.js file.js
# py -o index.js --- only one file
# py -h

help() {
    echo "NAME"
    echo -e "\tpy - creates a python file according to holberton requirements "
    echo
    echo "SYNOPSIS"
    echo -e "\tpy [OPTION]... [FILENAME]..."
    echo
    echo "DESCRIPTION"
    echo -e "\tpy command helps you to create your python file with the required shebang and execute rights." | fmt -u -w 100
    echo
    echo "OPTIONS"
    echo -e "\t-o, --open=FILE"
    echo -e "\t\t open the file in insert mode after creation"
    echo -e "\t-h, --help"
    echo -e "\t\t display this help screen"
    echo
    echo -e "\tExit status:"
    echo -e "\t\t0\tif OK"
    echo -e "\t\t2\tif invalid option or syntax"
    echo
    echo "AUTHOR"
    echo -e "\tWritten by Abdourahamane (Abissa) Issaka Sani"
    echo -e "\tSoftware Engineering Student,"
    echo -e "\tAfrican Leadership University - Rwanda"
    echo
    echo -e "\t\tOctober 2022"
    exit 0
}

# case of no arguments
if [ $# -eq 0 ]; then
    echo "invalid usage"
    echo "Try 'py -h' for more information."
else
    ARGUMENTS=$(getopt -n py --options ho: --longoptions help,open -- "$@")
    eval set -- "$ARGUMENTS"

    while :; do
        case "$1" in
        -h | help)
            help
            break
            ;;
        -o | open)
            # help
            single_file_to_open="$2"
            shift 2
            break
            ;;
        --)
            shift
            break
            ;;
        \?)
            invalid_option
            exit 2
            ;;
        esac
    done
    if [ "$single_file_to_open" ]; then
        if [ $# -gt 1 ]; then
            echo "more than ONE file to open"
        elif [ -f "$single_file_to_open" ]; then
            echo "file already exists"
        else
            echo -e "#!/usr/bin/python3\n" >"$single_file_to_open"
            chmod u+x "$single_file_to_open"
            vi +startinsert "$single_file_to_open"
        fi
    else
        for FILE in "$@"; do
            if [ -f $FILE ]; then
                echo "$FILE already exists"
            else
                echo -e "#!/usr/bin/python3\n" >"$FILE"
                chmod u+x "$FILE"
            fi
        done
    fi
fi
