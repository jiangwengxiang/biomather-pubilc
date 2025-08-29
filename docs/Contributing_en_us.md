<p align="center">
    <img src="../icons/logo.jpg" width="108" height="108">
</p>
<h1 align="center">Biomather Contribution Guide</h1>

<p align="center" class="language" title="Language selection">
  <b>English(American)</b>  | 
  <a href="../Contributing.md">简体中文</a> | 
  <a href="docs/Contributing_fr_fr.md">Français</a>| 
  <a href="docs/Contributing_zh_tw.md">繁體中文</a>
</p>

# Contribution Guide

We encourage everyone to contribute to the Biomather APP.

If you wish to contribute to this repository, you must carefully read and comply with the following content. Before you start, please be sure to read this guide carefully and understand all its contents. You should also pay attention to the **bolded text** in this guide and the content of the [Development Standards](#development-standards) section.

## Types of Contributions

> ### Icon Contributions

> If anyone wants to contribute icons, please read the [icons-about.md](./icons-about-en-us.md) file carefully to understand how to contribute.

> ### Code Contributions

> If anyone wants to contribute code, please read the following sections carefully.

## Basic Process

The following are the basic steps required to contribute to this repository.

1. You can look for anything that can be improved, including but not limited to code, icons, documentation, etc.

2. Then contact us and inform us of what you want to contribute. After obtaining our consent, you will join our organization and participate in contributing to this repository.

3. You first Fork this repository to your own repository, then Clone your repository to your local machine.

4. Make modifications locally and commit them to your repository. After completing the modifications, create a Pull Request in our organization's repository.

5. Wait for us to review your Pull Request, and if approved, it will be merged.

> [!TIP]
> During this process, please try to use Git command line, Github Desktop, etc. for submission.

## Important Reminders

* If you believe your modifications are of certain importance or magnitude, please describe the update content in the following format and promptly add relevant content to the [update log](./docs/Security_en_us.md):
  
      ```
      v1.4.0 (2025-12-31)
      (Update from @Somebody)
      - Updated...
      - Optimized...
      - Fixed...
      ...
      
      ```

> [!TIP]
> 
> 1. The title should include the version number and main update content.
> 2. The first line of content should indicate the update source.
> 3. The content should elaborate on the update content in a list format.

> [!NOTE]
> 
> 1. **Please do not** arbitrarily select version numbers. If you are not familiar with version number rules, please contact us through the [creator's email](mailto:www.jiang090322@outlook.com) or create a new [issue](https://github.com/Jourious/biomather-pubilc/issues) on GitHub to obtain a version number.
> 2. When updating, **remember** to add relevant content about the update in the update records of the "About biomather APP" application.
> 3. If your modification is of certain importance or magnitude, please add relevant content in the update records.

* According to the relevant laws of the People's Republic of China, you **must not** spread illegal and non-compliant content through this project. Otherwise, once discovered, we will take **locking + possible banning** measures, and we reserve the right to take legal actions and pursue legal responsibilities in all ways at any time.

* You are aware and agree: **To enable better sharing and promotion of the content you contribute, you grant us a worldwide, free, non-exclusive, sublicenseable right to the content you contribute to this project; such content includes but is not limited to written works, artistic works, graphic works, audio-visual works, computer program source code and other content that constitutes "works" under copyright law; such rights include but are not limited to reproduction, translation, arrangement, compilation, annotation, adaptation, information network dissemination, distribution and other copyrights and related rights, and such rights shall at least cover the rights and licenses for the "biomather APP" project or part or all of the relevant content developed in other ways.**

## Development Standards

### Python Development Standards

1. We have the following regulations for internally tested Python files:
   
   * 1. Beginning standards
        Please refer to the code standards at the beginning of `app-bate-v0.1.0.py`([click to jump](../app-py/app-bate-v0.1.0.py)) and read them carefully.
   
   * 2. Please develop according to the following code style:
   
   ```python
      sum = 0
      for i in range(10):
         sum = sum + i
      print(sum)
   ```
   
   * 3. For function and variable naming, please use underscore naming convention, such as:
        *  user_name
        *  user_password
        *  user_age
   
   * 4. For class or module names, please use camel case naming convention, such as:
        *  jsonParser
        *  widget
   
   * 5. For other code standard regulations:
        
        * 1. For code that does not need to be expanded, try to compress it into one line
        
        * 2. For lines that need indentation, please be sure to keep the indentation as 4 spaces
        
        * 3. For inline comments, please use # at the beginning and keep it on the same line as the code to be commented, such as:
             ```python
             sum = 0  # This is a comment ```
        
        * 4. For function and class comments, please use """ at the beginning and occupy one or more lines separately, such as:
              
             ```python
             def func():
             """
             This is a function
             """
             print("hello world")
             ```

### C++ Development Standards

* Note: The version developed in C++ belongs to the public beta or official version, so please take C++ development seriously

* Reminder: The current C++ version has not been developed yet. If you want to contribute C++ code, please be sure to contact us to confirm that the development you are doing does not overlap with others.

1. We have the following regulations for header files:
    Please be sure to write header files in the following format:
   
   ```cpp
   #ifndef __HEADER_H__
   #define __HEADER_H__
   ```

2. Regarding C++ code style, please develop according to the following example:
   
   ```cpp
   #include <iostream>
   using namespace std;
   
   void massage(), line();
   
   int main()
   {
       cout << "maybe I hate writing C++!" << endl;
       massage();
       line();
       cout << "this is too difficult to learn !" << endl;
       line();
       return 0;
   }
   
   void massage()
   {
       cout << "C++ is a language that too many people dislike to learn !" << endl;
   }
   
   void line()
   {
       cout << "------------------------------------------" << endl;
   }
   ```

3. For function names, variable names, class names, and module names, please keep them consistent with Python's development specifications. (Not repeated here)

4. For other specifications, we have the following regulations:
   
   * 1. The first to second points are consistent with the Python development specifications mentioned above.
   
   * 2. For inline comments, please use // at the beginning and keep it on the same line as the code to be commented, such as:
        
        ```cpp
        int sum = 0; // This is a comment
        ```
   
   * 3. For function and class comments, please use /** at the beginning and end with */, and you can use multi-line or single-line comments such as:
        
        ```cpp
        /**
        * This is a function
        */
        void func()
        {
           cout << "hello world" << endl;
        }
        ```
