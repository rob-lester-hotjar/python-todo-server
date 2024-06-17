#!/bin/bash

case "$1" in
    run)
        exec python -m todo ${@:2}
    ;;
    test)
        exec pytest ${@:2}
    ;;
    *)
        exec "$@"
esac
