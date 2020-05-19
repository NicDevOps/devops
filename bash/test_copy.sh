#!/bin/bash
# rpi_build = find ./rpi -name "*rpi*"

# if [ rpi_build != '' ]
# then
#   echo 'Writing new file to pi@rpi!'
#   echo rpi_build
#   #scp rpi_build pi@rpi:~/projects/rpi
# else
#   'no files to copy to pi@rpi!'
# fi

# for FILE in `find ~/projects/devops/rpi/*rpi* -type f`
# do
#   echo FILE
#   #scp FILE pi@rpi:~/projects/rpi
# done

touch 'one.txt' 'two three.txt' 'foo.bmp

list = "$(find . -name \*.txt -o -name \*.bmp -type f)"

for file in $list; do if [ ! -f "$file" ]; then echo "MISSING: $file"; fi; done