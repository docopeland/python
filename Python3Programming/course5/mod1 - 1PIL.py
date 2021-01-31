# this course uses jupyter, but I will use IntelliJ

# The Python Imaging Library (PIL)
# The Python Imaging Library, which is known as PIL or PILLOW, is the main library we use in python for dealing with
# image files.

# You'll recall that we import a library using the `import` keyword.
import PIL
# Documentation is a big help in learning a library. There exist standards that make this process easier.
# For example, most libraries let you check their version using the version attribute.
PIL.__version__

# Let's figure out how to open an image with `Pillow`. Python provides some built-in functions to help us
# understand the functions and objects which are available in libraries. For instance, the help function,
# when called on any object, returns the object’s built-in documentation. Lets try it with our new library
# module, PIL.
help(PIL)

# This shows us that there are a host of classes available to us in the module, as well as version information
# and even the file, called __init__.py, which has the source code for the module itself. We could look up
# the source code for this in the Jupyter console if we wanted to. These documentation standards make it easy
# to poke around an unexplored library.
#
# Python also has a function called dir() which will list the contents of an object. This is especially useful
# with modules where you might want to see what classes you might interact with. Lets list the details of
# the PIL module
dir(PIL)

# At the top of the list, there is something called Image. This sounds like it could be interesting, so lets
# import it directly, and run the help command on it.
from PIL import Image
help(Image)

# Lets call help on the open function to see what it's all about. Remember that since we want to pass in the
# function reference, and not run the function itself, we don't put paretheses behind the function name.
help(Image.open)

# It looks like Image.open() is a function that loads an image from a file and returns an instance
# of the Image class. Lets give it a try. In the read_only directory there is an image I've provided
# which is from our Master's of Information program recruitment flyer. Lets try and load that now
file = "readonly/msi_recruitment.gif"
image = Image.open(file)
print(image)

# Ok, we see that this returns us a kind of PIL.GifImagePlugin.GifImageFile. At first this might
# seem a bit confusing, since because we were told by the docs that we should be exepcting a
# PIL.Image.Image object back. But this is just object inheritance working! In fact, the object
# returned is both an Image and a GifImageFile. We can use the python inspect module to see this
# as the getmro function will return a list of all of the classes that are being inherited by a
# given object. Lets try it.
import inspect
print("The type of the image is " + str(type(image)))
inspect.getmro(type(image))

# Now that we are comfortable with the object. How do we view the image? It turns out that the
# image object has a show function. You can find this by looking at all of the properties of
# the object if you wanted to, using the dir() function.
image.show()

# Hrm, that didn't seem to have the intended effect. The problem is that the image is stored
# remotely, on Coursera's server, but show tries to show it locally to you. So, if the Coursera
# server software was running on someone's workstation in Mountain View California, where Coursera
# has its offices, then you just popped up a picture of our recruitment materials. Thanks! :)
# Instead, we want to render the image in the Jupyter notebook. It turns out Jupyter has a function
# which can help with this.
# NB: IPython does not work for me, I think it only works on Jupyter
from IPython.display import display
display(image)