#Define a static variable and access that through a class
class example:
    static_variable=12;

print(example.static_variable);   



#Define a static variable and access that through a instance
instance = example();
print(instance.static_variable);

#Define a static variable and change within the instance
instance.static_variable=29;
print(instance.static_variable);


#Define a static variable and change within the class
class example2:
    static_variable=40;

example2.static_variable=80;
print(example2.static_variable);