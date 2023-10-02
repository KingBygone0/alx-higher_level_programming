
<p align="center">  
<img src ="https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png">
</p>

<h1 align="center">
	Python is EASY
</h1>

>Learning C right now, been wanting to get on this. It's going to be FUN !!.

>If you need any **help**. Please do not hesitate to get in touch with me in our <a href="https://twitter.com/kingbygone">King on Twitter</a>.


----

## About
- This repository consists of all the C programming projects done with [ALX Africa](https://www.alxafrica.com/) Full stack Software Engineering course in partnership with [ALX SE](https:/alxafrica.com/).
- All main.c files are prewritten by the school. We build functions that produce a specific output while also taking into consideration edge cases.

----


## Content table

- [0x00](./0x00-python-hello_world) : Python Hello, World.



----

## Python Program Compilation

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:572/1*cLTFQXZbzxZIdVXSXhGM7g.gif" />
</p>

The compilation process has four different steps:
1. The preprocessing stage
2. The compiling stage
3. The assembling stage
4. The linking stage
    
### Step 1: Preprocessing `-E`
The preprocessor reads the source code and performs various transformations to it:
- Expanding macros (replacing all of the macros with their values)
- Handling include files (replaces the #include macro with the content of the header file specified in <>)
- Removing comments
- The results in a new file called a translation unit stored in a file with `.i` extension (intermediate)
    
### Step 2: Compiling `-S`
The build phase provides us with assembly code that is unique to the target architecture.

In this step the compiler takes action by taking a preprocessed file which checks for syntax or structure errors (in case of errors the compilation process stops and displays the corresponding errors). After compiling it, it generates an intermediate code in assembly language `file.s`.

### Step 3: Assembing `-c`
In the third stage of compilation, an assembler is used to convert assembly language into machine code. The assembler takes the code and generates an object file `file.o`, which contains machine code that is not yet executable because it needs to be mapped to a specific memory address. The linker combines all the object files, resolves references between modules, and corrects the addresses, creating an executable file.

### Step 4: Linking
The linker is an important tool in compilation that performs two tasks: resolution and relocation of symbols. It arranges the pieces of object code so that functions in one piece can successfully call functions in others. The linker also adds parts that contain the instructions for the library functions used by the program. The result of this stage is the executable file. usually `a.out` if `-o` is not specified.

---

## Author

- [`@KingBygone0`]() | Software Engineer Student

    > Reach out to me if you need any help or have any questions.

	<a href="mailto:kingbygone@icloud.com">
		<img alt="Feel free to contact me" src="https://img.shields.io/badge/-Ask_me_anything-blue?style=flat&logo=Gmail&logoColor=white&link=mailto:kingbygone@gmail.com&color=3d85c6" />
	</a>
	<span> * </span>
    <a href="https://www.linkedin.com/in/kingbygone/">
        <img alt="Linkedin Profile" src="https://img.shields.io/badge/-Linkedin-0072b1?style=flat&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/achrafelkhnissi/" />
    </a>
    <span> * </span>
    <a href="https://twitter.com/KingBygone">
        <img alt="Twitter Profile" src="https://img.shields.io/badge/-Twitter-0072b1?style=flat&logo=Twitter&logoColor=white&link=https://www.linkedin.com/in/kingbygone/&color=1DA1F2" />
    </a>
    <span> * </span>
    <a href="#">
        <img alt="Discord Profile" src="https://img.shields.io/badge/-Discord-0072b1?style=flat&logo=Discord&logoColor=white&link=#/&color=7289da" />
    </a>
---
