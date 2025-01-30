cd /c/Users/christian/Downloads/bashcrawl-stable-2024.02.09/entrance
cat scroll
ls
cd cellar
ls
cd treasure
cd armoury/
ls
cd chamber/
ls
less spell
cd /c/Users/christian/Downloads/bashcrawl-stable-2024.02.09/entrance
cat scroll
ls
cd cellar/
ls
cat scroll
cd armoury/
ls
cat potion
unalias ls
ls -F
alias ls='ls -F'
cat scroll
./treasure
export I="sword,$I"
echo $I
alias inv='echo $I'
inv
cd ..
ls
./treasure
export I="amulet,$I"
inv
cd armoury/
ls
./potion
export HP=20
alias hp='echo $HP'
hp
cd chamber/
ls
cat scroll
./treasure
export I="coins,$I"
inv
ls
./statue
let "HP=HP-7"
hp
ls
./spell
ln -fs ../../../chapel/courtyard/aviary/hall portal
ls
cat scroll
cd portal/
ls
cd library/
ls
cat scroll
./tome
cd ..
ls
./monster
ls
./treasure
export I="crown,$I"
inv
./carcass
cd library/
ls
./tome
cd ..
ls
./treasure
cd ..
ls
cd vault/
ls
./glass
cat scroll
cd stronghold/
ls
