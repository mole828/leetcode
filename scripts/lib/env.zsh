# Shared bootstrap for commands; resolve configuration beside the repository,
# independently of the current working directory.
_leetcode_load_env() {
  local repository="${${(%):-%x}:A:h:h:h}"
  local assignments setting
  assignments=$(node "$repository/scripts/lib/env.cjs" "$repository") || return $?
  for setting in "${(@0)assignments}"; do
    [[ -n "$setting" ]] && export "$setting"
  done
  export LEETCODE_ROOT="${LEETCODE_ROOT:-$repository}"
  # A relative override is interpreted from this repository, never from $PWD.
  if [[ "$LEETCODE_ROOT" != /* ]]; then
    export LEETCODE_ROOT="$repository/$LEETCODE_ROOT"
  fi
  if [[ -n "${LEETCODE_CLI:-}" && "$LEETCODE_CLI" != /* ]]; then
    export LEETCODE_CLI="$repository/$LEETCODE_CLI"
  fi
}
_leetcode_load_env
