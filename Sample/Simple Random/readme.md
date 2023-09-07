# Simple Random Sample

This code uses numpy random choice method to return data frames with samples. The functions has two modes:
- mode='percentage': In this case you need to provide a size_smp as a percentage
- mode='n': In this case you should provide an integer smaller than the size of the original data frame.
You can also tweak two parameters:
- seed_smp: If not provided, it will use an pseudo arbitrary seed.
- repl: If you want samples with replacement, you should change to True.
