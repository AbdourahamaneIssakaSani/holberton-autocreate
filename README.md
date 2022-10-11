# holberton autocreate

## Requirements

- [Linux](https://www.linux.org/) or [WSL](https://learn.microsoft.com/en-us/windows/wsl/)
- [Git](https://git-scm.com/)

## Installation

```sh
git clone https://github.com/AbdourahamaneIssakaSani/holberton-autocreate.git && cd holberton-autocreate && ./install
```

## Overview

After the installation process, type the following command:

```sh
ha
```

## Usage

1. push your file to GitHub

   You can achieve this with the `pu` command. Type `pu -h` to know more. Find examples below:

   - to commit and push all files you changed, just type

   ```sh
   pu
   ```

   - to commit and push a single file called `file1`

   ```sh
   pu file1
   ```

   - to commit and push the files `file1` and `file2` (as many files as you want)

   ```sh
   pu file1 file2
   ```

   A default commit message is provided. To override it, use `-m=MESSAGE` option like this:

   ```sh
   pu -m "custom commit message"
   ```

   or with the specific file

   ```sh
    pu -m "custom commit message" file1
   ```

2. Create a javascript file

   To create a javascript file with `execute rights` and starting with `#!/usr/bin/node`, use the `js` command. Type `js -h` to know more. Find examples below:

   - to create the file named `0-rectangle.js`

   ```sh
   js 0-rectangle.js
   ```

   - to create the file named `0-rectangle.js` and open it in insert mode, use `-o` option (only for on file)

   ```sh
   js -o 0-rectangle.js
   ```

   - to create the files named `0-rectangle.js` and `1-rectangle.js` (as many files as you want)

   ```sh
   js 0-rectangle.js 1-rectangle.js
   ```

3. Create a python file

   To create a python file with `execute rights` and starting with `#!/usr/bin/python3`, use the `py` command. Type `py -h` to know more. Find examples below:

   - to create the file named `0-square.py`

   ```sh
   py 0-square.py
   ```

   - to create the file named `0-square.py` and open it in insert mode, use `-o` option (only for on file)

   ```sh
   py -o 0-square.py
   ```

   - to create the files named `0-square.py` and `1-square.py` (as many files as you want)

   ```sh
   py 0-square.py 1-square.py
   ```

4. Create a bash file

   To create a bash file with `execute rights` and starting with `#!/bin/bash`, use the `sh` command. Type `sh -h` to know more. Find examples below:

   - to create the file named `0-current_working_directory`

   ```sh
   sh 0-current_working_directory
   ```

   - to create the file named `0-current_working_directory` and open it in insert mode, use `-o` option (only for on file)

   ```sh
   sh -o 0-current_working_directory
   ```

   - to create the files named `0-current_working_directory` and `1-listit` (as many files as you want)

   ```sh
   sh 0-current_working_directory 1-listit
   ```

5. Create an env bash file

   To create a bash file with `execute rights` and starting with `#!/usr/bin/env bash`, use the `vh` command. Type `vh -h` to know more. Find examples below:

   - to create the file named `1-for_best_school`

   ```sh
   sh 1-for_best_school
   ```

   - to create the file named `1-for_best_school` and open it in insert mode, use `-o` option (only for on file)

   ```sh
   sh -o 1-for_best_school
   ```

   - to create the files named `1-for_best_school` and `2-while_best_school` (as many files as you want)

   ```sh
   sh 1-for_best_school 2-while_best_school
   ```

## To uninstall

If you want to remove all commands of Holberton autocreate, you can remove the files `ha`, `pu`, `js`, `py`, `sh`, `vh` located in `~/bin` directory and type
in your terminal

```sh
source ~/.profile
```

or go in the repository folder `holberton-autocreate` and type the following:

```sh
./uninstall
```

## NOTE

I created this project for African Leadership University and ALX Africa students or anyone taking the Holberton School Program of Software Engineering. Using it will help you save at least 60% of your time by preventing you from typing some commands irrelevant to the learning objective. That is why I do not recommend it to someone who is not yet familiar with the shebang, `chmod`, `git add`, `git commit`, `git push`. Use it if you have passed the assessment **_Shell - Processes & Signals_**. - Abissa
