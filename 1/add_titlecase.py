import json
import os
import sys
from difflib import SequenceMatcher
from subprocess import STDOUT, check_output, TimeoutExpired
import yaml


prepositions = """
aboard
about
above
across
after
against
along
amid
among
anti
around
as
at
before
behind
below
beneath
beside
besides
between
beyond
but
by
concerning
considering
despite
down
during
except
excepting
excluding
following
for
from
in
inside
into
like
minus
near
of
off
on
onto
opposite
outside
over
past
per
plus
regarding
round
save
since
than
through
to
toward
towards
under
underneath
unlike
until
up
upon
versus
via
with
within
without

having
using
""".split()


conjunctions = """
and
but
for
nor
or
so
yet
""".split()

articles = """
a
an
the
""".split()

terms = """
ph
"""


def titlecase_word(w):
    if w.lower() in prepositions:
        return w
    if w.lower() in conjunctions:
        return w
    if w.lower() in articles:
        return w
    if w.lower() in terms:
        return w
    if w[0] in "abcdefghijklmnopqrstuvwxyz":
        return w[0].upper() + w[1:]
    return w


def titlecase(s):
    words = s.split()
    print(words, file=sys.stderr)
    t = []
    for w in words:
        t.append(titlecase_word(w))
    print(t, file=sys.stderr)
    return " ".join(t)




import json
import sys

id = sys.argv[1]

with open(f"master/{id}.json") as f:
    data = json.load(f)

if "titlee.original" not in data:
    data["titlee.original"] = data["titlee"]
data["titlee"] = titlecase(data["titlee"])

with open(f"master/{id}.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)
