# Perceptron
Implementation of (3-bit input / 1-bit output / 1-layer) neural network.

![alt text](
https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Perceptron.svg/1280px-Perceptron.svg.png
)

![alt text](/AI/perceptron_training_data.png)

## Results
Output of [__table_print.py__](python/AI/table_print.py)

<p style='color:red'>Column Inputs and Expected Outputs consisit training data.</p>
<p style='color:blue'>Words <before/after> means before/after training</p>

```
Training iterations: 10000

Inputs Expected Outputs Outputs before Outputs after    Differences    
------ ---------------- -------------- ------------- ------------------
 0 0 1                0      0.2689864    0.00966449        -0.25932191
 1 1 1                1      0.3262757    0.99211957         0.66584387
 1 0 1                1     0.23762817    0.99358898 0.7559608099999999
 0 1 1                0     0.36375058    0.00786506        -0.35588552
Differences sum: 0.80659725

Weights before Weights after
-------------- -------------
   -0.16595599    9.67299303
    0.44064899    -0.2078435
   -0.99977125   -4.62963669

Process finished with exit code 0
```


## Files
- [__perceptron.py__](python/AI/perceptron.py)
- [__perceptron_main.py__](/python/AI/perceptron_main.py)  
- [__table_print.py__](python/AI/table_print.py)

## See also

[Wiki: Perceptron](https://www.wikiwand.com/en/Perceptron#)
[Wiki: Comparison of activation functions](https://www.wikiwand.com/en/Activation_function#/Comparison_of_activation_functions)

[How to build a simple neural network in 9 lines of Python code](https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1)
[A Neural Network in 11 lines of Python (Part 1)](https://iamtrask.github.io/2015/07/12/basic-python-network/)

