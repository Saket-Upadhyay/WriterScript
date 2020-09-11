<h6 align="center">
<br>
<img style="margin-bottom:-14px" src="https://raw.githubusercontent.com/Saket-Upadhyay/WriterScript/master/Docs/Images/WSL.png" />
<br>
</h6>

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
Beta :
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
Remove all [0-9] index by replacing `r'\[[0-9][0-9]\]'` with  ` `.
and all [a-z] index by replacing `r'\[[a-z][a-z]\]'` with  ` `.

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
> The project is under MIT license, so it can be used as a teaching resource, other projects, etc. with proper citation to this repository.

---

Work In Progress
<br>
#### [Download Beta Deployment Package](https://github.com/Saket-Upadhyay/WriterScript/releases/download/v0.2.1-beta/writerscript-0.2.1.tar.gz)

<br>

###### [Check TODO](./Todo.md)
