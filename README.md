# lua-smudger
Reindents Lua code during git checkout/commit

# Goal

You prefer using indents with 2/3/4-space indents, but project standard is 2/3/4 spaces.  This will convert to and fro for you, using git smudge/clean

# To install/configure

## Pre-requisites

* have python installed, and available at /usr/bin/python (or modify the first line of lua_indents.py so it is true)

## .gitattributes

Create a file ~/.gitattributes, and add the following lines:

```
*.lua filter=luaindent
```

## .gitconfig

In your ~/.gitconfig file, add following lines:

```
[filter "luaindent"]
	smudge = /path/to/lua_indents.py indent=3
	clean = /path/to/lua_indents.py indent=2

[core]
	attributesfile = /path/to/.gitattributes
```

Notes:
* Replace anything with `/path/to` with the appropriate path.
* You can configure the indentation in the [filter] section above.  In this case above, the repo has 3 spaces, and you see 2 spaces.

## lua_indents.py

Make sure it is executable

# Issues?

Raise an issue, in issue page of this repo.

# License

BSD2

