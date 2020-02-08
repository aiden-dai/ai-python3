import re

"""
. any character
^ start with
$ end with
*  0 or more
+ 1 or more
? 0 or 1
```
{m} m repetitions
{m, n} m to n repetitions
[] a set of characters, for example, [amk]
[-] range, for example, [a-z], [0-9]
[^]  not.  for example, [^5], any values but 5
()  Groups

\d Matches any decimal digit, [0-9]
\D Not decimal digit [^0-9]
\s Matches Unicode whitespace characters , includes [\t\n\r\f\v]
\S Not a whitespace character. 
\w Matches Unicode word characters including _, [a-zA-Z0-9_]
\W Not unicode word characters [^a-zA-Z0-9_]
\b Matches the empty string, but only at the beginning or end of a word.  
\B Matches the empty string, but only when it is not at the beginning or end of a word

Sepcial characters use \

(?P<name>...) Similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name name. 


"""

# re.match(pattern, string) #return a corresponding match object.
# re.search(pattern, string) #looking for the first location, None if not found.

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.groups())  # ('Malcolm', 'Reynolds')
print(m.group(0))  # Entile match, Malcolm Reynolds
print(m.group(1))  # First () group, Malcolm
print(m.group('first_name'))  # group P<first_name>, Malcolm

s = re.search(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(s)  # <re.Match object; span=(0, 16), match='Malcolm Reynolds'>
print(s.span())  # (0, 16)
print(s.start())  # 0



# re.split(pattern, string, maxsplit=0, flags=0)
words = re.split(r'\W+', 'Words, words, words.')  #['Words', 'words', 'words', '']
print(words)

# re.comple(pattern) Compile a regular expression pattern into a regular expression object
str1 = '\\ab()|,.c'
cp1 = re.compile(r'\W')
repl = cp1.sub('', str1)
print(repl)  # abc

# This is equals to 
repl2 = re.sub(r'\W', '', str1)
print(repl2)  # abc

