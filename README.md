# Flask_Blog
A simple blog website created with Flask as back end framework

### Flask
### Jinja

Jinja2 is a full featured template engine for Python. It has full unicode 
support, an optional integrated sandboxed execution environment, widely used and 
BSD licensed 

Here i'm going to list only the featured that i have used inside this project 
for more details plese visit : http://jinja.pocoo.org 

###### VARIABLE

To simply pass a variable and print out its value without any modifications
we can simply use a pair of curly brackets, here an example:

```html
<h1>{{ title }}</h1>
```
And with this code we are printing out the content of the variable **title** as an *h1*, this varible is passed
as a parameter in the function **render_template**.
This method can be used not only to provide text to our page but also to define class,id,name
tag and many other in a straightforward way.
```html
<h1 class="{{ class }}"></h1>
<h1 id="{{ id }}"></h1>
```

###### IF STATEMENT

With the if statement we display different title depending on the variable **title**
that are passed in the **render_template** function.
```html
{% if title %}
    <title> TITLE </title>
{% else %}
    <title> NO TITLE </title>
{% endif %}
```

###### FOR STATEMENT
###### INCLUDE
###### EXTEND
###### BLOCK



### Other
