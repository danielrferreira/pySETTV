# File Import (input file -> pandas DataFrame)

90% of time a simple pandas [read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) will do the trick, but I also added two options:
1) [Function](https://github.com/danielrferreira/pySTETV/tree/main/06%20-%20Utility%20%26%20References/File%20Import/Multiple%20Formats) that import 5 different types of files without having to mention with type you are trying to import into a data
2) [Import CSV](https://github.com/danielrferreira/pySTETV/tree/main/Utility/File%20Import/Import%20from%20scratch) from scratch if you want to dig and try something different. This one is not optimized for memory usage, since it loads the whole file into memory twice.
