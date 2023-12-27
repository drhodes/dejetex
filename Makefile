SHELL = bash
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

# -----------------------------------------------------------------------------
# Section: Python

# Ensure the system python is not used, maintain a virtual
# environment.

VENV = source venv/bin/activate &&

# to run a python script use the following incantation:
#   ${PY} a-python-script.py

PY = ${VENV} python3

venv: requirements.txt ## establish a virtual environment for python
	python3 -m venv venv && \
	${VENV} pip install -r requirements.txt
	touch venv


ANTLR_VERSION=4.13.1
# ANTLR_JAR=antlr-${ANTLR_VERSION}-complete.jar
# ANTLR_URL=https://www.antlr.org/download/${ANTLR_JAR}
# ANTLR=util/${ANTLR_JAR}

# ${ANTLR}:
# 	curl -O ${ANTLR_URL}
# 	mv ${ANTLR_JAR} util


# -----------------------------------------------------------------------------
# Section: Parser

GRAMMAR = DejeTex
SRCDIR = dejetex

PARSER_FILES = \
	${SRCDIR}/${GRAMMAR}Lexer.interp \
	${SRCDIR}/${GRAMMAR}Lexer.tokens \
	${SRCDIR}/${GRAMMAR}.py \
	${SRCDIR}/${GRAMMAR}.interp \
	${SRCDIR}/${GRAMMAR}Lexer.py \
	${SRCDIR}/${GRAMMAR}Listener.py \
	${SRCDIR}/${GRAMMAR}Visitor.py \
	${SRCDIR}/${GRAMMAR}.tokens

${PARSER_FILES}: venv ${GRAMMAR}.g4 ${GRAMMAR}Lexer.g4
	${VENV} antlr4 \
	-v ${ANTLR_VERSION} \
	-o ${SRCDIR} \
	-visitor \
	-Dlanguage=Python3 \
	${GRAMMAR}Lexer.g4 ${GRAMMAR}.g4

test: ${PARSER_FILES}
	${PY} -m pytest --capture=no

tree: venv
	${VENV} antlr4-parse -v ${ANTLR_VERSION} DejeTex.g4 DejeTexLexer.g4 ${RULE} tests/deje-tests/${TESTPROG} -trace -gui

.PHONY: clean-antlr
clean-antlr: 
	rm -f ${PARSER_FILES}

.PHONY: clean-python
clean-python:
	rm -rf venv
	rm -rf __pycache__


.PHONY: clean-all
clean-all: clean-antlr clean-python
