# Python Markdown Processor speed comparison

For a professional project, I need to process a lot of MD very fast and that's why I needed to compare the available processors.

You can run this code by doing the following

```bash
-- Create your virtualenv, then
pip install -r requirements.txt
python test.perf.py
```

The results I have with i9-9880H, python 3.9:
```bash
markdown2 <function markdown at 0x10ab53a60> 74.59436702728271
markdown.core <function markdown at 0x10abafa60> 6.1474082469940186
marko <function convert at 0x10afb84c0> 18.505269050598145
mistletoe <function markdown at 0x10aff0d30> 4.843760967254639
```

You can comment out the code to understand the difference between the outputs but it doesn't work well. 

I'm currently looking for a solution to compare 2 HTML files independently of escaping or formatting. 

If you feel like it, be free to add a PR :rocket: