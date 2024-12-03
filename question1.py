#pipeline functions

def pipeline(functions):
    def apply_pipeline(x):
        for func in functions:
            x = func(x)
        return x
    return apply_pipeline

pipeline_funcs = [lambda x: x + 1, lambda x: x * 2]
pipe = pipeline(pipeline_funcs)
print(pipe(3))  # Output: 8