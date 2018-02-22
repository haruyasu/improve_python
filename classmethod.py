class SampleClass:
    def sample_method(self):
        print "Hello World"

#SampleClass.sample_method()
#error

#########################
#instance
sample_class = SampleClass()
sample_class.sample_method()

#########################
#classmethod
class SampleClassMethod:
    @classmethod
    def sample_method(self):
        print "Hello ClassMethod"

SampleClassMethod.sample_method()

#########################
#static method
class DiffClassStaticMethod:
    @classmethod
    def class_method(*args):
        return args

    @staticmethod
    def static_method(*args):
        return args

print DiffClassStaticMethod.class_method()
print DiffClassStaticMethod.static_method()
