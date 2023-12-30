
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

Users will enjoy futuristic ameneties such as:

    - syntax errors
    
Possible features:

    - syntax highlighting
    - goto definition


## NonGoals : 

Reimplementing the latex ecosystem
