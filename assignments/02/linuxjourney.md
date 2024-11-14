1. Try some other Linux commands and see what they output:
$ date
$ whoami

Output:
$date Wed Nov 13 16:14:30 WEST 2024
$whoami Joshua Christian

2. Run the cd command without any flags, where does it take you?

Output:
/c/Users

3. Run ls with different flags and see the output you receive.

Output:
$ ls -r
 ntuser.ini         Videos/       'Saved Games'/      OneDrive/                                                                                      NTUSER.DAT         IntelGraphicsProfiles/   Desktop/
 ntuser.dat.LOG2    Templates@     Recent@            NetHood@                                                                                      'My Documents'@     IdeaProjects/            Cookies@
 ntuser.dat.LOG1   'Start Menu'@   PycharmProjects/   NTUSER.DAT{2ecc2ab7-ec44-11ed-98c2-f56ed1f8193b}.TMContainer00000000000000000002.regtrans-ms   Music/             Favorites/               Contacts/
 mysuperduperfile   SendTo@        PrintHood@         NTUSER.DAT{2ecc2ab7-ec44-11ed-98c2-f56ed1f8193b}.TMContainer00000000000000000001.regtrans-ms  'Local Settings'@   Downloads/              'Application Data'@
 ansel/             Searches/      Pictures/          NTUSER.DAT{2ecc2ab7-ec44-11ed-98c2-f56ed1f8193b}.TM.blf                                        Links/             Documents/               AppData/

$ ls -t
 Downloads/         IntelGraphicsProfiles/   Music/                                                    Cookies@                                                                                       SendTo@
 mysuperduperfile   PycharmProjects/         Contacts/                                                'Local Settings'@                                                                              'Start Menu'@
 Documents/         Pictures/                Favorites/                                                NTUSER.DAT{2ecc2ab7-ec44-11ed-98c2-f56ed1f8193b}.TMContainer00000000000000000001.regtrans-ms   Templates@
 OneDrive/         'Saved Games'/            ntuser.ini                                                NTUSER.DAT{2ecc2ab7-ec44-11ed-98c2-f56ed1f8193b}.TMContainer00000000000000000002.regtrans-ms   ntuser.dat.LOG1
 Videos/            IdeaProjects/            AppData/                                                  NetHood@                                                                                       ntuser.dat.LOG2
 NTUSER.DAT         Searches/                NTUSER.DAT{2ecc2ab7-ec44-11ed-98c2-f56ed1f8193b}.TM.blf   PrintHood@                                                                                    'My Documents'@
 Desktop/           Links/                  'Application Data'@                                        Recent@                                                                                        ansel/

4. Create a new file
Note the timestamp
Touch the file and check the timestamp once again

Output:
$ ls -l mysuperduperfile
-rw-r--r-- 1 Joshua Christian 197121 0 Nov 13 17:17 mysuperduperfile

$ ls -l mysuperduperfile
-rw-r--r-- 1 Joshua Christian 197121 0 Nov 13 23:23 mysuperduperfile

5. Run cat on different files and directories. Then try to cat multiple files.

Output:
$ cat mysuperduperfile myfile

6. History

Output:
$ history
    1  l
    2  ls
    3  touch mysuperduperfile
    4  ls -l
    5  man
    6  date
    7  whoami
    8  cd
    9  cd
   10  pwd
   11  cd /c/Users/Joshua Christian/Desktop
   12  cd
   13  cd /c/Users/
   14  pwd
   15  cd /c/Users/Joshua Christian
   16  cd /c/Users/Joshua Christian/
   17  cd /Users/Joshua Christian/Desktop
   18  cd /Users/Joshua Christian/Desktop
   19  /Users/Joshua Christian/Desktop/
   20  /Users/Joshua Christian
   21  /Users/Joshua Christian/
   22  pwd
   23  ls -R
   24  ls -r
   25
   26  ls -t
   27  touch mysuperduperfile
   28  ls
   29  ls -l mysuperduperfile
   30  touch mysuperduperfile
   31  ls -l mysuperduperfile
   32  touch myfile
   33  cat myfile mysuperduperfile
   34  l
   35  ls
   36  file mysuperduperfile
   37  cat mysuperduperfile myfile
   38  pwd
   39  cd mysuperduperfile
   40  cd /c/Desktop
   41  cd /c/Desktop/
   42  ls
   43  history

7. Copy over a couple of files, be careful not to overwrite anything important.

Output:
$ cp mysuperduperfile /c/Users/Joshua Christian/Documents/cooldocs


8. Rename a file, then move that file to a different directory.

Output:
$ mv myfile mynewfile
$ mv mynewfile /c/Users/Joshua Christian/Documents

9. Run less on a file, then page up and around the file. Try searching for a specific word. Quickly navigate to the beginning or the end of the file.

Output:
$ less 

10. Run the file command on a few different directories and files and note the output.

Output:
$ file chess.jpeg
chess.jpeg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, progressive, precision 8, 1260x708, components 3

11. Create a file called -file (don't forget the dash!).
Remove that file.

Output:
$ touch -file
$ rm -file

12. Find a file from the root directory that has the word net in it.

Output:
$ find /c/ -name net

13. Run help on the echo command, logout command and pwd command.

Output:
$ help echo
echo: echo [-neE] [arg ...]
    Write arguments to the standard output.

    Display the ARGs, separated by a single space character and followed by a
    newline, on the standard output.

    Options:
      -n        do not append a newline
      -e        enable interpretation of the following backslash escapes
      -E        explicitly suppress interpretation of backslash escapes

    `echo' interprets the following backslash-escaped characters:
      \a        alert (bell)
      \b        backspace
      \c        suppress further output
      \e        escape character
      \E        escape character
      \f        form feed
      \n        new line
      \r        carriage return
      \t        horizontal tab
      \v        vertical tab
      \\        backslash
      \0nnn     the character whose ASCII code is NNN (octal).  NNN can be
                0 to 3 octal digits
      \xHH      the eight-bit character whose value is HH (hexadecimal).  HH
                can be one or two hex digits
      \uHHHH    the Unicode character whose value is the hexadecimal value HHHH.
                HHHH can be one to four hex digits.
      \UHHHHHHHH the Unicode character whose value is the hexadecimal value
                HHHHHHHH. HHHHHHHH can be one to eight hex digits.

    Exit Status:
    Returns success unless a write error occurs.

$ help logout
logout: logout [n]
    Exit a login shell.

    Exits a login shell with exit status N.  Returns an error if not executed
    in a login shell.

$ help pwd
pwd: pwd [-LPW]
    Print the name of the current working directory.

    Options:
      -L        print the value of $PWD if it names the current working
                directory
      -P        print the physical directory, without any symbolic links
      -W        print the Win32 value of the physical directory

    By default, `pwd' behaves as if `-L' were specified.

    Exit Status:
    Returns 0 unless an invalid option is given or the current directory
    cannot be read.


