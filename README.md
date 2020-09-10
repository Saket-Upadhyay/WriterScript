<h6 align="center">
<br>
<img style="margin-bottom:-14px" src="Docs/Images/WSL.png" />
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

---

Work In Progress
<br>
#### [Download Beta Deployment Package](https://github.com/Saket-Upadhyay/WriterScript/releases/download/v0.2.1-beta/writerscript-0.2.1.tar.gz)

<br>

###### [Check TODO](./Todo.md)
