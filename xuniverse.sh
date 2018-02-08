#!/bin/sh
BASE="`realpath "$0"`"
BASE="`dirname "$BASE"`"
if [ -x "${BASE}/.xuniverse.run" ]; then
	"${BASE}/.xuniverse.run"
	exit $?
fi

python -m xuniverse

