Changelog
=========

v0.4.0 (*unreleased*)
---------------------


v0.3.5 (26 July 2022)
---------------------
- officially support python 3.10 (:pull:`115`)
- colorize removed trailing whitespace (:pull:`120`)
- write only if the content of a file changed (:issue:`127`, :pull:`128`)
- don't crash on strings with trailing empty strings (`"a"""`) (:issue:`131`, :pull:`132`)

v0.3.4 (17 July 2021)
---------------------
- declare the ``tomli`` library as a runtime dependency (:pull:`101`)

v0.3.3 (06 February 2021)
-------------------------
- don't crash on malformed rst directives (:issue:`78`, :pull:`79`)

v0.3.2 (05 January 2021)
------------------------
- don't strip newlines immediately before eol (:pull:`73`)

v0.3.1 (04 December 2020)
-------------------------
- don't detect comments ending with a colon as a block (:issue:`67`, :pull:`68`)
- don't add color to redirected output and print reports to ``stderr`` (:issue:`66`, :pull:`69`)
- add a nightly CI which also runs every day at 00:00 UTC (:pull:`71`)

v0.3 (04 November 2020)
-----------------------
- support running on python 3.9 (the target version is not yet supported by black)
  (:pull:`55`, :pull:`57`)
- add diff and color diff modes (:issue:`33`, :issue:`53`, :pull:`56`)
- support `black`'s string normalization option (:issue:`33`, :pull:`59`)
- add colors to the output (:issue:`33`, :pull:`60`)
- make the order of the printed files predictable (:pull:`61`)
- make sure blocks end with a empty continuation line (:issue:`52`, :pull:`62`)
- add a initial version of a contributing guide (:pull:`63`)


v0.2 (01 October 2020)
----------------------
- Support the :rst:dir:`testcode`, :rst:dir:`testsetup` and
  :rst:dir:`testcleanup` directives (:pull:`39`).
- Fix working with lines containing only the prompt and avoid changing the
  quotes of nested docstrings (:issue:`41`, :pull:`43`)
- Allow configuring ``blackdoc`` using ``pyproject.toml``
  (:issue:`40`, :pull:`45`, :pull:`47`)
- Add a ``force-exclude`` option (:pull:`49`)
- Document the options (:pull:`50`)


v0.1.2 (31 August 2020)
-----------------------
- Keep compatibility with ``black`` 20.8b1 (:issue:`33`, :pull:`34`)

v0.1.1 (14 June 2020)
---------------------
- Add pre-commit hook configuration (:pull:`26`, :pull:`27`)
- Document the release process (:pull:`29`)
- Make sure the tool returns a non-zero error code when encountering
  syntax errors (:pull:`28`)


v0.1 (30 May 2020)
------------------

- Add a CLI (:pull:`1`)
- Add support for ipython prompts (:pull:`4`)
- Add support for code blocks in rst files (:pull:`10`)
- Allow disabling / selectively enabling formats (:issue:`13`, :pull:`18`)
- Initial version of the documentation (:issue:`12`, :pull:`19`)
