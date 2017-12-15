my_global_variable = 0;

def function():
    global my_global_variable
    my_global_variable = 1;
    print("Inside Func: ",end="");print(my_global_variable);

def function2():
    my_global_variable = -1;
    function()

    print("Inside Func 2: ", end="");

    print(my_global_variable);
    
    my_global_variable = 2;


function2();
print("Outside: ",end='');print(my_global_variable);

