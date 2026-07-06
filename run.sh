#!/bin/zsh

# Run a Kotlin LeetCode solution by problem number.
# Source this file once to enable zsh completion for ./run.sh.

typeset -g LEETCODE_RUN_ROOT="${${(%):-%x}:A:h}"

_leetcode_problem_numbers() {
    local solution directory
    local -a numbers

    for solution in "$LEETCODE_RUN_ROOT"/problems/p*/Solution.kt(N); do
        directory="${solution:h:t}"
        numbers+=("${directory#p}")
    done

    _describe 'problem number' numbers
}

_leetcode_run_completion() {
    _arguments \
        '1:problem number:_leetcode_problem_numbers' \
        '*: :'
}

if [[ "$ZSH_EVAL_CONTEXT" == *:file ]]; then
    if (( ! $+functions[compdef] )); then
        autoload -Uz compinit
        compinit
    fi
    compdef _leetcode_run_completion ./run.sh run.sh "$LEETCODE_RUN_ROOT/run.sh"
    return 0
fi

if (( $# != 1 )) || [[ "$1" == '-h' || "$1" == '--help' ]]; then
    print -u2 "usage: ./run.sh <problem-number>"
    print -u2 "example: ./run.sh 1301"
    exit $(( $# == 1 ? 0 : 2 ))
fi

problem_number="${1#p}"
solution="$LEETCODE_RUN_ROOT/problems/p$problem_number/Solution.kt"

if [[ "$problem_number" != <-> ]] || [[ ! -f "$solution" ]]; then
    print -u2 "problem $1 does not exist: $solution"
    exit 2
fi

exec gradle -p "$LEETCODE_RUN_ROOT" run \
    "-PproblemNumber=$problem_number" \
    "-PmainClass=p$problem_number.SolutionKt"
