---
type: "corpus"
item_id: "627533a2d2edbd7b"
title: "Show HN: Pre Python 3.15 PEP 661 compat-sentinel"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50031926"
project_url: "https://pypi.org/project/compat-sentinel"
author: "owebeeone"
published_at: "2026-10-10T11:43:37Z"
captured_at: "2026-10-11T09:43:53+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-11"
pub_day: "2026-10-10"
tags:
  - 语料
  - hn_show
  - author_owebeeone
  - story_50031926
  - show_hn
metrics: {"points": 6, "comments": 1, "engagement_velocity": 6}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Pre Python 3.15 PEP 661 compat-sentinel

> [!info] 一句话导读
> Skip to main content

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50031926>
> 指标：点赞=6 · 评论=1 · engagement_velocity=6
> 作者：owebeeone　|　发布：2026-10-10T11:43:37Z
> 项目链接：<https://pypi.org/project/compat-sentinel>
> 采集：2026-10-11T09:43:53+08:00　|　id：`627533a2d2edbd7b`

## 正文

Skip to main content
 Switch to mobile version
Search PyPI
 search-focus#focusSearchField"
 data-search-focus-target="searchField">
Search
Help
Docs
Log in
Register
Help
Docs
Log in
Register
Deutsch
English
español
Esperanto
français
português (Brasil)
Ελληνικά
русский
українська
עברית
中文 (简体)
中文 (繁體)
日本語
한국어
Search PyPI
Search
compat-sentinel 0.1.2
PEP 661 sentinel for Python versions before 3.15
pip install compat-sentinel
Copy PIP instructions
project-tabs#tabKeydown"
 aria-label="Project description. Focus will be moved to the description.">
Description
project-tabs#tabKeydown"
 aria-label="Metadata. Focus will be moved to the metadata panel.">
Metadata
project-tabs#tabKeydown"
 aria-label="Files. Focus will be moved to the project files.">
Release files
project-tabs#tabKeydown"
 aria-label="Release history. Focus will be moved to the release history panel.">
Release history
compat-sentinel
PEP 661 sentinel for Python 3.10 and later.
On Python 3.15 and later, compat_sentinel.sentinel is the builtin. On older
interpreters it is a local implementation with the same constructor, copy
behavior, and pickle lookup.
from compat_sentinel import sentinel
MISSING = sentinel ( "MISSING" )
 DEFAULT = sentinel ( "DEFAULT" , repr = "" )
Each call returns a new object. A sentinel pickles back to itself when it can
be imported from its module under __name__ :
MISSING = sentinel ( "MISSING" )
class Box :
 SHORT = sentinel ( "Box.SHORT" )
A sentinel created in a local scope and never stored under that name does not
pickle. __module__ is taken from the caller and is writable; pickle uses the
value present at dump time.
int | MISSING and MISSING | str build a typing.Union .
pythonbackport-sentinel
pythonbackport-sentinel
0.1.0 claims the same 3.15 sentinel contract. Its current master does not
meet it. Construction, repr , truthiness, identity equality, and copy do work.
The caller lookup stops on sentinel.__new__ . Every sentinel reports
 __module__ == "sentinel.core" and a qualified name of sentinel.__new__ .
Pickle identity is a process-wide registry keyed by that module, that
qualified name, and the sentinel name. Two sentinel("MISSING") values
share one slot, and the later one replaces the earlier one. Unpickling the
first returns the second, including in a fresh process after the defining
module has been imported.
__reduce__ rebuilds through a private function. A new process unpickles a
sentinel without importing the module that defined it, and a custom repr
is dropped. A local sentinel that was never stored under its name still
pickles.
Assigning __module__ changes the attribute and leaves the pickle key
unchanged.
int | sentinel("A") raises TypeError on Python 3.13 because
 types.UnionType is not subscriptable. The same subscript is used on every
version before 3.14. On 3.14 the expression returns a typing.Union .
The package never uses builtins.sentinel . On 3.15, from sentinel import sentinel is still this class, so its pickles are not the builtin
module-and-name lookup.
tests/test_contract.py loads one implementation per run. The default is
 compat_sentinel . --sentinel=pybp loads pythonbackport-sentinel . On Python
3.13 the first command passes and the second fails all eight contract checks:
uv run --with pytest pytest -q
uv run --python 3.13 --with pytest --with pythonbackport-sentinel pytest -q --sentinel=pybp tests/test_contract.py
........................... [100%]
27 passed in 0.18s
FFFFFFFF [100%]
============================================ FAILURES ============================================
___________________________ test_caller_module_is_the_defining_module ____________________________
subjects =
def test_caller_module_is_the_defining_module(subjects) -> None:
> assert subjects.MISSING.__module__ == subjects.__name__
E AssertionError: assert 'sentinel.core' == 'contract_subjects'
E
E - contract_subjects
E + sentinel.core
tests/test_contract.py:71: AssertionError
_________________________ test_same_name_keeps_distinct_pickle_identity __________________________
subjects =
def test_same_name_keeps_distinct_pickle_identity(subjects) -> None:
 restored = pickle.loads(pickle.dumps(subjects.MISSING))
> assert restored is subjects.MISSING
E AssertionError: assert MISSING is MISSING
E + where MISSING = .MISSING
tests/test_contract.py:77: AssertionError
_________________________________ test_pickle_is_a_module_lookup _________________________________
subjects =
def test_pickle_is_a_module_lookup(subjects) -> None:
 blob = pickle.dumps(subjects.MISSING)
> assert subjects.__name__.encode() in blob
E AssertionError: assert b'contract_subjects' in b'\x80\x04\x95X\x00\x00\x00\x00\x00\x00\x00\x8c\rsentinel.core\x94\x8c\x15_reconstruct_sentinel\x94\x93\x94\x8c&sentinel.core\x00sentinel.__new__\x00MISSING\x94\x85\x94R\x94.'
E + where b'contract_subjects' = ()
E + where  = 'contract_subjects'.encode
E + where 'contract_subjects' = .__name__
tests/test_contract.py:84: AssertionError
___________________________ test_custom_repr_survives_in_a_new_process ___________________________
subjects =
def test_custom_repr_survives_in_a_new_process(subjects) -> None:
 report = _child("with-module", pickle.dumps(subjects.CUSTOM), subjects)
> assert report.get("is_custom") == "True", report
E AssertionError: {'is_custom': 'False', 'repr': 'CUSTOM'}
E assert 'False' == 'True'
E
E - True
E + False
tests/test_contract.py:91: AssertionError
___________________________ test_unpickle_requires_the_defining_module ___________________________
subjects =
def test_unpickle_requires_the_defining_module(subjects) -> None:
 report = _child("no-module", pickle.dumps(subjects.MISSING), subjects)
> assert report.get("error") == "ModuleNotFoundError", report
E AssertionError: {'ok': 'MISSING', 'module': 'sentinel.core'}
E assert None == 'ModuleNotFoundError'
E + where None = ('error')
E + where  = {'ok': 'MISSING', 'module': 'sentinel.core'}.get
tests/test_contract.py:98: AssertionError
______________________________ test_local_sentinel_is_not_picklable ______________________________
sentinel =
def test_local_sentinel_is_not_picklable(sentinel) -> None:
 value = sentinel("EPHEMERAL")
> with pytest.raises(pickle.PicklingError):
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E Failed: DID NOT RAISE PicklingError
tests/test_contract.py:104: Failed
_____________________________ test_module_assignment_controls_pickle _____________________________
subjects =
def test_module_assignment_controls_pickle(subjects) -> None:
 original = subjects.HOLDER.__module__
 subjects.HOLDER.__module__ = "not.a.real.module"
 try:
> with pytest.raises(pickle.PicklingError):
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E Failed: DID NOT RAISE PicklingError
tests/test_contract.py:112: Failed
___________________________ test_union_accepts_sentinel_on_either_side ___________________________
sentinel =
def test_union_accepts_sentinel_on_either_side(sentinel) -> None:
 value = sentinel("UNION")
> forward = int | value
 ^^^^^^^^^^^
tests/test_contract.py:120:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
site-packages/sentinel/core.py:276: in __ror__
 return _make_union(other, self)
 ^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
a = , b = UNION
def _make_union(a, b):
 """
 Build a ``Union`` instance that can be used in type expressions.
Tries the runtime ``types.UnionType`` (PEP 604, Python 3.10+)
 subscript syntax first, falling back to ``typing.Union``. Direct
 construction with ``types.UnionType((a, b))`` is intentionally
 avoided because it raises ``TypeError`` on Python 3.14+ where the
 runtime union class is the same as ``typing.Union`` and explicitly
 forbids manual instantiation.
 """
 # On Python 3.10-3.13 ``types.UnionType`` is a distinct class whose
 # subscript syntax (``UnionType[a, b]``) is the supported way of
 # constructing a runtime union.
 union_type = getattr(_types, "UnionType", None)
 if union_type is not None and union_type is not getattr(
 __import__("typing"), "Union", None
 ):
> return union_type[a, b]
 ^^^^^^^^^^^^^^^^
E TypeError: type 'types.UnionType' is not subscriptable
site-packages/sentinel/core.py:44: TypeError
==================================== short test summary info =====================================
FAILED tests/test_contract.py::test_caller_module_is_the_defining_module - AssertionError: assert 'sentinel.core' == 'contract_subjects'
FAILED tests/test_contract.py::test_same_name_keeps_distinct_pickle_identity - AssertionError: assert MISSING is MISSING
FAILED tests/test_contract.py::test_pickle_is_a_module_lookup - AssertionError: assert b'contract_subjects' in b'\x80\x04\x95X\x00\x00\x00\x00\x00\x00\x00\x8...
FAILED tests/test_contract.py::test_custom_repr_survives_in_a_new_process - AssertionError: {'is_custom': 'False', 'repr': 'CUSTOM'}
FAILED tests/test_contract.py::test_unpickle_requires_the_defining_module - AssertionError: {'ok': 'MISSING', 'module': 'sentinel.core'}
FAILED tests/test_contract.py::test_local_sentinel_is_not_picklable - Failed: DID NOT RAISE PicklingError
FAILED tests/test_contract.py::test_module_assignment_controls_pickle - Failed: DID NOT RAISE PicklingError
FAILED tests/test_contract.py::test_union_accepts_sentinel_on_either_side - TypeError: type 'types.UnionType' is not subscriptable
8 failed in 0.11s
Project links
Data verified by PyPI on Oct 8, 2026
Data provided by the project maintainers, verified at the time the release was uploaded to PyPI.
Issues
Repository
Source
Key dates
PyPI data
 Data sourced directly from PyPI's database.
Released:
 Oct 8, 2026
Latest release
1 maintainer
PyPI data
 Data sourced directly from PyPI's database.
owebeeone
Credits
Author: compat-sentinel contributors
GitHub Statistics
Data verified by PyPI on Oct 8, 2026
 The GitHub source repository was provided by the project maintainers and verified by PyPI at the time of upload. Stars, forks, and open issues/PRs are derived from that repository and have not been independently verified.
Repository
Stars:
Forks:
Open issues:
Open PRs:
License
MIT License (MIT License)
Requires
Python >=3.10
Provides Extra
dev
 test
Tags
compatibility
 pep661
 pickle
 sentinel
Classifiers
Development Status
3 - Alpha
Intended Audience
Developers
License
OSI Approved :: MIT License
Programming Language
Python :: 3
Python :: 3.10
Python :: 3.11
Python :: 3.12
Python :: 3.13
Python :: 3.14
Python :: 3.15
Report project as malware
Metadata
Project links
Data verified by PyPI on Oct 8, 2026
Data provided by the project maintainers, verified at the time the release was uploaded to PyPI.
Issues
Repository
Source
Key dates
PyPI data
 Data sourced directly from PyPI's database.
Released:
 Oct 8, 2026
Latest release
1 maintainer
PyPI data
 Data sourced directly from PyPI's database.
owebeeone
Credits
Author: compat-sentinel contributors
GitHub Statistics
Data verified by PyPI on Oct 8, 2026
 The GitHub source repository was provided by the project maintainers and verified by PyPI at the time of upload. Stars, forks, and open issues/PRs are derived from that repository and have not been independently verified.
Repository
Stars:
Forks:
Open issues:
Open PRs:
License
MIT License (MIT License)
Requires
Python >=3.10
Provides Extra
dev
 test
Tags
compatibility
 pep661
 pickle
 sentinel
Classifiers
Development Status
3 - Alpha
Intended Audience
Developers
License
OSI Approved :: MIT License
Programming Language
Python :: 3
Python :: 3.10
Python :: 3.11
Python :: 3.12
Python :: 3.13
Python :: 3.14
Python :: 3.15
Report project as malware
Release files for compat-sentinel 0.1.2
For a detailed explanation of source distributions (sdists) and built distributions (wheels), please see the package formats documentation .
Source distribution (sdist)
Source distribution for compat-sentinel 0.1.2
File
 Size
 Uploaded
compat_sentinel-0.1.2.tar.gz
14.1 kB
Oct 8, 2026
Details
Built distribution (wheel)
Table of built distributions (wheels) for compat-sentinel 0.1.2
File
Interpreter
ABI
Platform
Reset
compat_sentinel-0.1.2-py3-none-any.whl
7.2 kB
Oct 8, 2026
Python 3
none
any
Details
Total release size: 21.3 kB
Release files
 / compat_sentinel-0.1.2.tar.gz
Download URL
compat_sentinel-0.1.2.tar.gz
Size
 14.1 kB
Tags
Source
SHA-256 checksum
How to use checksums
7ff8db6e6f9aaef286de6801dfeb62e8291770f19a3491d2bb8c95d3e62cf32f
BLAKE2b-256 checksum
How to use checksums
87f996c20d278fd6be0073f3362fcf8bf6426e449c2ea6299806c3fbeb33a4e9
Upload date
Oct 8, 2026
Uploaded using Trusted Publishing?
What is trusted publishing?
Yes
Uploaded via
twine/7.0.0 CPython/3.13.14
Provenance
Provenance describes where a file came from. On PyPI, provenance is shared via attestations , which provide a verifiable record of the build or publishing details. View details, limitations and caveats.
PyPI Publish
Attestation
PyPI verified that this artifact, at this checksum, originated from the publisher listed below.
Signed by GitHub Actions, verified by PyPI on Oct 8, 2026.
Transparency log
Identity
Publishing platform
GitHub Actions
Publishing repository
github.com/owebeeone/compat-sentinel
Publishing commit
github.com/owebeeone/compat-sentinel/tree/f65bc4476bf8a6ca34c1f69a22c4b476b57c2ac3
Workflow
Publishing configuration
github.com/owebeeone/compat-sentinel/blob/f65bc4476bf8a6ca34c1f69a22c4b476b57c2ac3/.github/workflows/publish.yml
Publishing logs
github.com/owebeeone/compat-sentinel/actions/runs/37735015293/attempts/1
Artifact
Subject
compat_sentinel-0.1.2.tar.gz
SHA-256 checksum
7ff8db6e6f9aaef286de6801dfeb62e8291770f19a3491d2bb8c95d3e62cf32f
Verifying attestations
Release files
 / compat_sentinel-0.1.2-py3-none-any.whl
Download URL
compat_sentinel-0.1.2-py3-none-any.whl
Size
 7.2 kB
Tags
Python 3
SHA-256 checksum
How to use checksums
c211bb0b34b0ac808118196b49cec3cc1e7b4c1ad8a414ac11d7aafba963aa2a
BLAKE2b-256 checksum
How to use checksums
1a878a9c9007cf06726823551b1dad31ebba8e47c26934bb372696c9705de288
Upload date
Oct 8, 2026
Uploaded using Trusted Publishing?
What is trusted publishing?
Yes
Uploaded via
twine/7.0.0 CPython/3.13.14
Provenance
Provenance describes where a file came from. On PyPI, provenance is shared via attestations , which provide a verifiable record of the build or publishing details. View details, limitations and caveats.
PyPI Publish
Attestation
PyPI verified that this artifact, at this checksum, originated from the publisher listed below.
Signed by GitHub Actions, verified by PyPI on Oct 8, 2026.
Transparency log
Identity
Publishing platform
GitHub Actions
Publishing repository
github.com/owebeeone/compat-sentinel
Publishing commit
github.com/owebeeone/compat-sentinel/tree/f65bc4476bf8a6ca34c1f69a22c4b476b57c2ac3
Workflow
Publishing configuration
github.com/owebeeone/compat-sentinel/blob/f65bc4476bf8a6ca34c1f69a22c4b476b57c2ac3/.github/workflows/publish.yml
Publishing logs
github.com/owebeeone/compat-sentinel/actions/runs/37735015293/attempts/1
Artifact
Subject
compat_sentinel-0.1.2-py3-none-any.whl
SHA-256 checksum
c211bb0b34b0ac808118196b49cec3cc1e7b4c1ad8a414ac11d7aafba963aa2a
Verifying attestations
Release history
Release notifications |
 RSS feed
This release
0.1.2
 This release
Oct 8, 2026
2 release files
0.1.1
Oct 8, 2026
2 release files
0.1.0
Oct 7, 2026
2 release files
PyPI
Developed and maintained by the Python Software Foundation and Python community, for the Python community.
Status: all systems operational
Donate today!
Help
Installing packages
Uploading packages
User guide
Project name retention
FAQs
About PyPI
PyPI Blog
Infrastructure dashboard
Statistics
Logos & trademarks
Our sponsors
Contributing to PyPI
Bugs and feedback
Contribute on GitHub
Translate PyPI
Sponsor PyPI
Development credits
Using PyPI
Terms of Service
Report security issue
Code of conduct
Privacy Notice
Acceptable Use Policy
Switch to desktop version
Anthropic, PBC
 Visionary sponsor
Bloomberg
 Visionary sponsor
Hudson River Trading
 Visionary sponsor
Meta
 Visionary sponsor
NVIDIA
 Visionary sponsor
Microsoft
 Sustainability sponsor
Depot
 Continuous Integration
AWS
 Cloud computing and Security Sponsor
Datadog
 Monitoring
Fastly
 CDN
Google
 Download Analytics
Sentry
 Error logging
StatusPage
 Status page
"PyPI", "Python Package Index", and the blocks logos are registered trademarks of the Python Software Foundation .
© 2026 Python Software Foundation
Site map
Deployed from f43a0f7

## 评论（1/1）

> **owebeeone** · 2026-10-10T11:46:55.000Z　
> If you're like me, you don't want to wait for 3.15 to get it's features. Enjoy!

## 导航

- 项目页：[[10-项目/pypi.org_ec0c0b51]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
