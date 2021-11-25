import markdown2
import time
import glob2
import markdown
import marko
import mistletoe
import difflib
import re


def remove_whitespace(string):
    newString = re.sub(re.compile(r'(\s)+'), '', string)
    newString = re.sub(re.compile(r'\&\S+;'), '', newString)
    newString = re.sub(re.compile(r'[\"\']+'), '', newString)
    return newString


all_test_files = glob2.glob('tests/**/*.md')
print("Test run on", len(all_test_files), "files")
tested = [markdown2.markdown, markdown.markdown, marko.convert, mistletoe.markdown]
results = [[] for x in tested]
for i, t in enumerate(tested):
    start = time.time()
    for f in all_test_files:
        with open(f) as md:
            results[i].append(t(md.read()))
    end = time.time()
    print(t.__module__,t, end-start)


# Calculates diff between libs
# report = ""
# for testIndex, test in enumerate(results[0]):
#     for otherTestIndex, othertests in enumerate(results[1:]):
#         if remove_whitespace(test) != remove_whitespace(othertests[testIndex]):
#             report = difflib.HtmlDiff(wrapcolumn=80).make_file(test.splitlines(), othertests[testIndex].splitlines(), '1', str(otherTestIndex))
#             with open('diff{}.html'.format(testIndex), 'w+') as export:
#                 export.write(report)
