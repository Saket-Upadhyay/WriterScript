<h6 align="center">
<br>
<img style="margin-bottom:-14px" src="https://raw.githubusercontent.com/Saket-Upadhyay/WriterScript/master/Docs/Images/WSL.png" />
<br>
</h6>
<p align='center'>
 <a href="https://hub.docker.com/r/x64mayhem/writerscript">[Check on DockerHub]</a> <b>|</b> <a href="https://pypi.org/project/writerscript/">[Check on PyPI]</a> <b>|</b> <a href="https://github.com/Saket-Upadhyay/WriterScript/releases/download/BETA/writerscript-0.3.3.tar.gz">[Download Beta Deployment Package v0.3.3]</a>
</p>
  
Syntax
------
WordCount  | brainfuck | description                                   
----------|-----------|-----------------------------------------------
`5`      | **+**         | increment the byte at cell location pointer                
`6`      | **-**        | decrement the byte at cell location pointer                 
`7`    | **\[**         | if pointer is zero, jump to code after matching `8`    
`8`     | **\]**         | if pointer is nonzero, jump to code after matching `7`
`9`    | **>**         | increment the data cell location pointer                    
`10`   | **<**         | decrement the data cell location pointer                      
`11`  | **,**         | input of one byte into cell location pointer              
`12` | **.**         | output the byte at cell location pointer                    

Installation
------------
**Docker (recommended)**
```shell
chmod +x buildDockerImage.sh
./buildDockerImage.sh
. ./dockerAppAlias
wscript_d
```
This will create an alias `wscript_d` which you can use to run wcsript in docker, it also mounts the current directory in docker.

```shell
wscript_d -g -sbf brainfk.txt -stxt data.txt
```

will produce `out.pen` in your current directory which can be run by -
```shell
wscript_d -e -s out.pen
```

If you want to add this alias to your shell, cat the `dockerAppAlias` to your rc file -
```shell
cat dockerAppAlias >> ~/.bashrc
```


**Stable-ish (From PyPI):**
```shell
python3 -m pip install writerscript
```

**Install to Host (From Source) :**
```shell
git clone https://github.com/Saket-Upadhyay/WriterScript.git
cd WriterScript/WriterScript/

python3 setup.py install
```


File Extention
--------------
WriterScript works with `.pen` or `.txt` formats (UTF-8)

Usage
-----
Execute Code (CLI):
```shell
wscript -e -s file.pen
```

Convert BrainFuck to WriterScript:
```shell
wscript -g -sbf sourcebrainfuckfile.txt -stxt templateTextFile.txt
```

How to Create WriterScript code from any text source
---

**Step 1 :** Copy the source to a text file

**Step 2 :** Replace the following elements with null -
```
, -> null
. -> null
r'\n' ->null

r'\[([a-z])*|([0-9])*\]' -> null
```
For Data from WikiPedia :
Remove all [0-9] index by replacing `r'\[[(0-9)]*\]'` with  ` `.
and all [a-z] index by replacing `r'\[[a-z]*\]'` with  ` `.

**For Example** 
```
A programming language is a notation for writing programs, which are specifications of a computation or algorithm.[3] Some authors restrict the term "programming language" to those languages that can express all possible algorithms.[3][4] Traits often considered important for what constitutes a programming language include:

Function and target
  A computer programming language is a language used to write computer programs, which involves a computer performing some kind of computation[5] or algorithm and possibly control external devices such as printers, disk drives, robots,
[6] and so on. For example, PostScript programs are frequently created by another program to control a computer printer or display.
More generally, a programming language may describe computation on some, possibly abstract, machine. It is generally accepted that a complete specification for a programming language includes a description, possibly idealized, of a machine or processor for that language.
[7] In most practical contexts, a programming language involves a computer;
consequently, programming languages are usually defined and studied this way.
[8] Programming languages differ from natural languages in that natural languages are only used for interaction between people, while programming languages also allow humans to communicate instructions to machines.
```

Becomes ->

```
A programming language is a notation for writing programs which are specifications of a computation or algorithm Some authors restrict the term "programming language" to those languages that can express all possible algorithms Traits often considered important for what constitutes a programming language include: Function and target A computer programming language is a language used to write computer programs which involves a computer performing some kind of computation or algorithm and possibly control external devices such as printers disk drives robots and so on For example PostScript programs are frequently created by another program to control a computer printer or display More generally a programming language may describe computation on some possibly abstract machine It is generally accepted that a complete specification for a programming language includes a description possibly idealized of a machine or processor for that language In most practical contexts a programming language involves a computer; consequently programming languages are usually defined and studied this way Programming languages differ from natural languages in that natural languages are only used for interaction between people while programming languages also allow humans to communicate instructions to machines
```

**Step 3 :** Save with `.txt` extention.

**Step 4 :** Save your BrainFuck `oneliner` code as `.txt`


**Step 5 :** Run `wscript -g -sbf brainfuckfile.txt -stxt textfile.txt`

**Step 6 :** `out.pen` file will be created

**Test :** To test the code run `wscript -e -s out.pen` 

Note
---
> I created this project to help myself learn `Theory of Computation and Compiler Design` (5th Semester Course), This project is just for fun and is not associated with any person, organization (academic or non-academic) whatsoever.
> The project is under MIT license, so it can be used as a teaching resource, project, personal use, etc. with proper credits / citation to this repository.

---

<br>
<br>

###### [Check TODO](./Todo.md)
