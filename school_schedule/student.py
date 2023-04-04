class Student:
    '''
    attributes: 
        -name -str
        -grade -str
        -classes -list
    methods: 
        -add_class, param: STR
        -get_num_classes, no params
        -summary, no params
        -pretty_print_each_class(), 
    '''
    
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes
        
    def __str__(self):
        return f"hi, Student {self.name}, {self.grade}, {self.classes}"
    
    def pretty_print_each_class(self):
        string = ''
        for item in self.classes:
            string += f" {item}, "
            if item[-1]:
                string += f"{item}."
        return string
    
    def add_class(self, class_name):
        self.classes.append(class_name)
        return self.classes
            
    def summary(self):
        pass
    
    def get_num_classes(self):
        pass