# Thanks to https://github.com/highlightjs/highlight.js/blob/main/SUPPORTED_LANGUAGES.md
COMMON_EXTS = {
    "as" : "as",
    "adb" : "ada",
    "ada" : "ada",
    "ads" : "ada",
    "applescript" : "osascript",
    "scpt" : "osascript",
    "asciidoc" : "adoc",
    "adoc" : "adoc",
    "asc" : "adoc",
    "aj" : "aspectj",
    "ahk" : "autohotkey",
    "ahkl" : "autohotkey",
    "au3" : "autoit",
    "awk" : "awk",
    "auk" : "awk",
    "gawk" : "awk",
    "mawk" : "awk",
    "nawk" : "awk",
    "b" : "bf",
    "bf" : "bf",
    "c" : "c",
    "cats" : "c",
    "h" : "c",
    "idc" : "c",
    "w" : "c",
    "cs" : "cs",
    "cake" : "cs",
    "cshtml" : "cs",
    "csx" : "cs",
    "cpp" : "cc",
    "c++" : "cc",
    "cc" : "cc",
    "cp" : "cc",
    "cxx" : "cc",
    "h" : "cc",
    "h++" : "cc",
    "hh" : "cc",
    "hpp" : "cc",
    "hxx" : "cc",
    "inc" : "cc",
    "inl" : "cc",
    "ipp" : "cc",
    "tcc" : "cc",
    "tpp" : "cc",
    "cmake" : "cmake",
    "cmake.in" : "cmake",
    "css" : "css",
    "clj" : "clj",
    "boot" : "clj",
    "cl2" : "clj",
    "cljc" : "clj",
    "cljs" : "clj",
    "cljs.hl" : "clj",
    "cljscm" : "clj",
    "cljx" : "clj",
    "hic" : "clj",
    "coffee" : "cson",
    "_coffee" : "cson",
    "cake" : "cson",
    "cjsx" : "cson",
    "cson" : "cson",
    "iced" : "cson",
    "coq" : "coq",
    "v" : "coq",
    "cr" : "cr",
    "d" : "d",
    "di" : "d",
    "dart" : "dart",
    "diff" : "diff",
    "patch" : "diff",
    "dockerfile" : "docker",
    "ex" : "elixir",
    "exs" : "elixir",
    "elm" : "elm",
    "erl" : "erl",
    "es" : "erl",
    "escript" : "erl",
    "hrl" : "erl",
    "xrl" : "erl",
    "yrl" : "erl",
    "fs" : "fs",
    "fsi" : "fs",
    "fsx" : "fs",
    "golo" : "golo",
    "go": "go",
    "gradle" : "gradle",
    "groovy" : "groovy",
    "grt" : "groovy",
    "gtpl" : "groovy",
    "gvy" : "groovy",
    "http" : "http",
    "haml" : "haml",
    "haml.deface" : "haml",
    "handlebars" : "hbs",
    "hbs" : "hbs",
    "hs" : "hs",
    "hsc" : "hs",
    "hx" : "hx",
    "hxsl" : "hx",
    "hy" : "hy",
    "json" : "json",
    "geojson" : "json",
    "lock" : "json",
    "topojson" : "json",
    "java" : "jsp",
    "js" : "js",
    "_js" : "js",
    "bones" : "js",
    "es" : "js",
    "es6" : "js",
    "frag" : "js",
    "gs" : "js",
    "jake" : "js",
    "jsb" : "js",
    "jscad" : "js",
    "jsfl" : "js",
    "jsm" : "js",
    "jss" : "js",
    "njs" : "js",
    "pac" : "js",
    "sjs" : "js",
    "ssjs" : "js",
    "sublime-build" : "js",
    "sublime-commands" : "js",
    "sublime-completions" : "js",
    "sublime-keymap" : "js",
    "sublime-macro" : "js",
    "sublime-menu" : "js",
    "sublime-mousemap" : "js",
    "sublime-project" : "js",
    "sublime-settings" : "js",
    "sublime-theme" : "js",
    "sublime-workspace" : "js",
    "sublime_metrics" : "js",
    "sublime_session" : "js",
    "xsjs" : "js",
    "xsjslib" : "js",
    "jl" : "julia",
    "kt" : "kt",
    "ktm" : "kt",
    "kts" : "kt",
    "lasso" : "ls",
    "las" : "ls",
    "lasso8" : "ls",
    "lasso9" : "ls",
    "ldml" : "ls",
    "less" : "less",
    "ls" : "ls",
    "_ls" : "ls",
    "lua" : "lua",
    "fcgi" : "lua",
    "nse" : "lua",
    "pd_lua" : "lua",
    "rbxs" : "lua",
    "wlua" : "lua",
    "mak" : "mk",
    "d" : "mk",
    "mk" : "mk",
    "mkfile" : "mk",
    "md" : "md",
    "markdown" : "md",
    "mkd" : "md",
    "mkdn" : "md",
    "mkdown" : "md",
    "ron" : "md",
    "mathematica" : "wl",
    "cdf" : "wl",
    "m" : "wl",
    "ma" : "wl",
    "mt" : "wl",
    "nb" : "wl",
    "nbp" : "wl",
    "wl" : "wl",
    "wlt" : "wl",
    "matlab" : "matlab",
    "m" : "matlab",
    "m" : "mercury",
    "moo" : "mercury",
    "monkey" : "monkey",
    "nsi" : "nsis",
    "nsh" : "nsis",
    "nginxconf" : "nginx",
    "vhost" : "nginx",
    "nix" : "nix",
    "ml" : "ml",
    "eliom" : "ml",
    "eliomi" : "ml",
    "ml4" : "ml",
    "mli" : "ml",
    "mll" : "ml",
    "mly" : "ml",
    "scad" : "scad",
    "oxygene" : "oxygene",
    "php" : "php",
    "aw" : "php",
    "ctp" : "php",
    "fcgi" : "php",
    "inc" : "php",
    "php3" : "php",
    "php4" : "php",
    "php5" : "php",
    "phps" : "php",
    "phpt" : "php",
    "pl" : "pl",
    "al" : "pl",
    "cgi" : "pl",
    "fcgi" : "pl",
    "perl" : "pl",
    "ph" : "pl",
    "plx" : "pl",
    "pm" : "pl",
    "pod" : "pl",
    "psgi" : "pl",
    "t" : "pl",
    "pony" : "pony",
    "ps1" : "ps",
    "psd1" : "ps",
    "psm1" : "ps",
    "pde" : "processing",
    "pl" : "prolog",
    "pro" : "prolog",
    "prolog" : "prolog",
    "yap" : "prolog",
    "pp" : "pp",
    "py" : "py",
    "bzl" : "py",
    "cgi" : "py",
    "fcgi" : "py",
    "gyp" : "py",
    "lmi" : "py",
    "pyde" : "py",
    "pyp" : "py",
    "pyt" : "py",
    "pyw" : "py",
    "rpy" : "py",
    "tac" : "py",
    "wsgi" : "py",
    "xpy" : "py",
    "qml" : "qml",
    "qbs" : "qml",
    "r" : "r",
    "rd" : "r",
    "rsx" : "r",
    "rb" : "rb",
    "builder" : "rb",
    "fcgi" : "rb",
    "gemspec" : "rb",
    "god" : "rb",
    "irbrc" : "rb",
    "jbuilder" : "rb",
    "mspec" : "rb",
    "pluginspec" : "rb",
    "podspec" : "rb",
    "rabl" : "rb",
    "rake" : "rb",
    "rbuild" : "rb",
    "rbw" : "rb",
    "rbx" : "rb",
    "ru" : "rb",
    "ruby" : "rb",
    "thor" : "rb",
    "watchr" : "rb",
    "rs" : "rs",
    "rs.in" : "rs",
    "sas" : "SAS",
    "scss" : "scss",
    "sql" : "sql",
    "cql" : "sql",
    "ddl" : "sql",
    "inc" : "sql",
    "prc" : "sql",
    "tab" : "sql",
    "udf" : "sql",
    "viw" : "sql",
    "scala" : "scala",
    "sbt" : "scala",
    "sc" : "scala",
    "scm" : "scheme",
    "sld" : "scheme",
    "sls" : "scheme",
    "sps" : "scheme",
    "ss" : "scheme",
    "sci" : "sci",
    "sce" : "sci",
    "tst" : "sci",
    "sh" : "shell",
    "bash" : "shell",
    "bats" : "shell",
    "cgi" : "shell",
    "command" : "shell",
    "fcgi" : "shell",
    "ksh" : "shell",
    "sh.in" : "shell",
    "tmux" : "shell",
    "tool" : "shell",
    "zsh" : "shell",
    "smali" : "smali",
    "st" : "st",
    "cs" : "st",
    "stan" : "stan",
    "do" : "stata",
    "ado" : "stata",
    "doh" : "stata",
    "ihlp" : "stata",
    "mata" : "stata",
    "matah" : "stata",
    "sthlp" : "stata",
    "styl" : "styl",
    "swift" : "swift",
    "tcl" : "tk",
    "adp" : "tk",
    "tm" : "tk",
    "thrift" : "thrift",
    "twig" : "twig",
    "ts" : "ts",
    "tsx" : "ts",
    "vhdl" : "vhdl",
    "vhd" : "vhdl",
    "vhf" : "vhdl",
    "vhi" : "vhdl",
    "vho" : "vhdl",
    "vhs" : "vhdl",
    "vht" : "vhdl",
    "vhw" : "vhdl",
    "vala" : "vala",
    "vapi" : "vala",
    "v" : "v",
    "veo" : "v",
    "xquery" : "xq",
    "xq" : "xq",
    "xql" : "xq",
    "xqm" : "xq",
    "xqy" : "xq",
    "yml" : "yml",
    "reek" : "yml",
    "rviz" : "yml",
    "sublime-syntax" : "yml",
    "syntax" : "yml",
    "yaml" : "yml",
    "yaml-tmlanguage" : "yml",
    "zep" : "zep",
    "txt" : ""
}