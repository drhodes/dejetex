
# dejetex, a context free subset of latex.

``` latex
% progress

\begin{edxvertical}
  \begin{edxtext}
    \sum{a+b}_{i=1}^{\infty}
    Lorem ipsum 
    \begin{itemize} 
    \item{Pellentesque} % this is a comment
    \item{Proin}
    \end{itemize}
    
  \end{edxtext}
\end{edxvertical}
```





## Project Goals

Problem: Debugging latex can be a pain because there is no formal
grammar for which to build tools upon. 

Goal: To define a grammar and implement a parser with associated tools
for a substantial subset of $\LaTeX$. The grammar adds an unsafe
environment for unchecked latex, which the tools will simply ignore.


## Benefits: 

Users will enjoy ameneties such as:

    - syntax errors
    - linter
    - are environments closed? if not where?
    - macro tracing
    
Possible features:

    - treesitter integration
    - goto definition


## NonGoals : 

Reimplementing the latex ecosystem


----

## How is this going to work?

https://tex.stackexchange.com/questions/58269/how-does-latex-implement-environments

Sat 30 Dec 2023 12:23:53 PM EST

So, some reasonable floor needs to be established, and I believe that
will be with `\newcommand`, but time will tell.

\newenvironment{<env-name>}[<n-args>][<default>]{<begin-code>}{<end-code>} 


\newcommand{\<env-name>}[<n-args>][<default>]{<begin-code>}
\newcommand{\end<env-name>}{<end-code>}



