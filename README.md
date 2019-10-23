# Procedures

These are our preferred coding practices.

## Git
All repos are set with "dev" branch as default. 
Production, and staging are used also. Staging should only merge from dev and production should only merge from staging. 

When doing work, it's best to create branches off dev. Naming the branch with easily understandable titles is preferred. Alternatively, if the branch intention is to fix an issue, you may name the branch issue_XXX.

### Push code often!
We prefer you push code often. It's better to have more commits than less. The reason is we often have multiple people on a project and need to keep track of progress. I also need information to tell the client with regards to work.

### Use Pull Requests
When a branch is ready, issue a PR so that team members can review and comment on code.  
If you see a PR, look over the code and comment "ok" so we know it's ok to merge.

## Naming
Use easily understandable names wherever possible. This includes variables, templates, views etc. Avoid using acronyms. Consider the fact that the code may be dormant for a year and then someone returns for bug fixes. Will they understand your code and names?

We prefer to name templates, urls, and views with identical names for easy identification. Example:

```
views: 
def helloWorld(request):
  return render(request, 'hello_world.html')
  
urls:
  path('/hello_world/', views.helloWorld, name='hello_world')
  
template:
hello_world.html
```

## Pip
We use pip-tools.

Usage is easy: put all requirements into the file with suffix .in. For example `base.in`  
Compile dependencies: `pip-compile base.in`  
This will create the list of requirements. `base.txt`  
Afterwards install/update: `pip-sync base.txt`  

## Deployment
We typically deploy on heroku for staging. Instructions can be found here:  
[https://github.com/tkwon/idea-procedure/blob/master/doc/heroku.md](https://github.com/tkwon/idea-procedure/blob/master/doc/heroku.md)
